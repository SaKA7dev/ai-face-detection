"""
AI Hand Gesture Volume Controller
Built by Aarav Shukla — Class 9
"""

import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(
    page_title="Gesture Volume · Aarav Shukla",
    page_icon="🤚",
    layout="centered",
)

# ── CSS ───────────────────────────────────────────────────────────────────────
st.markdown("""<style>
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&family=Fira+Code:wght@400;500;600&display=swap');

:root {
    --bg: #0a0a0f;
    --card: #12121a;
    --border: #1e1e2e;
    --text: #e4e4e7;
    --muted: #52525b;
    --sub: #71717a;
    --accent: #8b5cf6;
}

.stApp {
    background: var(--bg) !important;
    font-family: 'Inter', sans-serif !important;
    color: var(--text);
}
header[data-testid="stHeader"] { background: transparent !important; }
#MainMenu, footer { visibility: hidden !important; }
.block-container { padding-top: 1.5rem !important; max-width: 720px !important; }

.app-header { text-align: center; padding: 1.5rem 0 1rem; }
.app-badge {
    display: inline-block; padding: 4px 10px; border-radius: 4px;
    background: var(--card); border: 1px solid var(--border);
    color: var(--muted); font-size: 0.62rem; font-weight: 500;
    font-family: 'Fira Code', monospace; letter-spacing: 0.06em;
    margin-bottom: 0.6rem;
}
.app-title {
    font-size: 1.9rem; font-weight: 700; color: var(--text);
    letter-spacing: -0.03em; margin: 0 0 0.3rem;
}
.app-title-accent { color: var(--accent); }
.app-author { font-size: 1rem; font-weight: 600; color: var(--text); margin: 0.5rem 0 0.2rem; }
.app-author span { color: var(--accent); font-weight: 700; }
.app-desc { color: var(--sub); font-size: 0.8rem; line-height: 1.5; margin: 0 auto; max-width: 440px; }

.info-grid { display: grid; grid-template-columns: repeat(4, 1fr); gap: 8px; margin: 1rem 0; }
.info-item {
    background: var(--card); border: 1px solid var(--border);
    border-radius: 10px; padding: 10px 6px; text-align: center;
}
.info-val { color: var(--text); font-size: 1.1rem; font-weight: 700; font-family: 'Fira Code', monospace; }
.info-label { color: var(--muted); font-size: 0.58rem; font-weight: 500; letter-spacing: 0.06em; text-transform: uppercase; margin-top: 3px; }

.section-card {
    background: var(--card); border: 1px solid var(--border);
    border-radius: 12px; padding: 14px 16px; margin: 8px 0;
}
.section-header { display: flex; align-items: center; gap: 8px; margin-bottom: 8px; }
.section-dot { width: 7px; height: 7px; border-radius: 50%; background: var(--accent); }
.section-dot.green { background: #22c55e; }
.section-title {
    color: var(--muted); font-size: 0.65rem; font-weight: 600;
    letter-spacing: 0.08em; text-transform: uppercase;
    font-family: 'Fira Code', monospace;
}

.steps-list { list-style: none; padding: 0; margin: 0; }
.step-item { display: flex; align-items: flex-start; gap: 10px; padding: 6px 0; border-bottom: 1px solid rgba(30,30,46,0.5); }
.step-item:last-child { border-bottom: none; }
.step-num {
    flex-shrink: 0; width: 22px; height: 22px; border-radius: 5px;
    background: rgba(139,92,246,0.1); border: 1px solid rgba(139,92,246,0.15);
    color: var(--accent); font-size: 0.6rem; font-weight: 600;
    font-family: 'Fira Code', monospace;
    display: flex; align-items: center; justify-content: center;
}
.step-text { color: var(--sub); font-size: 0.78rem; line-height: 1.4; }
.step-text strong { color: var(--text); font-weight: 600; }

.app-footer { text-align: center; padding: 1.2rem 0; border-top: 1px solid var(--border); margin-top: 1rem; }
.footer-name { color: var(--text); font-weight: 700; font-size: 1.05rem; }
.footer-sub { color: var(--muted); font-size: 0.7rem; margin-top: 3px; }
.footer-tech { display: flex; justify-content: center; gap: 6px; margin-top: 8px; flex-wrap: wrap; }
.tech-pill {
    padding: 3px 9px; border-radius: 100px; background: var(--card);
    border: 1px solid var(--border); color: var(--muted); font-size: 0.6rem;
    font-family: 'Fira Code', monospace; font-weight: 500;
}

.stApp iframe { border-radius: 12px !important; }
</style>""", unsafe_allow_html=True)

# ── Header ────────────────────────────────────────────────────────────────────
st.markdown("""
<div class="app-header">
    <div class="app-badge">COMPUTER VISION PROJECT</div>
    <h1 class="app-title">Gesture <span class="app-title-accent">Volume</span> Control</h1>
    <p class="app-author">Built by <span>Aarav Shukla</span> · Class 9</p>
    <p class="app-desc">
        Real-time hand tracking that maps thumb-index finger
        distance to audio volume using MediaPipe hand landmarks.
    </p>
</div>
""", unsafe_allow_html=True)

st.markdown("""
<div class="info-grid">
    <div class="info-item"><div class="info-val">720p</div><div class="info-label">Resolution</div></div>
    <div class="info-item"><div class="info-val">30</div><div class="info-label">FPS Target</div></div>
    <div class="info-item"><div class="info-val">21</div><div class="info-label">Landmarks</div></div>
    <div class="info-item"><div class="info-val">1</div><div class="info-label">Hand</div></div>
</div>
""", unsafe_allow_html=True)

# ── Client-side camera + hand detection + audio ──────────────────────────────
COMPONENT = """
<style>
*{margin:0;padding:0;box-sizing:border-box}
body{background:#0a0a0f;overflow:hidden}
#wrap{width:100%;background:#000;position:relative;border-radius:12px 12px 0 0;overflow:hidden}
#out{width:100%;display:block}
#load{position:absolute;top:50%;left:50%;transform:translate(-50%,-50%);
      color:#71717a;font:500 13px 'Inter',sans-serif;text-align:center}
#load .spinner{width:28px;height:28px;border:3px solid #1e1e2e;border-top:3px solid #8b5cf6;
               border-radius:50%;animation:spin 0.8s linear infinite;margin:0 auto 10px}
@keyframes spin{to{transform:rotate(360deg)}}
#ctrl{background:#12121a;padding:12px 14px;display:flex;align-items:center;gap:12px;
      border-top:1px solid #1e1e2e}
#pbtn{background:linear-gradient(135deg,#8b5cf6,#7c3aed);border:none;color:#fff;
      width:36px;height:36px;border-radius:8px;cursor:pointer;font-size:15px;
      display:flex;align-items:center;justify-content:center}
#cinfo{flex:1}
#cinfo-top{display:flex;justify-content:space-between;margin-bottom:4px}
#sname{color:#e4e4e7;font:500 12px 'Inter',sans-serif}
#vpct{color:#8b5cf6;font:600 11px 'Fira Code',monospace}
#vtrack{width:100%;height:5px;background:#1e1e2e;border-radius:99px;overflow:hidden}
#vfill{height:100%;width:0%;border-radius:99px;background:#8b5cf6;transition:width .15s}
#sline{text-align:center;padding:6px;color:#52525b;font:500 10px 'Fira Code',monospace;
       background:#12121a;border-radius:0 0 12px 12px}
</style>

<div>
  <div id="wrap">
    <video id="cam" playsinline style="display:none"></video>
    <canvas id="out"></canvas>
    <div id="load"><div class="spinner"></div>Loading hand tracking...</div>
  </div>
  <div id="ctrl">
    <button id="pbtn" onclick="tgl()">&#9654;</button>
    <div id="cinfo">
      <div id="cinfo-top"><span id="sname">SoundHelix Song 1</span><span id="vpct">0%</span></div>
      <div id="vtrack"><div id="vfill"></div></div>
    </div>
  </div>
  <div id="sline">Show your hand to control volume</div>
</div>

<audio id="aud" loop preload="auto"
  src="https://www.soundhelix.com/examples/mp3/SoundHelix-Song-1.mp3"></audio>

<script src="https://cdn.jsdelivr.net/npm/@mediapipe/hands/hands.js" crossorigin="anonymous"></script>
<script src="https://cdn.jsdelivr.net/npm/@mediapipe/camera_utils/camera_utils.js" crossorigin="anonymous"></script>

<script>
const vid=document.getElementById('cam'),
      can=document.getElementById('out'),
      ctx=can.getContext('2d'),
      aud=document.getElementById('aud'),
      pb=document.getElementById('pbtn'),
      vp=document.getElementById('vpct'),
      vf=document.getElementById('vfill'),
      sl=document.getElementById('sline'),
      ld=document.getElementById('load');

const CN=[[0,1],[1,2],[2,3],[3,4],[0,5],[5,6],[6,7],[7,8],
          [0,9],[9,10],[10,11],[11,12],[0,13],[13,14],[14,15],[15,16],
          [0,17],[17,18],[18,19],[19,20],[5,9],[9,13],[13,17]];

let vol=0, playing=false, det=false;

function tgl(){
  if(!playing){
    aud.play().then(()=>{
      playing=true; pb.innerHTML='&#9646;&#9646;';
      sl.textContent='Playing — gesture controls active';
      sl.style.color='#22c55e';
    }).catch(()=>{
      sl.textContent='Tap again (browser blocked autoplay)';
      sl.style.color='#f59e0b';
    });
  }else{
    aud.pause(); playing=false; pb.innerHTML='&#9654;';
    sl.textContent='Paused'; sl.style.color='#52525b';
  }
}

function vc(v){return v<30?'#3c8ce7':v<65?'#22c55e':'#8b5cf6'}

function onRes(r){
  const w=can.width, h=can.height;
  ctx.save(); ctx.clearRect(0,0,w,h);
  ctx.translate(w,0); ctx.scale(-1,1);
  ctx.drawImage(r.image,0,0,w,h);
  ctx.restore();

  det=r.multiHandLandmarks&&r.multiHandLandmarks.length>0;

  if(det){
    const lm=r.multiHandLandmarks[0];
    const p=lm.map(l=>({x:(1-l.x)*w, y:l.y*h}));

    ctx.strokeStyle='#8b5cf6'; ctx.lineWidth=2;
    for(const[a,b]of CN){ctx.beginPath();ctx.moveTo(p[a].x,p[a].y);ctx.lineTo(p[b].x,p[b].y);ctx.stroke()}

    for(let i=0;i<p.length;i++){
      ctx.beginPath();
      if(i===4||i===8){
        ctx.arc(p[i].x,p[i].y,8,0,Math.PI*2);ctx.fillStyle='#dcd6ff';ctx.fill();
        ctx.strokeStyle='#8b5cf6';ctx.lineWidth=2;ctx.stroke();
      }else{
        ctx.arc(p[i].x,p[i].y,3,0,Math.PI*2);ctx.fillStyle='#b4b4bc';ctx.fill();
      }
    }

    const t=p[4],ix=p[8];
    const d=Math.sqrt((t.x-ix.x)**2+(t.y-ix.y)**2);
    const raw=Math.max(0,Math.min(100,(d-20)*100/140));
    vol=vol*0.55+raw*0.45;
    const c=vc(vol);

    ctx.beginPath();ctx.moveTo(t.x,t.y);ctx.lineTo(ix.x,ix.y);
    ctx.strokeStyle=c;ctx.lineWidth=2;ctx.stroke();

    const mx=(t.x+ix.x)/2, my=(t.y+ix.y)/2, mr=5+vol*0.12;
    ctx.beginPath();ctx.arc(mx,my,mr,0,Math.PI*2);ctx.fillStyle=c;ctx.fill();
    ctx.strokeStyle='#fff';ctx.lineWidth=1;ctx.stroke();

    const vi=Math.round(vol);
    ctx.font='600 13px "Fira Code",monospace';ctx.fillStyle='#fff';
    ctx.textAlign='center';ctx.fillText(vi+'%',mx,my-mr-6);

    aud.volume=Math.max(0,Math.min(1,vol/100));
  }

  // arc meter
  const vi=Math.round(vol),cx=w-50,cy=h-50,rd=32;
  const sa=135*Math.PI/180, sw=270*Math.PI/180, ea=sa+sw*vol/100;
  ctx.beginPath();ctx.arc(cx,cy,rd,sa,sa+sw);ctx.strokeStyle='#19191f';ctx.lineWidth=2;ctx.stroke();
  if(vol>0){ctx.beginPath();ctx.arc(cx,cy,rd,sa,ea);ctx.strokeStyle=vc(vol);ctx.lineWidth=3;ctx.stroke()}
  ctx.font='500 13px "Fira Code",monospace';ctx.fillStyle='#e4e4e7';ctx.textAlign='center';
  ctx.fillText(vi+'%',cx,cy+4);
  ctx.font='500 8px "Fira Code",monospace';ctx.fillStyle='#5a5a6e';ctx.fillText('VOL',cx,cy+15);

  // status top-left
  ctx.fillStyle='rgba(0,0,0,0.55)';ctx.fillRect(0,0,150,26);
  ctx.beginPath();ctx.arc(13,13,4,0,Math.PI*2);
  ctx.fillStyle=det?'#22c55e':'#505064';ctx.fill();
  ctx.font='500 10px "Fira Code",monospace';ctx.textAlign='left';
  ctx.fillText(det?'TRACKING':'SHOW HAND',25,17);

  // branding top-right
  ctx.fillStyle='rgba(0,0,0,0.45)';ctx.fillRect(w-130,0,130,22);
  ctx.font='500 10px "Fira Code",monospace';ctx.fillStyle='#8b5cf6';
  ctx.textAlign='right';ctx.fillText('AARAV SHUKLA',w-6,15);

  const cl=Math.round(Math.max(0,Math.min(100,vol)));
  vp.textContent=cl+'%';vf.style.width=cl+'%';
  vf.style.background=vc(vol);
}

const hands=new Hands({locateFile:f=>`https://cdn.jsdelivr.net/npm/@mediapipe/hands/${f}`});
hands.setOptions({maxNumHands:1,modelComplexity:0,minDetectionConfidence:0.5,minTrackingConfidence:0.5});
hands.onResults(onRes);

const mob=/Android|iPhone|iPad|iPod/i.test(navigator.userAgent);
const cw=mob?640:1280, ch=mob?480:720;

const camera=new Camera(vid,{
  onFrame:async()=>{await hands.send({image:vid})},
  width:cw,height:ch,facingMode:'user'
});

camera.start().then(()=>{
  can.width=cw;can.height=ch;ld.style.display='none';
}).catch(e=>{
  ld.innerHTML='Camera access denied.<br>Please allow camera and reload.';
  ld.style.color='#f59e0b';
});
</script>
"""

components.html(COMPONENT, height=540)

# ── How It Works ──────────────────────────────────────────────────────────────
st.markdown("""
<div class="section-card">
    <div class="section-header">
        <div class="section-dot"></div>
        <span class="section-title">How It Works</span>
    </div>
    <ul class="steps-list">
        <li class="step-item">
            <div class="step-num">01</div>
            <div class="step-text">Allow <strong>camera access</strong> when prompted.</div>
        </li>
        <li class="step-item">
            <div class="step-num">02</div>
            <div class="step-text">Raise your hand — the AI detects <strong>21 landmarks</strong> in real-time.</div>
        </li>
        <li class="step-item">
            <div class="step-num">03</div>
            <div class="step-text"><strong>Pinch</strong> your thumb &amp; index finger → volume goes down.</div>
        </li>
        <li class="step-item">
            <div class="step-num">04</div>
            <div class="step-text"><strong>Spread</strong> them apart → volume goes up.</div>
        </li>
        <li class="step-item">
            <div class="step-num">05</div>
            <div class="step-text">Press <strong>▶</strong> to play audio — volume changes <strong>in real-time</strong> with your gesture.</div>
        </li>
    </ul>
</div>
""", unsafe_allow_html=True)

# ── Footer ────────────────────────────────────────────────────────────────────
st.markdown("""
<div class="app-footer">
    <div class="footer-name">Aarav Shukla</div>
    <div class="footer-sub">Class 9 · Computer Vision Project</div>
    <div class="footer-tech">
        <span class="tech-pill">Python</span>
        <span class="tech-pill">OpenCV</span>
        <span class="tech-pill">MediaPipe</span>
        <span class="tech-pill">Streamlit</span>
    </div>
</div>
""", unsafe_allow_html=True)
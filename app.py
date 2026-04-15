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
.block-container { padding-top: 1.2rem !important; max-width: 720px !important; }

.app-header { text-align: center; padding: 1.2rem 0 0.8rem; }
.app-badge {
    display: inline-block; padding: 4px 10px; border-radius: 4px;
    background: var(--card); border: 1px solid var(--border);
    color: var(--muted); font-size: 0.6rem; font-weight: 500;
    font-family: 'Fira Code', monospace; letter-spacing: 0.06em;
    margin-bottom: 0.5rem;
}
.app-title {
    font-size: 1.8rem; font-weight: 700; color: var(--text);
    letter-spacing: -0.03em; margin: 0 0 0.2rem;
}
.app-title-accent { color: var(--accent); }
.app-author {
    font-size: 1.05rem; font-weight: 600; color: var(--text);
    margin: 0.4rem 0 0.2rem;
}
.app-author span { color: var(--accent); font-weight: 700; }
.app-desc {
    color: var(--sub); font-size: 0.78rem; line-height: 1.4;
    margin: 0 auto; max-width: 440px;
}

.info-grid { display: grid; grid-template-columns: repeat(4, 1fr); gap: 6px; margin: 0.8rem 0; }
.info-item {
    background: var(--card); border: 1px solid var(--border);
    border-radius: 8px; padding: 8px 4px; text-align: center;
}
.info-val {
    color: var(--text); font-size: 1rem; font-weight: 700;
    font-family: 'Fira Code', monospace;
}
.info-label {
    color: var(--muted); font-size: 0.55rem; font-weight: 500;
    letter-spacing: 0.06em; text-transform: uppercase; margin-top: 2px;
}

.section-card {
    background: var(--card); border: 1px solid var(--border);
    border-radius: 10px; padding: 12px 14px; margin: 6px 0;
}
.section-header { display: flex; align-items: center; gap: 7px; margin-bottom: 6px; }
.section-dot { width: 6px; height: 6px; border-radius: 50%; background: var(--accent); }
.section-dot.green { background: #22c55e; }
.section-title {
    color: var(--muted); font-size: 0.62rem; font-weight: 600;
    letter-spacing: 0.08em; text-transform: uppercase;
    font-family: 'Fira Code', monospace;
}

.steps-list { list-style: none; padding: 0; margin: 0; }
.step-item {
    display: flex; align-items: flex-start; gap: 8px; padding: 5px 0;
    border-bottom: 1px solid rgba(30,30,46,0.5);
}
.step-item:last-child { border-bottom: none; }
.step-num {
    flex-shrink: 0; width: 20px; height: 20px; border-radius: 4px;
    background: rgba(139,92,246,0.1); border: 1px solid rgba(139,92,246,0.15);
    color: var(--accent); font-size: 0.55rem; font-weight: 600;
    font-family: 'Fira Code', monospace;
    display: flex; align-items: center; justify-content: center;
}
.step-text { color: var(--sub); font-size: 0.74rem; line-height: 1.35; }
.step-text strong { color: var(--text); font-weight: 600; }

.app-footer {
    text-align: center; padding: 1rem 0; border-top: 1px solid var(--border);
    margin-top: 0.8rem;
}
.footer-name { color: var(--text); font-weight: 700; font-size: 1rem; }
.footer-sub { color: var(--muted); font-size: 0.68rem; margin-top: 2px; }
.footer-tech {
    display: flex; justify-content: center; gap: 5px; margin-top: 6px; flex-wrap: wrap;
}
.tech-pill {
    padding: 2px 8px; border-radius: 100px; background: var(--card);
    border: 1px solid var(--border); color: var(--muted); font-size: 0.58rem;
    font-family: 'Fira Code', monospace; font-weight: 500;
}

.stApp iframe { border-radius: 10px !important; }

.tip-box {
    background: rgba(139,92,246,0.08); border: 1px solid rgba(139,92,246,0.2);
    border-radius: 8px; padding: 8px 12px; margin: 6px 0; text-align: center;
}
.tip-box p {
    color: var(--sub); font-size: 0.72rem; margin: 0; line-height: 1.4;
}
.tip-box strong { color: var(--accent); }

@media (max-width: 600px) {
    .block-container { padding-top: 0.6rem !important; }
    .app-header { padding: 0.6rem 0 0.4rem; }
    .app-title { font-size: 1.4rem; }
    .app-author { font-size: 0.9rem; }
    .app-desc { font-size: 0.72rem; }
    .info-grid { gap: 4px; margin: 0.5rem 0; }
    .info-item { padding: 6px 3px; border-radius: 6px; }
    .info-val { font-size: 0.85rem; }
    .info-label { font-size: 0.5rem; }
    .section-card { padding: 10px 12px; margin: 5px 0; }
    .step-text { font-size: 0.7rem; }
    .app-footer { padding: 0.8rem 0; }
}
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
    <div class="info-item"><div class="info-val">30</div><div class="info-label">FPS</div></div>
    <div class="info-item"><div class="info-val">21</div><div class="info-label">Landmarks</div></div>
    <div class="info-item"><div class="info-val">1</div><div class="info-label">Hand</div></div>
</div>
""", unsafe_allow_html=True)

# ── How It Works (ABOVE camera) ──────────────────────────────────────────────
st.markdown("""
<div class="section-card">
    <div class="section-header">
        <div class="section-dot"></div>
        <span class="section-title">How It Works</span>
    </div>
    <ul class="steps-list">
        <li class="step-item">
            <div class="step-num">01</div>
            <div class="step-text">Allow <strong>camera access</strong> when prompted below.</div>
        </li>
        <li class="step-item">
            <div class="step-num">02</div>
            <div class="step-text">Raise your hand — AI detects <strong>21 landmarks</strong> in real-time.</div>
        </li>
        <li class="step-item">
            <div class="step-num">03</div>
            <div class="step-text"><strong>Pinch</strong> thumb &amp; index finger → volume goes down.</div>
        </li>
        <li class="step-item">
            <div class="step-num">04</div>
            <div class="step-text"><strong>Spread</strong> them apart → volume goes up.</div>
        </li>
        <li class="step-item">
            <div class="step-num">05</div>
            <div class="step-text">Press <strong>▶</strong> to play audio — volume follows your gesture.</div>
        </li>
    </ul>
</div>
""", unsafe_allow_html=True)

# ── Tip for best experience ──────────────────────────────────────────────────
st.markdown("""
<div class="tip-box">
    <p>💻 For the <strong>best experience</strong>, open this on a <strong>laptop or desktop</strong>. Works on mobile too but laptop gives smoother tracking.</p>
</div>
""", unsafe_allow_html=True)

# ── Client-side camera + hand detection + audio ──────────────────────────────
COMPONENT = """
<style>
*{margin:0;padding:0;box-sizing:border-box}
body{background:transparent;overflow:hidden}
#wrap{width:100%;background:#000;position:relative;border-radius:10px 10px 0 0;overflow:hidden}
#out{width:100%;display:block}
#load{position:absolute;top:50%;left:50%;transform:translate(-50%,-50%);
      color:#71717a;font:500 13px 'Inter',sans-serif;text-align:center;z-index:2}
#load .sp{width:26px;height:26px;border:3px solid #1e1e2e;border-top:3px solid #8b5cf6;
          border-radius:50%;animation:s .8s linear infinite;margin:0 auto 8px}
@keyframes s{to{transform:rotate(360deg)}}
#ctrl{background:#12121a;padding:10px 12px;display:flex;align-items:center;gap:10px;
      border-top:1px solid #1e1e2e}
#pb{background:linear-gradient(135deg,#8b5cf6,#7c3aed);border:none;color:#fff;
    width:34px;height:34px;border-radius:7px;cursor:pointer;font-size:14px;
    display:flex;align-items:center;justify-content:center;flex-shrink:0}
#ci{flex:1;min-width:0}
#ct{display:flex;justify-content:space-between;margin-bottom:4px}
#sn{color:#e4e4e7;font:500 11px 'Inter',sans-serif;white-space:nowrap;overflow:hidden;text-overflow:ellipsis}
#vp{color:#8b5cf6;font:600 11px 'Fira Code',monospace;flex-shrink:0;margin-left:6px}
#vt{width:100%;height:4px;background:#1e1e2e;border-radius:99px;overflow:hidden}
#vf{height:100%;width:0%;border-radius:99px;background:#8b5cf6;transition:width .15s}
#sl{text-align:center;padding:5px;color:#52525b;font:500 9px 'Fira Code',monospace;
    background:#12121a;border-radius:0 0 10px 10px}
</style>

<div>
  <div id="wrap">
    <video id="cam" playsinline style="display:none"></video>
    <canvas id="out"></canvas>
    <div id="load"><div class="sp"></div>Loading hand tracking...</div>
  </div>
  <div id="ctrl">
    <button id="pb" onclick="tgl()">&#9654;</button>
    <div id="ci">
      <div id="ct"><span id="sn">SoundHelix Song 1</span><span id="vp">0%</span></div>
      <div id="vt"><div id="vf"></div></div>
    </div>
  </div>
  <div id="sl">Show your hand to control volume</div>
</div>

<audio id="au" loop preload="auto"
  src="https://www.soundhelix.com/examples/mp3/SoundHelix-Song-1.mp3"></audio>

<script src="https://cdn.jsdelivr.net/npm/@mediapipe/hands/hands.js" crossorigin="anonymous"></script>
<script src="https://cdn.jsdelivr.net/npm/@mediapipe/camera_utils/camera_utils.js" crossorigin="anonymous"></script>

<script>
const vid=document.getElementById('cam'),
      can=document.getElementById('out'),
      ctx=can.getContext('2d'),
      au=document.getElementById('au'),
      pb=document.getElementById('pb'),
      vp=document.getElementById('vp'),
      vf=document.getElementById('vf'),
      sl=document.getElementById('sl'),
      ld=document.getElementById('load');

const CN=[[0,1],[1,2],[2,3],[3,4],[0,5],[5,6],[6,7],[7,8],
          [0,9],[9,10],[10,11],[11,12],[0,13],[13,14],[14,15],[15,16],
          [0,17],[17,18],[18,19],[19,20],[5,9],[9,13],[13,17]];

let vol=0,playing=false,det=false,fc=0;
const mob=/Android|iPhone|iPad|iPod/i.test(navigator.userAgent);

function tgl(){
  if(!playing){
    au.play().then(()=>{
      playing=true;pb.innerHTML='&#9646;&#9646;';
      sl.textContent='Playing — gesture controls active';
      sl.style.color='#22c55e';
    }).catch(()=>{
      sl.textContent='Tap again (browser blocked autoplay)';
      sl.style.color='#f59e0b';
    });
  }else{
    au.pause();playing=false;pb.innerHTML='&#9654;';
    sl.textContent='Paused';sl.style.color='#52525b';
  }
}

function vc(v){return v<30?'#3c8ce7':v<65?'#22c55e':'#8b5cf6'}

function onR(r){
  fc++;
  // On mobile, skip every other frame for performance
  if(mob && fc%2===0){return}

  const w=can.width,h=can.height;
  ctx.save();ctx.clearRect(0,0,w,h);
  ctx.translate(w,0);ctx.scale(-1,1);
  ctx.drawImage(r.image,0,0,w,h);
  ctx.restore();

  det=r.multiHandLandmarks&&r.multiHandLandmarks.length>0;

  if(det){
    const lm=r.multiHandLandmarks[0];
    const p=lm.map(l=>({x:(1-l.x)*w,y:l.y*h}));

    // skeleton
    ctx.strokeStyle='#8b5cf6';ctx.lineWidth=mob?1.5:2;
    for(const[a,b]of CN){ctx.beginPath();ctx.moveTo(p[a].x,p[a].y);ctx.lineTo(p[b].x,p[b].y);ctx.stroke()}

    // joints
    for(let i=0;i<p.length;i++){
      ctx.beginPath();
      if(i===4||i===8){
        ctx.arc(p[i].x,p[i].y,mob?6:8,0,Math.PI*2);ctx.fillStyle='#dcd6ff';ctx.fill();
        ctx.strokeStyle='#8b5cf6';ctx.lineWidth=1.5;ctx.stroke();
      }else{
        ctx.arc(p[i].x,p[i].y,mob?2:3,0,Math.PI*2);ctx.fillStyle='#b4b4bc';ctx.fill();
      }
    }

    // volume calc
    const t=p[4],ix=p[8];
    const d=Math.sqrt((t.x-ix.x)**2+(t.y-ix.y)**2);
    const minD=mob?15:20, maxD=mob?100:140;
    const raw=Math.max(0,Math.min(100,(d-minD)*100/(maxD-minD)));
    vol=vol*0.5+raw*0.5;
    const c=vc(vol);

    // connector
    ctx.beginPath();ctx.moveTo(t.x,t.y);ctx.lineTo(ix.x,ix.y);
    ctx.strokeStyle=c;ctx.lineWidth=2;ctx.stroke();

    // midpoint orb
    const mx=(t.x+ix.x)/2,my=(t.y+ix.y)/2,mr=4+vol*0.10;
    ctx.beginPath();ctx.arc(mx,my,mr,0,Math.PI*2);ctx.fillStyle=c;ctx.fill();
    ctx.strokeStyle='#fff';ctx.lineWidth=1;ctx.stroke();

    // vol % text
    const vi=Math.round(vol);
    ctx.font=mob?'600 11px monospace':'600 13px "Fira Code",monospace';
    ctx.fillStyle='#fff';ctx.textAlign='center';
    ctx.fillText(vi+'%',mx,my-mr-5);

    au.volume=Math.max(0,Math.min(1,vol/100));
  }

  // arc meter bottom-right
  const vi=Math.round(vol),arcR=mob?24:32;
  const cx=w-(mob?38:50),cy=h-(mob?38:50);
  const sa=135*Math.PI/180,sw=270*Math.PI/180,ea=sa+sw*vol/100;
  ctx.beginPath();ctx.arc(cx,cy,arcR,sa,sa+sw);ctx.strokeStyle='#19191f';ctx.lineWidth=2;ctx.stroke();
  if(vol>0){ctx.beginPath();ctx.arc(cx,cy,arcR,sa,ea);ctx.strokeStyle=vc(vol);ctx.lineWidth=2.5;ctx.stroke()}
  ctx.font=mob?'500 11px monospace':'500 13px "Fira Code",monospace';
  ctx.fillStyle='#e4e4e7';ctx.textAlign='center';ctx.fillText(vi+'%',cx,cy+3);
  ctx.font=mob?'500 7px monospace':'500 8px "Fira Code",monospace';
  ctx.fillStyle='#5a5a6e';ctx.fillText('VOL',cx,cy+13);

  // status top-left
  ctx.fillStyle='rgba(0,0,0,0.55)';ctx.fillRect(0,0,mob?120:150,mob?22:26);
  ctx.beginPath();ctx.arc(mob?10:13,mob?11:13,3.5,0,Math.PI*2);
  ctx.fillStyle=det?'#22c55e':'#505064';ctx.fill();
  ctx.font=mob?'500 9px monospace':'500 10px "Fira Code",monospace';
  ctx.textAlign='left';ctx.fillText(det?'TRACKING':'SHOW HAND',mob?20:25,mob?14:17);

  // branding top-right
  const bw=mob?105:130;
  ctx.fillStyle='rgba(0,0,0,0.45)';ctx.fillRect(w-bw,0,bw,mob?20:22);
  ctx.font=mob?'500 9px monospace':'500 10px "Fira Code",monospace';
  ctx.fillStyle='#8b5cf6';ctx.textAlign='right';ctx.fillText('AARAV SHUKLA',w-5,mob?13:15);

  // update UI bar
  const cl=Math.round(Math.max(0,Math.min(100,vol)));
  vp.textContent=cl+'%';vf.style.width=cl+'%';vf.style.background=vc(vol);
}

// init MediaPipe
const hands=new Hands({locateFile:f=>`https://cdn.jsdelivr.net/npm/@mediapipe/hands/${f}`});
hands.setOptions({maxNumHands:1,modelComplexity:0,minDetectionConfidence:0.5,minTrackingConfidence:0.5});
hands.onResults(onR);

// camera — lower res on mobile for speed
const cw=mob?480:1280, ch=mob?360:720;

const camera=new Camera(vid,{
  onFrame:async()=>{await hands.send({image:vid})},
  width:cw,height:ch,facingMode:'user'
});

camera.start().then(()=>{
  can.width=cw;can.height=ch;ld.style.display='none';
}).catch(()=>{
  ld.innerHTML='Camera access denied.<br>Allow camera and reload.';
  ld.style.color='#f59e0b';
});
</script>
"""

components.html(COMPONENT, height=480)

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
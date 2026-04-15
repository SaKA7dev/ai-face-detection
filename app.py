"""
AI Hand Gesture Volume Controller
Aarav Shukla — Class 9 | ThinkSkool Project
"""

import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(
    page_title="Gesture Volume · Aarav Shukla",
    page_icon="🤚",
    layout="centered",
)

st.markdown("""<style>
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&family=Fira+Code:wght@400;500;600&display=swap');

:root{--bg:#0a0a0f;--card:#12121a;--border:#1e1e2e;--text:#e4e4e7;--muted:#52525b;--sub:#71717a;--accent:#8b5cf6}

.stApp{background:var(--bg)!important;font-family:'Inter',sans-serif!important;color:var(--text)}
header[data-testid="stHeader"]{background:transparent!important}
#MainMenu,footer{visibility:hidden!important}
.block-container{padding-top:1rem!important;max-width:720px!important}

.desk-warn{background:linear-gradient(135deg, #7c3aed, #6d28d9);border:none;border-radius:8px;
  padding:16px 20px;margin:10px 0 24px;text-align:center;box-shadow:0 4px 12px rgba(124,58,237,0.3)}
.desk-warn p{margin:0;color:#fff;font-size:0.95rem;font-weight:600;line-height:1.4;letter-spacing:0.02em}
.desk-warn strong{color:#fff;background:rgba(0,0,0,0.25);padding:2px 8px;border-radius:4px;margin:0 2px}

.app-header{text-align:center;padding:0.2rem 0 0.8rem}
.app-title{font-size:1.9rem;font-weight:700;color:var(--text);letter-spacing:-0.02em;margin:0 0 0.4rem}
.app-title span{color:var(--accent)}
.app-author{font-size:1rem;font-weight:600;color:var(--text);margin:0 0 0.4rem}
.app-author span{color:var(--accent);font-weight:700}
.app-desc{color:var(--sub);font-size:0.8rem;line-height:1.5;margin:0 auto;max-width:460px}

.info-grid{display:grid;grid-template-columns:repeat(4,1fr);gap:6px;margin:0.6rem 0}
.info-item{background:var(--card);border:1px solid var(--border);border-radius:8px;padding:7px 4px;text-align:center}
.info-val{color:var(--text);font-size:0.95rem;font-weight:700;font-family:'Fira Code',monospace}
.info-label{color:var(--muted);font-size:0.52rem;font-weight:500;letter-spacing:0.06em;text-transform:uppercase;margin-top:2px}

.section-card{background:var(--card);border:1px solid var(--border);border-radius:10px;padding:10px 13px;margin:6px 0}
.section-header{display:flex;align-items:center;gap:6px;margin-bottom:5px}
.section-dot{width:6px;height:6px;border-radius:50%;background:var(--accent)}
.section-title{color:var(--muted);font-size:0.6rem;font-weight:600;letter-spacing:0.08em;text-transform:uppercase;font-family:'Fira Code',monospace}

.steps-list{list-style:none;padding:0;margin:0}
.step-item{display:flex;align-items:center;gap:8px;padding:4px 0}
.step-num{flex-shrink:0;width:18px;height:18px;border-radius:4px;background:rgba(139,92,246,0.1);
  border:1px solid rgba(139,92,246,0.15);color:var(--accent);font-size:0.5rem;font-weight:600;
  font-family:'Fira Code',monospace;display:flex;align-items:center;justify-content:center}
.step-text{color:var(--sub);font-size:0.72rem;line-height:1.3}
.step-text strong{color:var(--text);font-weight:600}

.app-footer{text-align:center;padding:1.2rem 0;border-top:1px solid var(--border);margin-top:1rem}
.footer-name{color:var(--text);font-weight:700;font-size:1rem}
.footer-sub{color:var(--muted);font-size:0.7rem;margin-top:4px}
.footer-tech{display:flex;justify-content:center;gap:6px;margin-top:8px;flex-wrap:wrap}
.tech-pill{padding:3px 10px;border-radius:100px;background:var(--card);border:1px solid var(--border);
  color:var(--muted);font-size:0.6rem;font-family:'Fira Code',monospace;font-weight:500}

.stApp iframe{border-radius:10px!important}
</style>""", unsafe_allow_html=True)

# ── Desktop Warning ───────────────────────────────────────────────────────────
st.markdown("""
<div class="desk-warn">
    <p>💻 FOR THE BEST EXPERIENCE, PLEASE OPEN THIS PROJECT ON A <strong>LAPTOP OR DESKTOP</strong></p>
</div>
""", unsafe_allow_html=True)

# ── Header ────────────────────────────────────────────────────────────────────
st.markdown("""
<div class="app-header">
    <h1 class="app-title">Gesture <span>Volume</span> Control</h1>
    <p class="app-author">Built by <span>Aarav Shukla</span> · Class 9</p>
    <p class="app-desc">
        Control audio volume with hand gestures — pinch to lower, spread to raise.
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

# ── Steps ─────────────────────────────────────────────────────────────────────
st.markdown("""
<div class="section-card">
    <div class="section-header">
        <div class="section-dot"></div>
        <span class="section-title">How to Use</span>
    </div>
    <ul class="steps-list">
        <li class="step-item"><div class="step-num">1</div><div class="step-text">Allow <strong>camera</strong> access</div></li>
        <li class="step-item"><div class="step-num">2</div><div class="step-text">Show your <strong>hand</strong> to the camera</div></li>
        <li class="step-item"><div class="step-num">3</div><div class="step-text"><strong>Pinch</strong> thumb + index → volume down · <strong>Spread</strong> → volume up</div></li>
        <li class="step-item"><div class="step-num">4</div><div class="step-text">Press <strong>▶</strong> to play audio and hear the volume change</div></li>
    </ul>
</div>
""", unsafe_allow_html=True)

# ── Client-side Camera + Hand Detection + Audio ──────────────────────────────
COMPONENT = """
<style>
*{margin:0;padding:0;box-sizing:border-box}
body{background:transparent;overflow:hidden}
#wrap{width:100%;background:#000;position:relative;border-radius:10px 10px 0 0;overflow:hidden}
#out{width:100%;display:block}
#load{position:absolute;top:50%;left:50%;transform:translate(-50%,-50%);
  color:#71717a;font:500 13px 'Inter',sans-serif;text-align:center;z-index:2}
#load .sp{width:24px;height:24px;border:3px solid #1e1e2e;border-top:3px solid #8b5cf6;
  border-radius:50%;animation:s .7s linear infinite;margin:0 auto 8px}
@keyframes s{to{transform:rotate(360deg)}}
#ctrl{background:#12121a;padding:10px 12px;display:flex;align-items:center;gap:10px;border-top:1px solid #1e1e2e}
#pb{background:linear-gradient(135deg,#8b5cf6,#7c3aed);border:none;color:#fff;
  width:34px;height:34px;border-radius:7px;cursor:pointer;font-size:14px;
  display:flex;align-items:center;justify-content:center;flex-shrink:0}
#ci{flex:1;min-width:0}
#ct{display:flex;justify-content:space-between;margin-bottom:4px}
#sn{color:#e4e4e7;font:500 11px 'Inter',sans-serif}
#vp{color:#8b5cf6;font:600 11px 'Fira Code',monospace;flex-shrink:0}
#vt{width:100%;height:4px;background:#1e1e2e;border-radius:99px;overflow:hidden}
#vf{height:100%;width:0%;border-radius:99px;background:#8b5cf6;transition:width .12s}
#sl{text-align:center;padding:5px;color:#52525b;font:500 9px 'Fira Code',monospace;
  background:#12121a;border-radius:0 0 10px 10px}
</style>

<div>
  <div id="wrap">
    <video id="cam" playsinline style="display:none"></video>
    <canvas id="out"></canvas>
    <div id="load"><div class="sp"></div>Loading hand tracking model...</div>
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

let vol=0,playing=false,det=false;

function tgl(){
  if(!playing){
    au.play().then(()=>{
      playing=true;pb.innerHTML='&#9646;&#9646;';
      sl.textContent='Playing — gesture controls active';sl.style.color='#22c55e';
    }).catch(()=>{
      sl.textContent='Tap again (browser blocked autoplay)';sl.style.color='#f59e0b';
    });
  }else{
    au.pause();playing=false;pb.innerHTML='&#9654;';
    sl.textContent='Paused';sl.style.color='#52525b';
  }
}

function vc(v){return v<30?'#3c8ce7':v<65?'#22c55e':'#8b5cf6'}

function onR(r){
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
    ctx.strokeStyle='#8b5cf6';ctx.lineWidth=2;
    for(const[a,b]of CN){ctx.beginPath();ctx.moveTo(p[a].x,p[a].y);ctx.lineTo(p[b].x,p[b].y);ctx.stroke()}

    // joints
    for(let i=0;i<p.length;i++){
      ctx.beginPath();
      if(i===4||i===8){
        ctx.arc(p[i].x,p[i].y,8,0,Math.PI*2);ctx.fillStyle='#dcd6ff';ctx.fill();
        ctx.strokeStyle='#8b5cf6';ctx.lineWidth=1.5;ctx.stroke();
      }else{
        ctx.arc(p[i].x,p[i].y,3,0,Math.PI*2);ctx.fillStyle='#b4b4bc';ctx.fill();
      }
    }

    // volume from thumb-index distance
    // calibrated: pinch (~30px) = 0%, full spread (~280px) = 100%
    const t=p[4],ix=p[8];
    const d=Math.sqrt((t.x-ix.x)**2+(t.y-ix.y)**2);
    const raw=Math.max(0,Math.min(100,(d-30)*100/250));
    vol=vol*0.3+raw*0.7;  // fast response
    const c=vc(vol);

    // connector line
    ctx.beginPath();ctx.moveTo(t.x,t.y);ctx.lineTo(ix.x,ix.y);
    ctx.strokeStyle=c;ctx.lineWidth=2;ctx.stroke();

    // midpoint orb
    const mx=(t.x+ix.x)/2,my=(t.y+ix.y)/2,mr=4+vol*0.11;
    ctx.beginPath();ctx.arc(mx,my,mr,0,Math.PI*2);ctx.fillStyle=c;ctx.fill();
    ctx.strokeStyle='#fff';ctx.lineWidth=1;ctx.stroke();

    // vol % near midpoint
    const vi=Math.round(vol);
    ctx.font='600 13px "Fira Code",monospace';ctx.fillStyle='#fff';
    ctx.textAlign='center';ctx.fillText(vi+'%',mx,my-mr-5);

    au.volume=Math.max(0,Math.min(1,vol/100));
  }

  // arc meter bottom-right
  const vi=Math.round(vol),cx=w-50,cy=h-50,rd=32;
  const sa=135*Math.PI/180,sw=270*Math.PI/180,ea=sa+sw*vol/100;
  ctx.beginPath();ctx.arc(cx,cy,rd,sa,sa+sw);ctx.strokeStyle='#19191f';ctx.lineWidth=2;ctx.stroke();
  if(vol>0){ctx.beginPath();ctx.arc(cx,cy,rd,sa,ea);ctx.strokeStyle=vc(vol);ctx.lineWidth=2.5;ctx.stroke()}
  ctx.font='500 13px "Fira Code",monospace';ctx.fillStyle='#e4e4e7';ctx.textAlign='center';ctx.fillText(vi+'%',cx,cy+3);
  ctx.font='500 8px "Fira Code",monospace';ctx.fillStyle='#5a5a6e';ctx.fillText('VOL',cx,cy+14);

  // status top-left
  ctx.fillStyle='rgba(0,0,0,0.55)';ctx.fillRect(0,0,150,26);
  ctx.beginPath();ctx.arc(13,13,3.5,0,Math.PI*2);
  ctx.fillStyle=det?'#22c55e':'#505064';ctx.fill();
  ctx.font='500 10px "Fira Code",monospace';ctx.textAlign='left';
  ctx.fillText(det?'TRACKING':'SHOW HAND',25,17);

  // branding top-right
  ctx.fillStyle='rgba(0,0,0,0.45)';ctx.fillRect(w-130,0,130,22);
  ctx.font='500 10px "Fira Code",monospace';ctx.fillStyle='#8b5cf6';
  ctx.textAlign='right';ctx.fillText('AARAV SHUKLA',w-6,15);

  // update UI bar
  const cl=Math.round(Math.max(0,Math.min(100,vol)));
  vp.textContent=cl+'%';vf.style.width=cl+'%';vf.style.background=vc(vol);
}

const hands=new Hands({locateFile:f=>`https://cdn.jsdelivr.net/npm/@mediapipe/hands/${f}`});
hands.setOptions({maxNumHands:1,modelComplexity:1,minDetectionConfidence:0.6,minTrackingConfidence:0.6});
hands.onResults(onR);

const camera=new Camera(vid,{
  onFrame:async()=>{await hands.send({image:vid})},
  width:1280,height:720,facingMode:'user'
});

camera.start().then(()=>{
  can.width=1280;can.height=720;ld.style.display='none';
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
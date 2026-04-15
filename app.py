"""
AI Hand Gesture Volume Controller
Built by Aarav Shukla — Class 9th
"""

import cv2
import numpy as np
import math
import os
import threading
import urllib.request
import time

import streamlit as st
import streamlit.components.v1 as components
from streamlit_webrtc import webrtc_streamer
import av
import mediapipe as mp
from mediapipe.tasks import python as mp_python
from mediapipe.tasks.python import vision

# ── Page Config ───────────────────────────────────────────────────────────────
st.set_page_config(
    page_title="Gesture Volume · Aarav Shukla",
    page_icon="🤚",
    layout="centered",
)

# ── CSS ───────────────────────────────────────────────────────────────────────
st.markdown("""<style>
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800&family=Fira+Code:wght@400;500&display=swap');

:root {
    --bg-primary: #0a0a0f;
    --bg-card: #12121a;
    --bg-card-hover: #161620;
    --border: #1e1e2e;
    --border-accent: #2a2a3e;
    --text-primary: #e4e4e7;
    --text-secondary: #71717a;
    --text-muted: #52525b;
    --accent: #8b5cf6;
    --accent-soft: rgba(139, 92, 246, 0.12);
    --accent-glow: rgba(139, 92, 246, 0.25);
    --green: #22c55e;
    --amber: #f59e0b;
}

*, *::before, *::after { box-sizing: border-box; }

.stApp {
    background: var(--bg-primary) !important;
    font-family: 'Inter', -apple-system, BlinkMacSystemFont, sans-serif !important;
    color: var(--text-primary);
}

header[data-testid="stHeader"] { background: transparent !important; }
#MainMenu, footer { visibility: hidden !important; }

.block-container { padding-top: 2rem !important; max-width: 720px !important; }

/* ── Hero Section ── */
.app-header {
    text-align: center;
    padding: 2rem 0 1.5rem;
    position: relative;
}

.app-header::before {
    content: '';
    position: absolute;
    top: -60px; left: 50%; transform: translateX(-50%);
    width: 400px; height: 200px;
    background: radial-gradient(ellipse, var(--accent-glow) 0%, transparent 70%);
    pointer-events: none;
    opacity: 0.4;
}

.app-badge {
    display: inline-flex; align-items: center; gap: 6px;
    padding: 5px 12px; border-radius: 100px;
    background: var(--accent-soft);
    border: 1px solid rgba(139, 92, 246, 0.2);
    color: var(--accent); font-size: 0.7rem; font-weight: 500;
    font-family: 'Fira Code', monospace;
    letter-spacing: 0.04em;
    margin-bottom: 1rem;
}

.app-badge::before {
    content: '';
    width: 6px; height: 6px; border-radius: 50%;
    background: var(--accent);
    animation: pulse-dot 2s ease-in-out infinite;
}

@keyframes pulse-dot {
    0%, 100% { opacity: 1; transform: scale(1); }
    50% { opacity: 0.5; transform: scale(0.8); }
}

.app-title {
    font-size: 2.4rem; font-weight: 800; color: var(--text-primary);
    letter-spacing: -0.04em; line-height: 1.15; margin: 0 0 0.5rem;
}

.app-title-accent {
    background: linear-gradient(135deg, #8b5cf6, #a78bfa, #c4b5fd);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    background-clip: text;
}

.app-desc {
    color: var(--text-secondary); font-size: 0.88rem;
    line-height: 1.6; margin: 0; max-width: 480px;
    margin-left: auto; margin-right: auto;
}

/* ── Info Grid ── */
.info-grid {
    display: grid;
    grid-template-columns: repeat(4, 1fr);
    gap: 8px; margin: 1.2rem 0;
}

.info-item {
    background: var(--bg-card);
    border: 1px solid var(--border);
    border-radius: 10px;
    padding: 12px 8px;
    text-align: center;
    transition: border-color 0.2s;
}

.info-item:hover { border-color: var(--border-accent); }

.info-val {
    color: var(--text-primary); font-size: 1.15rem; font-weight: 700;
    font-family: 'Fira Code', monospace;
    line-height: 1;
}

.info-label {
    color: var(--text-muted); font-size: 0.6rem;
    font-weight: 500; letter-spacing: 0.06em;
    text-transform: uppercase; margin-top: 4px;
}

/* ── Cards ── */
.section-card {
    background: var(--bg-card);
    border: 1px solid var(--border);
    border-radius: 12px;
    padding: 16px 18px;
    margin: 10px 0;
}

.section-header {
    display: flex; align-items: center; gap: 8px;
    margin-bottom: 10px;
}

.section-dot {
    width: 7px; height: 7px; border-radius: 50%;
    background: var(--accent);
    box-shadow: 0 0 8px var(--accent-glow);
}

.section-dot.green { background: var(--green); box-shadow: 0 0 8px rgba(34, 197, 94, 0.3); }

.section-title {
    color: var(--text-muted); font-size: 0.68rem; font-weight: 600;
    letter-spacing: 0.08em; text-transform: uppercase;
    font-family: 'Fira Code', monospace;
}

/* ── Steps ── */
.steps-list { list-style: none; padding: 0; margin: 0; }

.step-item {
    display: flex; align-items: flex-start; gap: 12px;
    padding: 8px 0;
    border-bottom: 1px solid rgba(30, 30, 46, 0.5);
}

.step-item:last-child { border-bottom: none; padding-bottom: 0; }

.step-num {
    flex-shrink: 0;
    width: 24px; height: 24px;
    border-radius: 6px;
    background: var(--accent-soft);
    border: 1px solid rgba(139, 92, 246, 0.15);
    color: var(--accent);
    font-size: 0.65rem; font-weight: 600;
    font-family: 'Fira Code', monospace;
    display: flex; align-items: center; justify-content: center;
}

.step-text {
    color: var(--text-secondary); font-size: 0.82rem;
    line-height: 1.5; padding-top: 2px;
}

.step-text strong { color: var(--text-primary); font-weight: 600; }

/* ── Footer ── */
.app-footer {
    text-align: center; padding: 2rem 0 1.2rem;
    border-top: 1px solid var(--border);
    margin-top: 1.5rem;
}

.footer-name {
    color: var(--text-primary); font-weight: 600;
    font-size: 0.85rem;
}

.footer-sub {
    color: var(--text-muted); font-size: 0.72rem;
    margin-top: 4px; letter-spacing: 0.02em;
}

.footer-tech {
    display: flex; justify-content: center; gap: 8px;
    margin-top: 10px; flex-wrap: wrap;
}

.tech-pill {
    padding: 3px 10px; border-radius: 100px;
    background: var(--bg-card);
    border: 1px solid var(--border);
    color: var(--text-muted); font-size: 0.62rem;
    font-family: 'Fira Code', monospace;
    font-weight: 500; letter-spacing: 0.03em;
}

/* ── WebRTC overrides ── */
.stApp iframe { border-radius: 10px !important; }

/* ── Hide the volume data element ── */
#gesture-vol-data { display: none !important; }
</style>""", unsafe_allow_html=True)

# ── Model ─────────────────────────────────────────────────────────────────────
MODEL_URL = ("https://storage.googleapis.com/mediapipe-models/"
             "hand_landmarker/hand_landmarker/float16/latest/hand_landmarker.task")
MODEL_PATH = os.path.join(os.path.dirname(os.path.abspath(__file__)), "hand_landmarker.task")


@st.cache_resource
def load_detector():
    if not os.path.exists(MODEL_PATH):
        urllib.request.urlretrieve(MODEL_URL, MODEL_PATH)
    opts = vision.HandLandmarkerOptions(
        base_options=mp_python.BaseOptions(model_asset_path=MODEL_PATH),
        num_hands=1,
        min_hand_detection_confidence=0.5,
        min_hand_presence_confidence=0.5,
        min_tracking_confidence=0.5,
    )
    return vision.HandLandmarker.create_from_options(opts)


detector = load_detector()
lock = threading.Lock()

# ── Drawing constants ─────────────────────────────────────────────────────────
CONNS = [
    (0,1),(1,2),(2,3),(3,4),(0,5),(5,6),(6,7),(7,8),
    (0,9),(9,10),(10,11),(11,12),(0,13),(13,14),(14,15),(15,16),
    (0,17),(17,18),(18,19),(19,20),(5,9),(9,13),(13,17),
]

@st.cache_resource
def _get_shared_state():
    return {"vol": 0.0, "fc": 0}

state = _get_shared_state()


def _vol_color(v):
    """Return BGR color based on volume level."""
    if v < 30:
        return (180, 140, 60)
    elif v < 65:
        return (94, 197, 34)
    else:
        return (92, 92, 246)


# ── Frame processor ───────────────────────────────────────────────────────────
def process_frame(frame):
    img = frame.to_ndarray(format="bgr24")
    img = cv2.flip(img, 1)
    h, w, _ = img.shape
    fc = state["fc"] = state["fc"] + 1

    rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    mp_img = mp.Image(image_format=mp.ImageFormat.SRGB, data=rgb)

    with lock:
        res = detector.detect(mp_img)

    vol = state["vol"]
    detected = bool(res.hand_landmarks)

    if detected:
        lms = res.hand_landmarks[0]
        pts = [(int(l.x * w), int(l.y * h)) for l in lms]

        # ── Skeleton ──
        for a, b in CONNS:
            overlay = img.copy()
            cv2.line(overlay, pts[a], pts[b], (139, 92, 246), 6, cv2.LINE_AA)
            cv2.addWeighted(overlay, 0.12, img, 0.88, 0, img)
            cv2.line(img, pts[a], pts[b], (139, 92, 246), 2, cv2.LINE_AA)

        # ── Joints ──
        pulse = int(2 * math.sin(fc * 0.18))
        for i, pt in enumerate(pts):
            if i in (4, 8):
                r = 10 + pulse
                overlay = img.copy()
                cv2.circle(overlay, pt, r + 6, (139, 92, 246), -1, cv2.LINE_AA)
                cv2.addWeighted(overlay, 0.2, img, 0.8, 0, img)
                cv2.circle(img, pt, r, (220, 210, 255), -1, cv2.LINE_AA)
                cv2.circle(img, pt, r + 1, (139, 92, 246), 2, cv2.LINE_AA)
            else:
                cv2.circle(img, pt, 3, (180, 180, 200), -1, cv2.LINE_AA)

        # ── Volume from thumb-index distance ──
        thumb, idx = pts[4], pts[8]
        dist = math.hypot(idx[0] - thumb[0], idx[1] - thumb[1])
        raw = float(np.clip(np.interp(dist, [25, 160], [0, 100]), 0, 100))
        state["vol"] = 0.55 * state["vol"] + 0.45 * raw
        vol = state["vol"]
        vc = _vol_color(vol)

        # ── Connector line with glow ──
        overlay = img.copy()
        cv2.line(overlay, thumb, idx, vc, 8, cv2.LINE_AA)
        cv2.addWeighted(overlay, 0.15, img, 0.85, 0, img)
        cv2.line(img, thumb, idx, vc, 2, cv2.LINE_AA)

        # ── Midpoint orb ──
        mid = ((thumb[0] + idx[0]) // 2, (thumb[1] + idx[1]) // 2)
        mr = int(np.interp(vol, [0, 100], [5, 20]))
        pr = mr + int(2 * math.sin(fc * 0.2))
        overlay = img.copy()
        cv2.circle(overlay, mid, pr + 8, vc, -1, cv2.LINE_AA)
        cv2.addWeighted(overlay, 0.12, img, 0.88, 0, img)
        cv2.circle(img, mid, pr, vc, -1, cv2.LINE_AA)
        cv2.circle(img, mid, pr, (255, 255, 255), 1, cv2.LINE_AA)

        # ── Volume percentage near midpoint ──
        vi = int(vol)
        label_pos = (mid[0] - 15, mid[1] - pr - 12)
        cv2.putText(img, f"{vi}%", label_pos,
                    cv2.FONT_HERSHEY_SIMPLEX, 0.55, (255, 255, 255), 2, cv2.LINE_AA)
        cv2.putText(img, f"{vi}%", label_pos,
                    cv2.FONT_HERSHEY_SIMPLEX, 0.55, vc, 1, cv2.LINE_AA)

    # ── Arc meter (bottom-right) ──
    vi = int(vol)
    cx, cy, rad = w - 70, h - 80, 44
    vc = _vol_color(vol)
    start_angle, sweep = 135, 270

    cv2.ellipse(img, (cx, cy), (rad, rad), 0, start_angle, start_angle + sweep,
                (25, 25, 35), 3, cv2.LINE_AA)
    end_angle = start_angle + sweep * vol / 100
    overlay = img.copy()
    cv2.ellipse(overlay, (cx, cy), (rad, rad), 0, start_angle, end_angle, vc, 7, cv2.LINE_AA)
    cv2.addWeighted(overlay, 0.2, img, 0.8, 0, img)
    cv2.ellipse(img, (cx, cy), (rad, rad), 0, start_angle, end_angle, vc, 3, cv2.LINE_AA)

    tip_a = math.radians(end_angle)
    tx = int(cx + rad * math.cos(tip_a))
    ty = int(cy + rad * math.sin(tip_a))
    tp = int(3 + 1.5 * math.sin(fc * 0.12))
    cv2.circle(img, (tx, ty), tp, (255, 255, 255), -1, cv2.LINE_AA)

    cv2.putText(img, f"{vi}%", (cx - 20, cy + 6),
                cv2.FONT_HERSHEY_SIMPLEX, 0.6, (230, 230, 235), 2, cv2.LINE_AA)
    cv2.putText(img, "VOL", (cx - 14, cy + 22),
                cv2.FONT_HERSHEY_SIMPLEX, 0.32, (90, 90, 110), 1, cv2.LINE_AA)

    # ── Status indicator (top-left) ──
    overlay = img.copy()
    cv2.rectangle(overlay, (0, 0), (210, 36), (0, 0, 0), -1)
    cv2.addWeighted(overlay, 0.5, img, 0.5, 0, img)

    if detected:
        status_text = "TRACKING"
        dot_color = (94, 197, 34)
    else:
        status_text = "SHOW HAND"
        dot_color = (80, 80, 100)

    dot_r = 4 + int(1.5 * math.sin(fc * 0.15)) if detected else 4
    cv2.circle(img, (16, 18), dot_r, dot_color, -1, cv2.LINE_AA)
    cv2.putText(img, status_text, (28, 24),
                cv2.FONT_HERSHEY_SIMPLEX, 0.45, dot_color, 1, cv2.LINE_AA)

    # ── Branding (top-right) ──
    overlay2 = img.copy()
    cv2.rectangle(overlay2, (w - 175, 0), (w, 30), (0, 0, 0), -1)
    cv2.addWeighted(overlay2, 0.45, img, 0.55, 0, img)
    cv2.putText(img, "AARAV SHUKLA", (w - 165, 20),
                cv2.FONT_HERSHEY_SIMPLEX, 0.42, (139, 92, 246), 1, cv2.LINE_AA)

    # ── Encode volume as bar width for JS bridge ──────────────────────────
    # Bottom 3px strip: white bar whose width = vol/100 * frame_width
    # JS reads the bright→dark transition to decode volume percentage
    # This survives H.264 compression perfectly (spatial, not color-based)
    bar_w = int(np.clip(vol, 0, 100) * w / 100)
    img[h-3:h, :] = [10, 10, 15]          # dark background strip
    if bar_w > 0:
        img[h-3:h, 0:bar_w] = [255, 255, 255]  # white bar = volume

    return av.VideoFrame.from_ndarray(img, format="bgr24")


# ══════════════════════════════════════════════════════════════════════════════
#  UI LAYOUT
# ══════════════════════════════════════════════════════════════════════════════

st.markdown("""
<div class="app-header">
    <div class="app-badge">COMPUTER VISION PROJECT</div>
    <h1 class="app-title">Gesture <span class="app-title-accent">Volume</span> Control</h1>
    <p class="app-desc">
        Real-time hand tracking that maps your finger distance
        to a volume level — powered by MediaPipe's 21-point
        hand landmark model.
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

st.markdown("""
<div class="section-card">
    <div class="section-header">
        <div class="section-dot green"></div>
        <span class="section-title">Live Camera Feed</span>
    </div>
</div>
""", unsafe_allow_html=True)

webrtc_streamer(
    key="vol-ctrl",
    video_frame_callback=process_frame,
    rtc_configuration={"iceServers": [{"urls": ["stun:stun.l.google.com:19302"]}]},
    media_stream_constraints={
        "video": {"width": {"ideal": 1280}, "height": {"ideal": 720}},
        "audio": False,
    },
)

# ── Expose current volume to the browser via a hidden element ─────────────────
vol_now = int(state["vol"])
st.markdown(
    f'<div id="gesture-vol-data" data-vol="{vol_now}"></div>',
    unsafe_allow_html=True,
)

# ── Audio player with gesture-controlled volume (self-contained component) ────
AUDIO_HTML = """
<div id="gesture-audio-root" style="
    background:#12121a; border-radius:12px; padding:18px 18px 14px;
    border:1px solid #1e1e2e; font-family:'Inter',sans-serif;">

    <div style="display:flex;align-items:center;gap:8px;margin-bottom:12px;">
        <div style="width:7px;height:7px;border-radius:50%;background:#8b5cf6;
                    box-shadow:0 0 8px rgba(139,92,246,0.25);"></div>
        <span style="color:#52525b;font-size:0.68rem;font-weight:600;
                     letter-spacing:0.08em;text-transform:uppercase;
                     font-family:'Fira Code',monospace;">GESTURE AUDIO CONTROL</span>
    </div>

    <!-- Play / Pause button -->
    <div style="display:flex;align-items:center;gap:14px;margin-bottom:14px;">
        <button id="ga-play-btn" onclick="togglePlay()" style="
            background:linear-gradient(135deg,#8b5cf6,#7c3aed);border:none;
            color:#fff;width:42px;height:42px;border-radius:10px;cursor:pointer;
            font-size:18px;display:flex;align-items:center;justify-content:center;
            box-shadow:0 0 16px rgba(139,92,246,0.25);transition:transform 0.15s;">▶</button>

        <div style="flex:1;">
            <div style="display:flex;justify-content:space-between;align-items:center;margin-bottom:6px;">
                <span style="color:#e4e4e7;font-size:0.78rem;font-weight:500;">SoundHelix Song 1</span>
                <span id="ga-vol-label" style="color:#8b5cf6;font-size:0.72rem;
                      font-family:'Fira Code',monospace;font-weight:600;">0%</span>
            </div>

            <!-- Volume bar -->
            <div style="width:100%;height:6px;background:#1e1e2e;border-radius:100px;overflow:hidden;">
                <div id="ga-vol-bar" style="width:0%;height:100%;border-radius:100px;
                     background:linear-gradient(90deg,#8b5cf6,#a78bfa);
                     transition:width 0.15s ease;"></div>
            </div>
        </div>
    </div>

    <p id="ga-status" style="color:#52525b;font-size:10px;margin:0;
       font-family:'Fira Code',monospace;text-align:center;letter-spacing:0.03em;">
        Press ▶ then use hand gestures to control volume
    </p>
</div>

<audio id="ga-audio" loop preload="auto"
       src="https://www.soundhelix.com/examples/mp3/SoundHelix-Song-1.mp3"></audio>

<script>
(function() {
    const audio  = document.getElementById('ga-audio');
    const btn    = document.getElementById('ga-play-btn');
    const volBar = document.getElementById('ga-vol-bar');
    const volLbl = document.getElementById('ga-vol-label');
    const status = document.getElementById('ga-status');

    let playing = false;
    let cachedVideo = null;

    window.togglePlay = function() {
        if (!playing) {
            audio.play().then(() => {
                playing = true;
                btn.textContent = '⏸';
                status.textContent = 'Playing — gesture controls active';
                status.style.color = '#22c55e';
            }).catch(e => {
                status.textContent = 'Click again (browser blocked autoplay)';
                status.style.color = '#f59e0b';
            });
        } else {
            audio.pause();
            playing = false;
            btn.textContent = '▶';
            status.textContent = 'Paused';
            status.style.color = '#52525b';
        }
    };

    /* ── Find the WebRTC video element ── */
    function findVideo() {
        if (cachedVideo && cachedVideo.videoWidth > 0) return cachedVideo;
        const parent = window.parent.document;

        // Check videos directly in parent
        for (const v of parent.querySelectorAll('video')) {
            if (v.videoWidth > 0) { cachedVideo = v; return v; }
        }
        // Check inside iframes (streamlit_webrtc uses one)
        for (const f of parent.querySelectorAll('iframe')) {
            try {
                if (!f.contentDocument) continue;
                for (const v of f.contentDocument.querySelectorAll('video')) {
                    if (v.videoWidth > 0) { cachedVideo = v; return v; }
                }
            } catch(e) { /* cross-origin skip */ }
        }
        return null;
    }

    /* ── Canvas for reading bottom bar pixels ── */
    const rc = document.createElement('canvas');
    let rcReady = false;
    const rctx = rc.getContext('2d', { willReadFrequently: true });

    /* ── Read volume from the white bar width at the bottom of the video ── */
    function readVolFromVideo() {
        const video = findVideo();
        if (!video || video.videoWidth === 0 || video.readyState < 2) return -1;
        try {
            const vw = video.videoWidth;
            const vh = video.videoHeight;

            // Resize canvas to match video width (only bottom 3 rows)
            if (rc.width !== vw || !rcReady) {
                rc.width = vw;
                rc.height = 3;
                rcReady = true;
            }

            // Draw only the bottom 3 rows of the video
            rctx.drawImage(video, 0, vh - 3, vw, 3, 0, 0, vw, 3);
            const px = rctx.getImageData(0, 0, vw, 3).data;

            // Scan left-to-right: find where brightness drops (white → dark)
            // Average brightness across the 3 rows for each column
            let barEnd = 0;
            for (let x = 0; x < vw; x++) {
                let brightness = 0;
                for (let y = 0; y < 3; y++) {
                    const idx = (y * vw + x) * 4;
                    brightness += px[idx] + px[idx+1] + px[idx+2];
                }
                brightness /= 9;  // average per channel per row
                if (brightness > 128) {
                    barEnd = x + 1;  // still in the bright zone
                } else if (x > 4) {
                    break;  // transitioned to dark, stop
                }
            }
            return Math.round(barEnd / vw * 100);
        } catch(e) { /* canvas tainted or cross-origin */ }
        return -1;
    }

    /* ── Fallback: read from hidden data attribute ── */
    function readVolFromAttr() {
        try {
            const el = window.parent.document.getElementById('gesture-vol-data');
            if (el) return parseInt(el.getAttribute('data-vol') || '-1', 10);
        } catch(e) {}
        return -1;
    }

    /* ── Main polling loop ── */
    function updateVolume() {
        let vol = readVolFromVideo();
        if (vol < 0) vol = readVolFromAttr();   // fallback
        if (vol < 0) return;

        const clamped = Math.max(0, Math.min(100, vol));
        audio.volume = clamped / 100;
        volBar.style.width = clamped + '%';
        volLbl.textContent = clamped + '%';

        if (clamped < 30) {
            volBar.style.background = 'linear-gradient(90deg,#3c8ce7,#00eaff)';
        } else if (clamped < 65) {
            volBar.style.background = 'linear-gradient(90deg,#22c55e,#4ade80)';
        } else {
            volBar.style.background = 'linear-gradient(90deg,#8b5cf6,#a78bfa)';
        }
    }

    setInterval(updateVolume, 200);
})();
</script>
"""

components.html(AUDIO_HTML, height=160)

st.markdown("""
<div class="section-card">
    <div class="section-header">
        <div class="section-dot"></div>
        <span class="section-title">How It Works</span>
    </div>
    <ul class="steps-list">
        <li class="step-item">
            <div class="step-num">01</div>
            <div class="step-text">Click <strong>START</strong> and allow camera access when prompted.</div>
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
            <div class="step-text">The audio volume <strong>actually changes</strong> based on your gesture — pinch to mute, spread to max.</div>
        </li>
    </ul>
</div>
""", unsafe_allow_html=True)

st.markdown("""
<div class="app-footer">
    <div class="footer-name">Aarav Shukla</div>
    <div class="footer-sub">Class 9th · Computer Vision Project</div>
    <div class="footer-tech">
        <span class="tech-pill">Python</span>
        <span class="tech-pill">OpenCV</span>
        <span class="tech-pill">MediaPipe</span>
        <span class="tech-pill">Streamlit</span>
    </div>
</div>
""", unsafe_allow_html=True)
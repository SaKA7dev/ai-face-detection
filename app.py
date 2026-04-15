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

import streamlit as st
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

/* Remove default streamlit padding */
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

/* ── Audio Player Styling ── */
.audio-wrapper {
    background: var(--bg-card);
    border-radius: 10px;
    padding: 12px 14px;
}

.audio-wrapper audio {
    width: 100%;
    height: 34px;
    border-radius: 6px;
}

.audio-wrapper audio::-webkit-media-controls-panel {
    background: #1a1a24;
}

.audio-hint {
    color: var(--text-muted); font-size: 0.68rem;
    text-align: center; margin-top: 6px;
    font-family: 'Fira Code', monospace;
}

/* ── WebRTC overrides ── */
.stApp iframe { border-radius: 10px !important; }
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

# Shared state for volume tracking across frames
@st.cache_resource
def _get_shared_state():
    return {"vol": 0.0, "fc": 0}

state = _get_shared_state()


def _vol_color(v):
    """Return BGR color based on volume level."""
    if v < 30:
        return (180, 140, 60)    # cool blue-ish
    elif v < 65:
        return (94, 197, 34)     # green
    else:
        return (92, 92, 246)     # purple/accent


def _lerp_color(c1, c2, t):
    """Linearly interpolate between two BGR colors."""
    return tuple(int(a + (b - a) * t) for a, b in zip(c1, c2))


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

        # ── Skeleton ──────────────────────────────────────────────────
        for a, b in CONNS:
            # Subtle glow layer
            overlay = img.copy()
            cv2.line(overlay, pts[a], pts[b], (139, 92, 246), 6, cv2.LINE_AA)
            cv2.addWeighted(overlay, 0.12, img, 0.88, 0, img)
            # Main line
            cv2.line(img, pts[a], pts[b], (139, 92, 246), 2, cv2.LINE_AA)

        # ── Joints ────────────────────────────────────────────────────
        pulse = int(2 * math.sin(fc * 0.18))
        for i, pt in enumerate(pts):
            if i in (4, 8):
                r = 10 + pulse
                # glow
                overlay = img.copy()
                cv2.circle(overlay, pt, r + 6, (139, 92, 246), -1, cv2.LINE_AA)
                cv2.addWeighted(overlay, 0.2, img, 0.8, 0, img)
                # core
                cv2.circle(img, pt, r, (220, 210, 255), -1, cv2.LINE_AA)
                cv2.circle(img, pt, r + 1, (139, 92, 246), 2, cv2.LINE_AA)
            else:
                cv2.circle(img, pt, 3, (180, 180, 200), -1, cv2.LINE_AA)

        # ── Volume from thumb-index distance ──────────────────────────
        thumb, idx = pts[4], pts[8]
        dist = math.hypot(idx[0] - thumb[0], idx[1] - thumb[1])
        raw = float(np.clip(np.interp(dist, [25, 160], [0, 100]), 0, 100))
        state["vol"] = 0.55 * state["vol"] + 0.45 * raw
        vol = state["vol"]
        vc = _vol_color(vol)

        # ── Connector line with glow ──────────────────────────────────
        overlay = img.copy()
        cv2.line(overlay, thumb, idx, vc, 8, cv2.LINE_AA)
        cv2.addWeighted(overlay, 0.15, img, 0.85, 0, img)
        cv2.line(img, thumb, idx, vc, 2, cv2.LINE_AA)

        # ── Midpoint orb ──────────────────────────────────────────────
        mid = ((thumb[0] + idx[0]) // 2, (thumb[1] + idx[1]) // 2)
        mr = int(np.interp(vol, [0, 100], [5, 20]))
        pr = mr + int(2 * math.sin(fc * 0.2))
        overlay = img.copy()
        cv2.circle(overlay, mid, pr + 8, vc, -1, cv2.LINE_AA)
        cv2.addWeighted(overlay, 0.12, img, 0.88, 0, img)
        cv2.circle(img, mid, pr, vc, -1, cv2.LINE_AA)
        cv2.circle(img, mid, pr, (255, 255, 255), 1, cv2.LINE_AA)

        # ── Volume percentage near midpoint ───────────────────────────
        vi = int(vol)
        label_pos = (mid[0] - 15, mid[1] - pr - 12)
        cv2.putText(img, f"{vi}%", label_pos,
                    cv2.FONT_HERSHEY_SIMPLEX, 0.55, (255, 255, 255), 2, cv2.LINE_AA)
        cv2.putText(img, f"{vi}%", label_pos,
                    cv2.FONT_HERSHEY_SIMPLEX, 0.55, vc, 1, cv2.LINE_AA)

    # ── Arc meter (bottom-right corner) ───────────────────────────────────
    vi = int(vol)
    cx, cy, rad = w - 70, h - 80, 44
    vc = _vol_color(vol)
    start_angle, sweep = 135, 270

    # background arc
    cv2.ellipse(img, (cx, cy), (rad, rad), 0, start_angle, start_angle + sweep,
                (25, 25, 35), 3, cv2.LINE_AA)
    # filled arc
    end_angle = start_angle + sweep * vol / 100
    overlay = img.copy()
    cv2.ellipse(overlay, (cx, cy), (rad, rad), 0, start_angle, end_angle, vc, 7, cv2.LINE_AA)
    cv2.addWeighted(overlay, 0.2, img, 0.8, 0, img)
    cv2.ellipse(img, (cx, cy), (rad, rad), 0, start_angle, end_angle, vc, 3, cv2.LINE_AA)

    # tip dot
    tip_a = math.radians(end_angle)
    tx = int(cx + rad * math.cos(tip_a))
    ty = int(cy + rad * math.sin(tip_a))
    tp = int(3 + 1.5 * math.sin(fc * 0.12))
    cv2.circle(img, (tx, ty), tp, (255, 255, 255), -1, cv2.LINE_AA)

    # center text
    cv2.putText(img, f"{vi}%", (cx - 20, cy + 6),
                cv2.FONT_HERSHEY_SIMPLEX, 0.6, (230, 230, 235), 2, cv2.LINE_AA)
    cv2.putText(img, "VOL", (cx - 14, cy + 22),
                cv2.FONT_HERSHEY_SIMPLEX, 0.32, (90, 90, 110), 1, cv2.LINE_AA)

    # ── Status indicator (top-left) ───────────────────────────────────────
    overlay = img.copy()
    cv2.rectangle(overlay, (0, 0), (210, 36), (0, 0, 0), -1)
    cv2.addWeighted(overlay, 0.5, img, 0.5, 0, img)

    if detected:
        status_text = "TRACKING"
        dot_color = (94, 197, 34)  # green
    else:
        status_text = "SHOW HAND"
        dot_color = (80, 80, 100)

    # dot with subtle pulse
    dot_r = 4 + int(1.5 * math.sin(fc * 0.15)) if detected else 4
    cv2.circle(img, (16, 18), dot_r, dot_color, -1, cv2.LINE_AA)
    cv2.putText(img, status_text, (28, 24),
                cv2.FONT_HERSHEY_SIMPLEX, 0.45, dot_color, 1, cv2.LINE_AA)

    # ── Branding watermark (top-right) ────────────────────────────────────
    overlay2 = img.copy()
    cv2.rectangle(overlay2, (w - 175, 0), (w, 30), (0, 0, 0), -1)
    cv2.addWeighted(overlay2, 0.45, img, 0.55, 0, img)
    cv2.putText(img, "AARAV SHUKLA", (w - 165, 20),
                cv2.FONT_HERSHEY_SIMPLEX, 0.42, (139, 92, 246), 1, cv2.LINE_AA)

    return av.VideoFrame.from_ndarray(img, format="bgr24")


# ══════════════════════════════════════════════════════════════════════════════
#  UI LAYOUT
# ══════════════════════════════════════════════════════════════════════════════

# ── Hero ──────────────────────────────────────────────────────────────────────
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

# ── Stats bar ─────────────────────────────────────────────────────────────────
st.markdown("""
<div class="info-grid">
    <div class="info-item"><div class="info-val">720p</div><div class="info-label">Resolution</div></div>
    <div class="info-item"><div class="info-val">30</div><div class="info-label">FPS Target</div></div>
    <div class="info-item"><div class="info-val">21</div><div class="info-label">Landmarks</div></div>
    <div class="info-item"><div class="info-val">1</div><div class="info-label">Hand</div></div>
</div>
""", unsafe_allow_html=True)

# ── Webcam ────────────────────────────────────────────────────────────────────
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

# ── Audio Player (standalone — no server bridge) ─────────────────────────────
st.markdown("""
<div class="section-card">
    <div class="section-header">
        <div class="section-dot"></div>
        <span class="section-title">Test Audio</span>
    </div>
    <div class="audio-wrapper">
        <audio controls loop preload="auto"
            style="width:100%; height:36px; border-radius:6px;
                   filter: invert(0.85) hue-rotate(180deg) saturate(0.5) brightness(0.9);">
            <source src="https://www.soundhelix.com/examples/mp3/SoundHelix-Song-1.mp3" type="audio/mpeg">
            Your browser does not support audio.
        </audio>
        <p style="color:#52525b; font-size:11px; margin:6px 0 0;
                  font-family:'Fira Code',monospace; text-align:center; letter-spacing:0.02em;">
            Press ▶ to play · Volume level shown on camera feed
        </p>
    </div>
</div>
""", unsafe_allow_html=True)

# ── How it works ──────────────────────────────────────────────────────────────
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
            <div class="step-text">The gesture volume is displayed live on the camera overlay.</div>
        </li>
    </ul>
</div>
""", unsafe_allow_html=True)

# ── Footer ────────────────────────────────────────────────────────────────────
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
"""
AI Hand Gesture Volume Controller
Built by Aarav Shukla — Class 9th
Deployment test — checking Python version + deps
"""

import sys
import streamlit as st

st.set_page_config(page_title="Gesture Volume · Aarav Shukla", page_icon="🤚", layout="centered")

st.title("🤚 Gesture Volume Control")
st.info(f"**Python version:** {sys.version}")

# ── Test mediapipe import ──
try:
    import mediapipe as mp
    st.success("✅ MediaPipe loaded")
except ImportError as e:
    st.error(f"❌ MediaPipe failed: {e}")

# ── Test mediapipe Tasks API (the part that crashed) ──
try:
    from mediapipe.tasks import python as mp_python
    from mediapipe.tasks.python import vision
    st.success("✅ MediaPipe Tasks API loaded")
except Exception as e:
    st.error(f"❌ MediaPipe Tasks API failed: {e}")

# ── Test OpenCV ──
try:
    import cv2
    st.success(f"✅ OpenCV loaded (v{cv2.__version__})")
except ImportError as e:
    st.error(f"❌ OpenCV failed: {e}")

# ── Test av ──
try:
    import av
    st.success("✅ PyAV loaded")
except ImportError as e:
    st.error(f"❌ PyAV failed: {e}")

# ── Test webrtc ──
try:
    from streamlit_webrtc import webrtc_streamer
    st.success("✅ streamlit-webrtc loaded")
except ImportError as e:
    st.error(f"❌ streamlit-webrtc failed: {e}")

st.markdown("---")
st.caption("Built by Aarav Shukla · Class 9th")
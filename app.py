"""
AI Hand Gesture Volume Controller
Built by Aarav Shukla — Class 9th
Staged deployment test
"""

import streamlit as st

st.set_page_config(page_title="Gesture Volume · Aarav Shukla", page_icon="🤚", layout="centered")

st.title("🤚 Gesture Volume Control")
st.write("**Step 1:** Basic deployment test — if you see this, infra is working.")

# ── Step 2: Test mediapipe import ──
try:
    import mediapipe as mp
    st.success("✅ MediaPipe loaded successfully")
except ImportError as e:
    st.error(f"❌ MediaPipe failed: {e}")

# ── Step 3: Test OpenCV import ──
try:
    import cv2
    st.success(f"✅ OpenCV loaded successfully (v{cv2.__version__})")
except ImportError as e:
    st.error(f"❌ OpenCV failed: {e}")

# ── Step 4: Test av import ──
try:
    import av
    st.success("✅ PyAV loaded successfully")
except ImportError as e:
    st.error(f"❌ PyAV failed: {e}")

# ── Step 5: Test streamlit-webrtc import ──
try:
    from streamlit_webrtc import webrtc_streamer
    st.success("✅ streamlit-webrtc loaded successfully")
except ImportError as e:
    st.error(f"❌ streamlit-webrtc failed: {e}")

import sys
st.info(f"Python version: {sys.version}")

st.markdown("---")
st.caption("Built by Aarav Shukla · Class 9th")
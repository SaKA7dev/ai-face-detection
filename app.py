"""
AI Hand Gesture Volume Controller
Built by Aarav Shukla — Class 9th
Phase 2: WebRTC test
"""

import streamlit as st
from streamlit_webrtc import webrtc_streamer

st.set_page_config(page_title="Gesture Volume · Aarav Shukla", page_icon="🤚", layout="centered")

st.title("🤚 Gesture Volume Control")
st.write("**Phase 2:** Testing WebRTC camera stream")

# ── Deps confirmed working ──
st.success("✅ All dependencies loaded")

# ── Phase 2: Basic WebRTC ──
webrtc_streamer(
    key="test",
    rtc_configuration={"iceServers": [{"urls": ["stun:stun.l.google.com:19302"]}]},
    media_stream_constraints={"video": True, "audio": False},
)

st.markdown("---")
st.caption("Built by Aarav Shukla · Class 9th")
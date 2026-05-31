import streamlit as st
from pathlib import Path
from src.utils import postprocess_notepad

st.set_page_config(page_title="Status", page_icon="📋")

LECTURE_RECORDING_DIR = "./lecture_recording"
STATUS_FILE = "./lecture_recording/note_pad.md"


st.title("📋 Lecture Recording Status")

if Path(STATUS_FILE).exists():
    st.markdown(postprocess_notepad(STATUS_FILE))
else:
    st.info("Status file not found. Click '🔄 Refresh Status' in the sidebar on the main page to generate it.")

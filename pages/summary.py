import streamlit as st
from pathlib import Path
from src.utils import read_markdown,initialize_notepad
from src.pdf.generator import generate_lecture_pdf

st.set_page_config(page_title="Summaries", page_icon="📚")

LECTURE_RECORDING_DIR = "./lecture_recording"


def get_summary_path(voice_name: str):
    base = Path(LECTURE_RECORDING_DIR) / voice_name
    return {
        "summary_md": base / f"{voice_name}_summary.md",
        "summary_pdf": base / f"{voice_name}_summary.pdf",
        "formatted": base / f"{voice_name}_formatted.md",
    }


def get_voice_folders():
    root = Path(LECTURE_RECORDING_DIR)
    if not root.exists():
        return []
    return sorted([f.name for f in root.iterdir() if f.is_dir() and not f.name.startswith('.')])


st.title("📚 Lecture Summaries")

voice_folders = get_voice_folders()
if voice_folders:
    selected = st.selectbox("Select a lecture:", voice_folders, key="summary_select")
    paths = get_summary_path(selected)

    if paths["summary_md"].exists():
        st.markdown(read_markdown(str(paths["summary_md"])))

        if not paths['summary_pdf'].exists():
            generate_lecture_pdf(read_markdown(str(paths["summary_md"])), str(paths["summary_pdf"]) )

        initialize_notepad(LECTURE_RECORDING_DIR)

        if paths["summary_pdf"].exists():
            with open(paths["summary_pdf"], "rb") as f:
                st.download_button(
                    label="📥 Download as PDF",
                    data=f,
                    file_name=paths["summary_pdf"].name,
                    mime="application/pdf"
                )
    else:
        st.warning(f"Summary not yet available for **{selected}**")
else:
    st.info("No projects yet. Process a lecture from the main page first.")

import streamlit as st
import io
from pathlib import Path
from pydub import AudioSegment


from src.utils import initialize_notepad, process_raw_data, process_info
from src.agent import get_agent
import uuid 

# ─────────────────────────────────────────────
# Config
# ─────────────────────────────────────────────
st.set_page_config(
    page_title="Lecture AI",
    page_icon="🎓",
    layout="wide"
)

LECTURE_RECORDING_DIR = "./lecture_recording"
STATUS_FILE = "./lecture_recording/note_pad.md"

# ─────────────────────────────────────────────
# Helpers
# ─────────────────────────────────────────────

def ensure_lecture_folders(voice_name: str) -> dict:
    """
    Ensure all subfolders exist for a lecture project.
    Creates: raw/, chunks/, asr/ under lecture_recording/{voice_name}/

    Returns dict with paths for convenience.
    """
    base = Path(LECTURE_RECORDING_DIR) / voice_name
    folders = {
        "base": base,
        "raw": base / "raw",
        "chunks": base / "chunks",
        "asr": base / "asr",
    }
    for folder in folders.values():
        folder.mkdir(parents=True, exist_ok=True)
    return folders


def save_audio_file(uploaded_file, voice_name: str) -> str:
    """Save uploaded file to lecture_recording/{voice_name}/raw/"""

    if voice_name: 
        folders = ensure_lecture_folders(voice_name)
        suffix = Path(uploaded_file.name).suffix
        filename = f"{voice_name}_raw{suffix}"

    else: 
        file_name = uploaded_file.name.split('.')[0]
        folders = ensure_lecture_folders(file_name)
        filename = uploaded_file.name
    
    filepath = folders["raw"] / filename
    filepath.write_bytes(uploaded_file.getvalue())
    return str(filepath)


def save_recorded_audio(audio_data, voice_name: str, format: str = "webm") -> str:
    """Save recorded audio to lecture_recording/{voice_name}/raw/"""
    folders = ensure_lecture_folders(voice_name)

    suffix = ".mp3" if format == "mp3" else ".webm"
    filename = f"{voice_name}_raw{suffix}"
    filepath = folders["raw"] / filename

    audio_bytes = audio_data.read() 
    try:
        # 2. Load the raw WAV bytes into Pydub
        audio_segment = AudioSegment.from_file(io.BytesIO(audio_bytes), format="wav")
        
        # 3. Export the file locally as an MP3
        audio_segment.export(filepath, format="mp3", bitrate="192k")
        
        # 4. Success confirmations & local playback
        st.success(f"Successfully saved as `{filepath}`!")
            
    except Exception as e:
        st.error(f"An error occurred during conversion: {e}")
        st.info("Make sure FFmpeg is properly installed on your system.")

    filepath.write_bytes(audio_bytes)
    return str(filepath)


def get_voice_folders():
    """Get list of existing voice/project folders."""
    root = Path(LECTURE_RECORDING_DIR)
    if not root.exists():
        return []
    return sorted([f.name for f in root.iterdir() if f.is_dir() and not f.name.startswith('.')])


def get_summary_path(voice_name: str):
    """Get paths for summary files."""
    base = Path(LECTURE_RECORDING_DIR) / voice_name
    return {
        "summary_md": base / f"{voice_name}_summary.md",
        "summary_pdf": base / f"{voice_name}_summary.pdf",
        "formatted": base / f"{voice_name}_formatted.md",
    }


# ─────────────────────────────────────────────
# Session state
# ─────────────────────────────────────────────
if "messages" not in st.session_state:
    st.session_state.messages = []
    st.session_state.thread_id = str(uuid.uuid4()).replace('-',"")
    st.session_state.agent = get_agent()
    st.session_state.aggregate_file_path = None 

# ─────────────────────────────────────────────
# Sidebar
# ─────────────────────────────────────────────
with st.sidebar:
    st.header("⚙️ Configuration")

    # Input method: upload or record
    input_method = st.radio(
        "Input method:",
        options=["📤 Upload Audio", "🎙️ Record Voice"],
        horizontal=True
    )

    if input_method == "📤 Upload Audio":
        uploaded_file = st.file_uploader(
            "Upload audio file",
            type=["mp3", "wav", "mp4", "m4a", "flac"]
        )
    else:
        st.write("🎙️ Record your voice:")
        audio_data = st.audio_input("Record")

        # Voice / Lecture name (shared)
        voice_name = st.text_input(
            "Voice / Lecture name (Required)",
            placeholder="e.g., lecun_world_model",
            help="This will be the folder name for your lecture",
            
        )

        if audio_data is not None:
            st.audio(audio_data)

    st.divider()

    # Optional: Lecturer name
    st.subheader("📋 Optional Info")
    lecturer_name = st.text_input(
        "Lecturer / Instructor name",
        placeholder="Optional"
    )

    # Chunk size
    max_chunk_size = st.slider(
        "Max chunk size (MB)",
        min_value=0,
        max_value=20,
        value=5
    )

    st.divider()

    # Process button
    if st.button("🚀 Pre-Process Lecture (ASR)", type="primary"):
        if input_method == "📤 Upload Audio" and not uploaded_file:
            st.error("⚠️ Please upload a file")
        elif input_method == "🎙️ Record Voice" and not audio_data:
            st.error("⚠️ Please record your voice")
        else:
            # Save audio
            if input_method == "📤 Upload Audio":
                saved_path = save_audio_file(uploaded_file, voice_name = None)
                input_desc = f"uploaded file: `{uploaded_file.name}`"
            else:
                if not voice_name:
                    st.error("⚠️ Please provide a name")
                # Detect format from name or default
                fmt = "mp3" if hasattr(audio_data, 'name') and str(audio_data.name).endswith('.mp3') else "webm"
                saved_path = save_recorded_audio(audio_data, voice_name, fmt)
                input_desc = "recorded voice"

            st.session_state.raw_file_path = saved_path
            print('Raw File Path:', st.session_state.raw_file_path)

            st.session_state.aggregate_file_path = process_raw_data(raw_path=st.session_state.raw_file_path, max_size_mb=max_chunk_size)


    st.divider()

    # Existing projects
    st.subheader("📁 Projects")
    voice_folders = get_voice_folders()
    if voice_folders:
        for vf in voice_folders:
            paths = get_summary_path(vf)
            done = paths["summary_md"].exists()
            st.write(f"{'✅' if done else '⏳'} {vf}")
    else:
        st.info("No projects yet")

    # Refresh status
    if st.button("🔄 Refresh Status"):
        initialize_notepad(LECTURE_RECORDING_DIR, STATUS_FILE)
        st.success("Status updated")

    st.divider()

    # Navigation
    st.subheader("🗂️ Views")
    st.page_link("pages/summary.py", label="📚 Summaries")
    st.page_link("pages/status.py", label="📋 Status")


# ─────────────────────────────────────────────
# Main Page
# ─────────────────────────────────────────────
st.title("🎓 Lecture AI")

# ── Chat (outside tabs — renders above tabs in document order) ──
chat_history = st.container()
with chat_history:
    for msg in st.session_state.messages:
        with st.chat_message(msg["role"]):
            st.markdown(msg["content"])

if prompt := st.chat_input("Ask about the lecture..."):
    with chat_history:
        st.chat_message("user").markdown(prompt)
        st.session_state.messages.append({"role": "user", "content": prompt})

        if st.session_state.aggregate_file_path:
            aggregate_path, format_path, summary_path = process_info(st.session_state.aggregate_file_path)
            prompt_addition = f"\nPlease Note that the current upload voice file is in: {aggregate_path}, the formatted ASR will be stored in {format_path}, the keynote summary will be stored in {summary_path} "
        else:
            prompt_addition = f"\nCurrently no voice has been upload or record, please check with the notepad if user ask to process any voice files"

        user_message = {"messages": [{"role": "user", "content": prompt + prompt_addition}]}

        with st.chat_message("assistant"):
            response = st.session_state.agent.invoke(user_message, config={"configurable": {"thread_id": st.session_state.thread_id}})
            response_text = response['messages'][-1].content[-1]['text']

            print(response)
            st.markdown(response_text)
            st.session_state.messages.append({"role": "assistant", "content": response_text})


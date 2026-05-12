import streamlit as st
import tempfile
import os
from pathlib import Path

from src.graph.builder import build_lecture_pipeline_graph
from src.graph.state import LecturePipelineState

st.set_page_config(
    page_title="Lecture AI - Transcription Pipeline",
    page_icon="🎓",
    layout="wide"
)

# Title
st.title("🎓 Lecture AI - Transcription Pipeline")
st.markdown("Upload audio, get transcribed lecture notes and tasks extracted as PDF.")

# Initialize session state
if "pipeline_graph" not in st.session_state:
    st.session_state.pipeline_graph = build_lecture_pipeline_graph()
if "results" not in st.session_state:
    st.session_state.results = None
if "processing" not in st.session_state:
    st.session_state.processing = False

# Sidebar: Configuration
with st.sidebar:
    st.header("⚙️ Configuration")

    st.subheader("Audio Preprocessing")
    max_chunk_size = st.slider(
        "Max chunk size (MB)",
        min_value=5,
        max_value=100,
        value=20,
        help="Split audio if file exceeds this size"
    )
    max_duration = st.number_input(
        "Max duration (minutes, 0 = no limit)",
        min_value=0,
        max_value=180,
        value=0,
        help="Slice audio to this duration"
    )
    max_duration = max_duration if max_duration > 0 else None

    st.subheader("Processing")
    show_raw_transcript = st.checkbox("Show raw transcript", value=True)
    show_speaker_transcript = st.checkbox("Show speaker-aware transcript", value=True)

# Main content area
col1, col2 = st.columns([1, 1])

# Left column: Upload and Process
with col1:
    st.header("📤 Upload Audio")

    uploaded_file = st.file_uploader(
        "Choose an audio file",
        type=["mp3", "wav", "mp4", "m4a", "flac"],
        help="Upload lecture audio in any common format"
    )

    if uploaded_file:
        # Save to temp file
        suffix = Path(uploaded_file.name).suffix
        with tempfile.NamedTemporaryFile(delete=False, suffix=suffix) as tmp:
            tmp.write(uploaded_file.getvalue())
            tmp_path = tmp.name

        st.success(f"Uploaded: {uploaded_file.name}")
        st.info(f"Size: {uploaded_file.size / 1024 / 1024:.2f} MB")

        # Process button
        if st.button("🚀 Process Lecture", type="primary", disabled=st.session_state.processing):
            st.session_state.processing = True

            # Progress message
            progress_placeholder = st.empty()

            with st.spinner("Processing audio..."):
                # Ensure output directory exists
                os.makedirs("./output", exist_ok=True)

                # Prepare initial state
                initial_state: LecturePipelineState = {
                    "audio_path": tmp_path,
                    "max_chunk_size_mb": max_chunk_size,
                    "max_duration_minutes": max_duration,
                    "preprocessed_chunks": [],
                    "transcription_segments": [],
                    "speaker_aware_transcript": "",
                    "lecture_notes": "",
                    "task_summary": "",
                    "pdf_path": None,
                    "messages": [],
                    "status": "idle",
                    "error_message": None,
                }

                # Run the pipeline
                try:
                    progress_placeholder.info("⏳ Preprocessing audio...")
                    result = st.session_state.pipeline_graph.invoke(
                        initial_state,
                        config={"configurable": {"thread_id": "lecture-session"}}
                    )
                    st.session_state.results = result
                    progress_placeholder.empty()
                except Exception as e:
                    st.error(f"Error: {str(e)}")
                    st.session_state.results = {"status": "error", "error_message": str(e)}
                finally:
                    st.session_state.processing = False
                    # Cleanup temp file
                    try:
                        os.unlink(tmp_path)
                    except Exception:
                        pass

    # Progress display
    if st.session_state.processing:
        st.progress(0.2, text="Preprocessing audio chunks...")
        st.progress(0.4, text="Transcribing with Whisper...")
        st.progress(0.6, text="Processing with AI agent...")
        st.progress(0.8, text="Generating PDF...")

# Right column: Results
with col2:
    st.header("📋 Results")

    if st.session_state.results:
        results = st.session_state.results

        # Status
        status = results.get("status", "unknown")
        if status == "complete":
            st.success("✅ Processing complete!")
        elif status == "error":
            st.error(f"❌ Error: {results.get('error_message', 'Unknown error')}")
        else:
            st.info(f"Status: {status}")

        # Tabs for different outputs
        tab1, tab2, tab3, tab4 = st.tabs([
            "📝 Raw Transcript",
            "🎤 Speaker Transcript",
            "📚 Lecture Notes",
            "📄 PDF"
        ])

        with tab1:
            st.subheader("Raw Whisper Transcript")
            if results.get("transcription_segments"):
                for seg in results["transcription_segments"]:
                    st.text(f"[{seg['start']:.1f}s-{seg['end']:.1f}s] {seg['speaker']}: {seg['text']}")
            else:
                st.info("No transcript segments available")

        with tab2:
            st.subheader("Speaker-Aware Transcript")
            if results.get("speaker_aware_transcript"):
                st.text_area("", results["speaker_aware_transcript"], height=400, label_visibility="collapsed")
            else:
                st.info("Not yet processed")

        with tab3:
            st.subheader("Generated Lecture Notes")
            if results.get("lecture_notes"):
                st.markdown(results["lecture_notes"])
            else:
                st.info("Not yet generated")

            st.divider()

            st.subheader("Task Summary")
            if results.get("task_summary"):
                st.markdown(results["task_summary"])
            else:
                st.info("No tasks extracted")

        with tab4:
            st.subheader("PDF Report")
            if results.get("pdf_path") and os.path.exists(results["pdf_path"]):
                with open(results["pdf_path"], "rb") as f:
                    st.download_button(
                        label="📥 Download PDF Report",
                        data=f,
                        file_name="lecture_notes.pdf",
                        mime="application/pdf"
                    )
            else:
                st.info("PDF not yet generated")
    else:
        st.info("👈 Upload an audio file and click Process to begin")

# Footer
st.divider()
st.caption("Lecture AI - Powered by LangGraph, DeepAgents, and OpenAI Whisper")
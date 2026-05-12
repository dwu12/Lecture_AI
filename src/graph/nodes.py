import os
from .state import LecturePipelineState
from ..audio.processor import separate_audio_chunk, slice_audio
from ..audio.transcriber import transcribe_audio_diarized


def preprocess_audio(state: LecturePipelineState) -> dict:
    """
    Node 1: Receive audio input and preprocess it.

    - Validates uploaded audio file
    - Slices to max_duration_minutes if set
    - Splits by file size if > max_chunk_size_mb
    - Transcribes each chunk using OpenAI Whisper
    - Merges and sorts segments by start time
    """
    audio_path = state["audio_path"]
    max_size = state.get("max_chunk_size_mb", 20)
    max_mins = state.get("max_duration_minutes")

    if not os.path.exists(audio_path):
        return {
            "status": "error",
            "error_message": f"Audio file not found: {audio_path}",
        }

    # Step 1: Handle duration cap (slice if needed)
    if max_mins and max_mins > 0:
        audio_path = slice_audio(audio_path, minutes=max_mins)

    # Step 2: Split by file size
    chunks = separate_audio_chunk(audio_path, max_size_mb=max_size)

    # Step 3: Transcribe each chunk and merge segments
    all_segments = []
    for chunk_path in chunks:
        segments = transcribe_audio_diarized(chunk_path)
        all_segments.extend(segments)

    # Sort by start time
    all_segments.sort(key=lambda x: x["start"])

    return {
        "preprocessed_chunks": chunks,
        "transcription_segments": all_segments,
        "status": "preprocessing_complete",
    }


def build_deepagent_node(agent):
    """
    Factory to create a deepagent node from a pre-built agent.

    Args:
        agent: A CompiledStateGraph from deepagents.create_deep_agent()
    """
    def deepagent_process(state: LecturePipelineState) -> dict:
        """
        Node 2: Use deepagent to process preprocessed result and generate PDF.

        - Builds raw transcript text from segments
        - Invokes deepagent with orchestration prompt
        - Deepagent delegates to transcription_agent and key_note_agent
        - Generates PDF via filesystem tools
        """
        from langchain_core.messages import HumanMessage
        import json

        # Build raw transcript text from segments
        raw_transcript = "\n".join(
            f"{seg['speaker']}  {seg['text']}"
            for seg in state["transcription_segments"]
        )

        # Prepare the task for the deepagent
        task_message = f"""Process this lecture transcript and generate a PDF report.

AUDIO FILE: {state['audio_path']}

RAW TRANSCRIPT:
{raw_transcript}

Please:
1. Format the transcript into speaker-aware format
2. Generate comprehensive lecture notes with key points, timeline, and summary
3. Extract tasks, due dates, and important assignments
4. Save the lecture notes as a PDF file to ./output/lecture_notes.pdf
5. Also generate a task summary

Output PDF path: ./output/lecture_notes.pdf
"""

        # Invoke the deepagent
        result = agent.invoke({
            "messages": [HumanMessage(content=task_message)]
        })

        # Extract outputs from the agent's message history
        final_message = result["messages"][-1].content if result.get("messages") else ""

        # Extract speaker-aware transcript from state (deepagent writes files)
        transcript_path = "./output/formatted_transcript.txt"
        speaker_transcript = ""
        if os.path.exists(transcript_path):
            with open(transcript_path, "r") as f:
                speaker_transcript = f.read()

        # Parse lecture notes - deepagent should have written to ./output/lecture_notes.md
        notes_path = "./output/lecture_notes.md"
        lecture_notes = ""
        if os.path.exists(notes_path):
            with open(notes_path, "r") as f:
                lecture_notes = f.read()

        # Extract task summary from final message (simplified for now)
        task_summary = _extract_task_summary(final_message)

        return {
            "speaker_aware_transcript": speaker_transcript,
            "lecture_notes": lecture_notes,
            "task_summary": task_summary,
            "pdf_path": "./output/lecture_notes.pdf",
            "status": "complete" if lecture_notes else "partial",
        }

    return deepagent_process


def _extract_task_summary(message_content: str) -> str:
    """Extract task summary from agent's response."""
    # Simple extraction - look for task-related sections
    lines = message_content.split("\n")
    task_lines = []
    in_tasks_section = False

    keywords = ["task", "assignment", "due", "deadline", "homework"]

    for line in lines:
        line_lower = line.lower().strip()
        if any(kw in line_lower for kw in keywords):
            in_tasks_section = True
        if in_tasks_section:
            task_lines.append(line)
        if in_tasks_section and len(line.strip()) == 0 and len(task_lines) > 3:
            break

    return "\n".join(task_lines) if task_lines else "No tasks found."
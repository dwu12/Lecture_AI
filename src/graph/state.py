from typing import TypedDict, Annotated
from langgraph.graph import add_messages
import operator


class LecturePipelineState(TypedDict):
    """State shared across all nodes in the lecture pipeline."""

    # Input
    audio_path: str
    max_chunk_size_mb: int
    max_duration_minutes: int | None

    # Audio Preprocessing
    preprocessed_chunks: list[str]
    transcription_segments: list[dict]  # {"speaker": str, "text": str, "start": float, "end": float}

    # DeepAgent Processing
    speaker_aware_transcript: str
    lecture_notes: str
    task_summary: str
    pdf_path: str | None

    # Messages (built-in for agent)
    messages: Annotated[list, add_messages]

    # Status
    status: str
    error_message: str | None
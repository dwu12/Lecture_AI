from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()
client = OpenAI()

def transcribe_audio_diarized(audio_path: str) -> list[dict]:
    """
    Transcribe audio using OpenAI's gpt-4o-transcribe-diarize.

    Args:
        audio_path: Path to the audio file

    Returns:
        List of segments: [{"speaker": str, "text": str, "start": float, "end": float}]
    """
    with open(audio_path, "rb") as f:
        transcript = client.audio.transcriptions.create(
            model="gpt-4o-transcribe-diarize",
            file=f,
            response_format="diarized_json",
            chunking_strategy="auto",
        )

    segments = []
    for seg in transcript.segments:
        segments.append({
            "speaker": seg.speaker,
            "text": seg.text,
            "start": seg.start,
            "end": seg.end,
        })

    return segments
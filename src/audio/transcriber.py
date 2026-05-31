from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()
client = OpenAI()

def transcribe_audio_diarized(audio_path: str, output_path: str) -> list[dict]:
    """
    Transcribe audio using OpenAI's gpt-4o-transcribe-diarize.

    Args:
        audio_path: Path to the audio file
        output_path: Path to the output ASR file 

    Returns:
        List of segments: [{"speaker": str, "text": str, "start": float, "end": float}]
    """
    with open(audio_path, "rb") as f:
        transcript = client.audio.transcriptions.create(
            model="gpt-4o-transcribe-diarize",
            file=f,
            response_format="diarized_json",
            chunking_strategy="auto"
        )

    segments = []
    output_str = ""

    for seg in transcript.segments:
        output_str += f'Speaker {seg.speaker}: {seg.text}\n'

        segments.append({
            "speaker": seg.speaker,
            "text": seg.text,
            "start": seg.start,
            "end": seg.end,
        })

    if output_path: 
        with open(output_path, 'w', encoding = 'utf-8') as file: 
            file.write(output_str)
            print(f'ASR content has been write to file: {output_path}')


    return segments, output_str 
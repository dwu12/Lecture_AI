import os
from pydub import AudioSegment


def separate_audio_chunk(audio_path: str, max_size_mb: int = 20) -> list[str]:
    """
    Split or convert audio file based on size.

    Args:
        audio_path: Path to the input audio file
        max_size_mb: Maximum chunk size in MB (default 20)

    Returns:
        List of paths to audio chunk files
    """
    if not os.path.exists(audio_path):
        raise FileNotFoundError(f"Audio file not found: {audio_path}")

    file_size_mb = os.path.getsize(audio_path) / (1024 * 1024)

    base_name = os.path.splitext(os.path.basename(audio_path))[0]
    output_dir = os.path.dirname(audio_path) or "."

    audio = AudioSegment.from_file(audio_path)
    total_duration_ms = len(audio)

    if file_size_mb < max_size_mb:
        # Convert to mp3 if not already
        if not audio_path.lower().endswith(".mp3"):
            output_path = os.path.join(output_dir, f"{base_name}.mp3")
            audio.export(output_path, format="mp3")
            return [output_path]
        return [audio_path]

    # Split into chunks
    num_chunks = int((file_size_mb / max_size_mb) + 0.99)
    chunk_duration_ms = total_duration_ms // num_chunks

    chunks = []
    for i in range(num_chunks):
        start = i * chunk_duration_ms
        end = start + chunk_duration_ms if i < num_chunks - 1 else total_duration_ms
        chunk = audio[start:end]
        chunk_path = os.path.join(output_dir, f"{base_name}_chunk_{i + 1}.mp3")
        chunk.export(chunk_path, format="mp3")
        chunks.append(chunk_path)

    return chunks


def slice_audio(audio_path: str, minutes: int) -> str:
    """
    Slice audio to keep only the first N minutes.

    Args:
        audio_path: Path to the input audio file
        minutes: Number of minutes to keep

    Returns:
        Path to the sliced audio file
    """
    if not os.path.exists(audio_path):
        raise FileNotFoundError(f"Audio file not found: {audio_path}")

    if minutes <= 0:
        raise ValueError("minutes must be positive")

    base_name = os.path.splitext(os.path.basename(audio_path))[0]
    output_dir = os.path.dirname(audio_path) or "."

    audio = AudioSegment.from_file(audio_path)
    target_duration_ms = minutes * 60 * 1000

    sliced_audio = audio[:target_duration_ms]
    output_path = os.path.join(output_dir, f"{base_name}_sliced_{minutes}_minutes.mp3")
    sliced_audio.export(output_path, format="mp3")

    return output_path
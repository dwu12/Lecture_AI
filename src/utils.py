from pathlib import Path
import re          

from src.audio.processor import separate_audio_chunk
from src.audio.transcriber import transcribe_audio_diarized
from concurrent.futures import ThreadPoolExecutor, as_completed

def aggregate_asr_files(asr_dir: str, output_path: str | None = None) -> str:                                                                                                              
      """                                                                                                                                                                                    
      Find all .md files in asr_dir, sort by chunk number, and combine into one file.                                                                                                        
                  
      Args:
          asr_dir: Path to the folder containing asr .md files
          output_path: Optional output path. If None, saves to {asr_dir}/../aggregated.md                                                                                                    
      
      Returns:                                                                                                                                                                               
          Path to the aggregated file
      """                                                                                                                                                                                    
      asr_dir = Path(asr_dir)
                                                                                                                                                                                             
      # Find all .md files
      md_files = list(asr_dir.glob("*.md"))

      if not md_files:
          raise FileNotFoundError(f"No .md files found in {asr_dir}")
                                                                                                                                                                                             
      # Extract chunk number for sorting
      def get_chunk_number(path: Path) -> int:                                                                                                                                               
          match = re.search(r"chunk_(\d+)", path.name)                                                                                                                                       
          return int(match.group(1)) if match else 0
                                                                                                                                                                                             
      # Sort by chunk number
      sorted_files = sorted(md_files, key=get_chunk_number)
                                                                                                                                                                                             
      # Combine all content
      aggregated_lines = []                                                                                                                                                                  
      for f in sorted_files:
          aggregated_lines.append(f.read_text())                                                                                                                                             
                                                                                                                                                                                             
      # Write aggregated file
      if output_path is None:                                                                                                                                                                
          output_path = asr_dir / "aggregated.md"
      else:
          output_path = Path(output_path)

      output_path.parent.mkdir(parents=True, exist_ok=True)                                                                                                                                  
      output_path.write_text("".join(aggregated_lines))
                                                                                                                                                                                             
      return str(output_path)


def initialize_notepad(lecture_recording_dir: str, output_path: str | None = None) -> str:
    """
    Scan lecture_recording folder and generate a status report.

    Lists all files in raw/, chunks/, and asr/ folders.
    Marks aggregated file with explanation.
    Only shows pending status for: formatted, summary.md, summary.pdf

    Args:
        lecture_recording_dir: Path to lecture_recording folder
        output_path: Optional output path for the status markdown

    Returns:
        Path to the generated status file
    """
    root = Path(lecture_recording_dir)

    if output_path is None:
        output_path = root / "note_pad.md"
    else:
        output_path = Path(output_path)

    # Find all subfolders (exclude special dirs like __pycache__)
    subfolders = [
        f for f in root.iterdir()
        if f.is_dir() and not f.name.startswith('.') and f.name != '__pycache__'
    ]

    lines = []
    lines.append("# Lecture Recording Status\n")
    lines.append(f"**Root:** `./lecture_recording`\n")
    lines.append(f"**Total lectures:** {len(subfolders)}\n")
    lines.append("---\n")

    for subfolder in sorted(subfolders):
        voice_name = subfolder.name
        lines.append(f"## {voice_name}\n")

        # 1. Raw folder - list the actual file
        raw_dir = subfolder / "raw"
        if raw_dir.exists():
            raw_files = [f for f in raw_dir.iterdir() if f.is_file()]
            if raw_files:
                lines.append("- **raw/ folder**\n")
                for f in sorted(raw_files):
                    lines.append(f"  - `{root}/raw/{f.name}`\n")
            else:
                lines.append("- **⏳ pending** `raw/` (no file)\n")
        else:
            lines.append("- **⏳ pending** `raw/` (folder missing)\n")

        # 2. Chunks folder - list all files
        chunks_dir = subfolder / "chunks"
        if chunks_dir.exists():
            chunk_files = sorted([f for f in chunks_dir.iterdir() if f.is_file()])
            if chunk_files:
                lines.append("- **chunks/ folder**\n")
                for f in chunk_files:
                    lines.append(f"  - `{root}/chunks/{f.name}`\n")
            else:
                lines.append("- **⏳ pending** `{root}/chunks/` (no files)\n")
        else:
            lines.append("- **⏳ pending** `{root}/chunks/` (folder missing)\n")

        # 3. ASR folder - list all files, mark aggregated
        asr_dir = subfolder / "asr"
        if asr_dir.exists():
            asr_files = sorted([f for f in asr_dir.iterdir() if f.is_file()])
            if asr_files:
                lines.append("- **asr/ folder**\n")
                for f in asr_files:
                    if "_aggregated.md" in f.name:
                        lines.append(f"  - `{root}/asr/{f.name}` (This is the aggregated asr file for agent)\n")
                    else:
                        lines.append(f"  - `{root}/asr/{f.name}`\n")
            else:
                lines.append("- **⏳ pending** `{root}/asr/` (no files)\n")
        else:
            lines.append("- **⏳ pending** `{root}/asr/` (folder missing)\n")

        # 4. Only 3 statuses: formatted, summary.md, summary.pdf
        lines.append(f"- **formatted text file**\n")
        formatted_file = subfolder / f"{voice_name}_formatted.md"
        status_formatted = "✅ done" if formatted_file.exists() else "⏳ pending"
        lines.append(f"\t - **{status_formatted}** `{root}/{voice_name}/{voice_name}_formatted.md`\n")

        lines.append(f"- **Key Note Summary (Markdown) file**\n")
        summary_md_file = subfolder / f"{voice_name}_summary.md"
        status_summary_md = "✅ done" if summary_md_file.exists() else "⏳ pending"
        lines.append(f"\t - **{status_summary_md}** `{root}/{voice_name}/{voice_name}_summary.md`\n")

        lines.append(f"- **Key Note Summary (PDF) file**\n")
        summary_pdf_file = subfolder / f"{voice_name}_summary.pdf"
        status_summary_pdf = "✅ done" if summary_pdf_file.exists() else "⏳ pending"
        lines.append(f"\t - **{status_summary_pdf}** `{root}/{voice_name}/{voice_name}_summary.pdf`\n")

        lines.append("\n")

    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_text("".join(lines))

    return str(output_path)


def postprocess_notepad(file_path: str) -> str:
    """
    Post-process the notepad markdown content to replace full paths with just filenames.
    E.g. `./lecture_recording/lecun/raw/test.mp3` → `test.mp3`
    Returns the processed content as a string.
    """
    content = Path(file_path).read_text()
    lines = content.split('\n')
    processed_lines = []
    for line in lines:
        def replace_path(match):
            path = match.group(1)
            return f"`{Path(path).name}`"
        line = re.sub(r'`([^`]+)`', replace_path, line)
        processed_lines.append(line)
    return '\n'.join(processed_lines)


def read_markdown(file_path: str) -> str:
    """
    Read a markdown file and return its content.

    Args:
        file_path: Path to the markdown file

    Returns:
        The markdown content as a string
    """
    return Path(file_path).read_text()


def process_raw_data(raw_path = './lecture_recording/test_lecture/raw/test_lecture_raw.webm', max_size_mb = 5):
    """
    Process raw data, steps: 
    1. chunk raw audio if the size is reach to max_size_mb
    2. run chunks in parallel to get ASR
    3. aggregate ASR
    4. create note pad for central file location
    """
    
    chunk_output_dir = raw_path.split('/raw')[0] + '/chunks/'
    asr_output_dir = raw_path.split('/raw')[0] + '/asr/'
    aggregate_output_path = raw_path.split('/raw')[0] + '/asr/' + raw_path.split('/')[-1].split('.')[0] + '_aggregated.md'

    audio_chunks = separate_audio_chunk(audio_path = raw_path, 
                                        output_dir = chunk_output_dir, 
                                        max_size_mb = max_size_mb)
    
    audio_asr_path = [i.split('chunks')[0] + 'asr/' + i.split('/')[-1].split('.mp3')[0]+'_asr.md' for i in audio_chunks]
    chunks_with_asr = list(zip(audio_chunks, audio_asr_path)) 
                                                                                                                                                                                             
    with ThreadPoolExecutor(max_workers=4) as executor:
        futures = [                                                                                                                                                                            
            executor.submit(transcribe_audio_diarized, chunk, output_path)
            for chunk, output_path in chunks_with_asr                                                                                                                                           
        ]
    
    aggregate_asr_files(asr_output_dir, output_path =aggregate_output_path )
    initialize_notepad(lecture_recording_dir = './lecture_recording/')

    return aggregate_output_path


def process_info(aggregated_asr_markdown_path, folder_name = None): 
    ''' 
    Given the ASR aggregate file, return both format file path and summary file path 
    '''
    if aggregated_asr_markdown_path.startswith('./'):
        aggregated_asr_markdown_path = aggregated_asr_markdown_path[1:]

    output_dir = aggregated_asr_markdown_path.split('/asr')[0]
    
    if not folder_name: 
        folder_name = aggregated_asr_markdown_path.split('/')[2]
    
    formatted_path = output_dir + f'/{folder_name}_formatted.md'
    summary_path = output_dir + f'/{folder_name}_summary.md'

    return aggregated_asr_markdown_path, formatted_path, summary_path
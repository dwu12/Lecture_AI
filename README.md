# Lecture AI

[中文](./README_cn.md) | [English](./README.md)

An AI-powered lecture note-taking assistant. Upload or record lecture audio and get structured notes with task extraction — powered by OpenAI Whisper, DeepAgents, and a multi-agent pipeline.

## Features

- **Audio Upload & Recording** — Support for MP3, WAV, MP4, M4A, FLAC; or record directly in the browser
- **Audio Processing** — Automatic splitting by file size via PyDub
- **Transcription** — OpenAI Whisper with speaker diarization
- **AI Processing Pipeline** — DeepAgent orchestration with two subagents:
  - **Transcription Agent** — cleans raw transcripts into speaker-labeled format
  - **Key-Note Agent** — extracts tasks, due dates, key concepts, and timeline
- **PDF Export** — Generate formatted lecture notes (auto-generated on the Summaries page)
- **Chat Interface** — Ask questions about the lecture directly on the main page
- **Multi-Page Navigation** — Summaries and Status accessible from the sidebar

## Architecture

```
Audio Upload/Recording
       │
       ▼
  Audio Chunking (PyDub, ≤5MB chunks)
       │
       ▼
  Whisper Transcription (speaker diarization)
       │
       ▼
  Aggregate ASR Output
       │
       ▼
  DeepAgent Pipeline
       │
       ├── Transcription Agent → formatted speaker transcript
       │
       └── Key-Note Agent → structured lecture notes + tasks
       │
       ▼
  PDF Generation (markdown_pdf)
```

## Project Structure

```
Lecture_AI/
├── app.py                        # Streamlit web app — main chat page (entry point)
├── pages/
│   ├── summary.py                 # Summaries page — view notes & download PDF
│   └── status.py                  # Status page — view processing status
├── src/
│   ├── agent.py                   # DeepAgent setup (orchestrator + 2 subagents)
│   ├── utils.py                   # Core utilities (chunking, ASR, pipeline)
│   ├── audio/
│   │   ├── processor.py           # Audio chunking & slicing (PyDub)
│   │   └── transcriber.py         # OpenAI Whisper transcription
│   ├── pdf/
│   │   └── generator.py           # PDF generation (markdown_pdf)
│   └── prompt/
│       ├── orchestration_agent_system_prompt.md
│       ├── transcription_agent_system_prompt.md
│       └── key_note_agent_system_prompt.md
└── lecture_recording/             # Working directory for lecture data
    └── [lecture_name]/
        ├── raw/                   # Original uploaded audio
        ├── chunks/                # Split audio chunks
        ├── asr/                   # ASR output per chunk
        ├── [lecture_name]_formatted.md
        ├── [lecture_name]_summary.md
        └── [lecture_name]_summary.pdf
```

## Setup

1. Install dependencies:
```bash
pip install -e .
```

2. Configure environment (copy `.env_example` to `.env` and fill in):
```bash
OPENAI_API_KEY=your_openai_key
ANTHROPIC_API_KEY=your_anthropic_key
OPENROUTER_API_KEY=your_openrouter_key   # optional
ROOT_DIR="Your ROOT DIR"
```

3. Run the application:
```bash
streamlit run app.py        
```

## Usage

### Main Page — Chat
1. Open the app in your browser at the local URL provided by Streamlit
2. Choose input method — upload an audio file or record live
3. Click **🚀 Pre-Process Lecture**
4. Ask questions about the lecture directly in the chat interface

### Summaries Page
- Navigate via the sidebar link **📚 Summaries**
- Select a lecture to view generated notes
- PDF is auto-generated on first visit; download with the button

### Status Page
- Navigate via the sidebar link **📋 Status**
- View the processing status of all lectures (raw, chunks, ASR, formatted, summary)

## Dependencies

- `streamlit` — Web UI
- `deepagents` — Multi-agent orchestration with subagents
- `openai` — Whisper transcription API
- `pydub` — Audio file processing
- `markdown-pdf` — PDF generation from markdown
- `python-dotenv` — Environment variable management

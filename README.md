# Lecture AI

A Streamlit-powered application that transcribes lecture audio and generates structured notes with task extraction using LangGraph and AI agents.

## Features

- **Audio Upload** - Support for MP3, WAV, MP4, M4A, FLAC formats
- **Audio Processing** - Automatic splitting by file size and duration slicing using PyDub
- **Transcription** - OpenAI Whisper with speaker diarization
- **AI Processing** - DeepAgents orchestration with transcription and key-note agents
- **PDF Export** - Generate formatted lecture notes ready for sharing

## Architecture

```
Audio Upload → preprocess_audio → deepagent_process → PDF Report
                   │                    │
                   │                    └── DeepAgent (Orchestrator)
                   │                          ├── Transcription Agent
                   │                          └── Key-Note Agent
                   │
                   └── OpenAI Whisper Diarization
```

## Project Structure

```
src/
├── audio/           # Audio processing
│   ├── processor.py # Chunk splitting & slicing (PyDub)
│   └── transcriber.py # Whisper transcription
├── graph/           # LangGraph pipeline
│   ├── state.py     # Pipeline state schema
│   ├── nodes.py    # Node functions
│   └── builder.py  # Graph assembly
├── pdf/             # PDF generation
│   └── generator.py
└── prompt/          # Agent system prompts
    ├── orchestration_agent_system_prompt.md
    ├── transcription_agent_system_prompt.md
    └── key_note_agent_system_prompt.md
```

## Setup

1. Install dependencies:
```bash
pip install -e .
```

2. Configure environment (`.env`):
```bash
OPENAI_API_KEY=your_openai_key
ANTHROPIC_API_KEY=your_anthropic_key
```

3. Run the application:
```bash
streamlit run app.py
```

## Usage

1. Open the app in your browser
2. Upload an audio file
3. Configure max chunk size and duration (optional)
4. Click "Process Lecture"
5. Review results in the tabs:
   - Raw Transcript (Whisper output)
   - Speaker Transcript (formatted)
   - Lecture Notes (generated)
   - PDF (downloadable)

## Dependencies

- `langgraph` - Graph-based pipeline orchestration
- `deepagents` - Deep agent with subagents and filesystem tools
- `openai` - Whisper transcription API
- `pydub` - Audio file processing
- `reportlab` - PDF generation
- `streamlit` - Web UI
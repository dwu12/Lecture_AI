from deepagents import create_deep_agent
from dotenv import load_dotenv
from langchain_anthropic import ChatAnthropic
from pathlib import Path     
from deepagents.backends import FilesystemBackend
from langgraph.checkpoint.memory import MemorySaver
import os 

load_dotenv()

def read_markdown(file_path: str) -> str:
    """
    Read a markdown file and return its content.

    Args:
        file_path: Path to the markdown file

    Returns:
        The markdown content as a string
    """
    return Path(file_path).read_text()

def get_agent():
    model = ChatAnthropic(
        model="MiniMax-M2.7",
        temperature=0,
        max_tokens=10000,
    )

    orchestration_agent_prompt = read_markdown('./src/prompt/orchestration_agent_system_prompt.md')
    key_note_agent_prompt = read_markdown('./src/prompt/key_note_agent_system_prompt.md') 
    transcription_agent_prompt = read_markdown('./src/prompt/transcription_agent_system_prompt.md')

    key_note_subagent = {
        "name": "keynote-agent",
        "description": "Used to summary the formatted lecture note from transcription agent",
        "system_prompt": key_note_agent_prompt,
    }

    transcription_subagent = {
        "name": "transcription-agent",
        "description": "Used to clean up the raw lecture note and convert it into a structured format",
        "system_prompt": transcription_agent_prompt,
    }

    subagents = [key_note_subagent, transcription_subagent]

    checkpointer = MemorySaver()

    agent = create_deep_agent(model=model, 
                              system_prompt = orchestration_agent_prompt,
                              subagents=subagents,
                              checkpointer = checkpointer,
                              backend=FilesystemBackend(root_dir=os.getenv("ROOT_DIR"), virtual_mode=True)
                            )
    
    return agent



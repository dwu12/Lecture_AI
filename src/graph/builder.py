import os
from langgraph.graph import StateGraph, START, END
from langgraph.checkpoint.memory import MemorySaver
from langchain_anthropic import ChatAnthropic
from deepagents import create_deep_agent
from dotenv import load_dotenv

from .state import LecturePipelineState
from .nodes import preprocess_audio, build_deepagent_node

load_dotenv()

# Prompt path
PROMPT_DIR = os.path.join(os.path.dirname(__file__), "..", "prompt")


def build_lecture_pipeline_graph():
    """
    Build the LangGraph lecture transcription pipeline.

    Flow:
        START → preprocess_audio → deepagent_process → END

    Returns:
        CompiledStateGraph ready to invoke
    """
    # Initialize model (MiniMax via Anthropic-compatible API)
    model = ChatAnthropic(
        model="MiniMax-M2.7",
        temperature=0,
        max_tokens=10000,
    )

    # Load orchestration agent prompt
    orchestration_prompt_path = os.path.join(PROMPT_DIR, "orchestration_agent_system_prompt.md")
    with open(orchestration_prompt_path, "r") as f:
        orchestration_prompt = f.read()

    # Create the deepagent (compiled LangGraph)
    agent = create_deep_agent(
        model=model,
        system_prompt=orchestration_prompt,
    )

    # Create the pipeline graph
    builder = StateGraph(LecturePipelineState)

    # Add nodes
    builder.add_node("preprocess_audio", preprocess_audio)
    builder.add_node("deepagent_process", build_deepagent_node(agent))

    # Define edges
    builder.add_edge(START, "preprocess_audio")
    builder.add_edge("preprocess_audio", "deepagent_process")
    builder.add_edge("deepagent_process", END)

    # Compile with checkpointer for memory
    checkpointer = MemorySaver()

    return builder.compile(checkpointer=checkpointer)
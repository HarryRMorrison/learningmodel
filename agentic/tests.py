from agent import agent_loop
from state_schema import AgentState

def print_trace(state: AgentState):

    print(f"\nRUN: {state.run_id}")
    print(f"STATUS: {state.status}")
    print(f"DURATION: {state.duration_ms:.0f}ms")
    print(f"STEPS: {state.step_count}")

    print("\nMODEL CALLS")

    for call in state.model_history:
        print(
            f"  Step {call.step}: "
            f"{call.duration_ms:.0f}ms | "
            f"{call.prompt_tokens} → "
            f"{call.completion_tokens} tokens"
        )

    print("\nTOOLS")

    for tool in state.tool_history:
        print(
            f"  Step {tool.step}: "
            f"{tool.name} | "
            f"{tool.status} | "
            f"{tool.duration_ms:.0f}ms | "
            f"{tool.attempts} attempt(s)"
        )

    if state.error:
        print("\nERROR")
        print(state.error)

    if state.final_answer:
        print("\nANSWER")
        print(state.final_answer)

from pathlib import Path


def save_trace(state: AgentState):

    Path("traces").mkdir(
        exist_ok=True
    )

    path = Path(
        f"traces/{state.run_id}.json"
    )

    path.write_text(
        state.model_dump_json(
            indent=2
        )
    )

def test_run_agent():
    state = AgentState(user_input="Compare the weather and surf forecast for Perth and Sydney. Which one is going to be a better day for surfing?")
    agent_loop(state)
    print_trace(state)

if __name__ == "__main__":
    test_run_agent()
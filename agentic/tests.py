from agent import agent_loop
from state_schema import AgentState

def test_run_agent():
    state = AgentState(user_input="Compare the weather and surf forecast for Perth and Sydney. Which one is going to be a better day for surfing?")
    agent_loop(state)
    print("STATUS:", state.status)
    print("STEPS:", state.step_count)
    print("TOOLS:", state.tool_history)
    print("FINAL:", state.final_answer)

if __name__ == "__main__":
    test_run_agent()
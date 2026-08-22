from agent import run_agent

def test_run_agent():
    user_input = "What is the weather like in Perth?"
    result = run_agent(user_input, max_steps=5)
    assert isinstance(result, str)
    assert "error" not in result.lower()  # Ensure no error message is returned
    if result:
        print(f"Agent response: {result}")

if __name__ == "__main__":
    test_run_agent()
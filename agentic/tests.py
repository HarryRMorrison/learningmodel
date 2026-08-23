from agent import run_agent

URL = "http://localhost:11434/api/chat"
MAX_STEPS = 10

def test_run_agent():
    user_input = "What is the weather like in Perth? Will it be good for surfing?"
    result = run_agent(user_input, url=URL, max_steps=MAX_STEPS)
    assert isinstance(result, str)
    assert "error" not in result.lower()  # Ensure no error message is returned
    if result:
        print(f"Agent response: {result}")

if __name__ == "__main__":
    test_run_agent()
import requests

def call_model(messages: list, tool_values: list, url: str = "http://localhost:11434/api/chat", llm_model: str = "qwen3:8b"):
    response = requests.post(
        url,
        json={
            "model": llm_model,
            "messages": messages,
            "stream": False,
            "tools": tool_values
        }
    )
    return response
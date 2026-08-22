import requests
from tools import TOOLS

def get_llm_response(messages: list, tool_values: list, url: str, llm_model: str = "qwen3:8b"):
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
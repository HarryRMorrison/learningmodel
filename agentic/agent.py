import json
from llm import get_llm_response
from tools import TOOLS

def run_agent(user_input: str, max_steps: int = 10):

    messages = [
        {
            "role": "user",
            "content": user_input
        }
    ]



    for step in range(max_steps):

        print(f"\n--- Step {step+1} ---")

        response = get_llm_response(messages, tool_values=list(TOOLS.values()), url="http://localhost:11434/api/chat").json()

        # Save the models message
        messages.append(response['message'])

        try:
            tool_calls = response['message']['tool_calls']
        except KeyError:
            # If no tool call, the model has produced its final answer
            return response['message']['content']

        for call in tool_calls:
            tool_name = call['function']['name']
            tool_args = call['function']['arguments']

            print(f"Tool call: {tool_name} with arguments {tool_args}")

            function_ = next((k for k, v in TOOLS.items() if v['function']['name'] == tool_name), None)

            if function_ is None:
                result = json.dumps({"error": f"Tool {tool_name} not found"})
            else:
                try:
                    result = function_(**tool_args)
                except Exception as e:
                    result = json.dumps({"error": str(e)})

            print(f"Tool result: {result}")

            # Send observation back to the model
            messages.append({
                "role": "tool",
                "tool_name": tool_name,
                "content": result,
            })

    raise RuntimeError(
        f"Agent exceeded maximum of {max_steps} steps"
    )
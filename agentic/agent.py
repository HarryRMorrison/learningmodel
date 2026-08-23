import json
from llm import get_llm_response
from tools import TOOLS, build_tool_schemas
from pydantic import ValidationError

def execute_tool(tool_call, verbose: bool = True):
    tool_name = tool_call['function']['name']
    tool_raw_args = tool_call['function']['arguments']

    print(f"Tool call: {tool_name} with arguments {tool_raw_args}")

    tool = TOOLS.get(tool_name)

    if tool is None:
        return json.dumps({"error": f"Tool {tool_name} not found"})

    try:
        args = tool["args_model"].model_validate(tool_raw_args)
    except ValidationError as e:
        return json.dumps({"error": str(e)})

    try:
        return tool['function'](**args.model_dump())
    except Exception as e:
        return json.dumps({"error": f"Tool failed: {str(e)}"})


def run_agent(user_input: str, url: str, max_steps: int = 10):

    messages = [{"role": "user", "content": user_input}]
    tool_schemas = build_tool_schemas()

    for step in range(max_steps):

        print(f"\n--- Step {step+1} ---")

        response = get_llm_response(messages, tool_values=tool_schemas, url=url).json()

        # Save the models message
        messages.append(response['message'])

        tool_calls = response['message'].get("tool_calls", None)

        if tool_calls is None:
            return response['message']["content"]

        for call in tool_calls:
            call_results = execute_tool(call)

            # Send observation back to the model
            messages.append({
                "role": "tool",
                "tool_name": call['function']['name'],
                "content": json.dumps(call_results),
            })

    raise RuntimeError(
        f"Agent exceeded maximum of {max_steps} steps"
    )
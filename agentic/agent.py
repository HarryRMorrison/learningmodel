import json
from llm import call_model
from tools import TOOLS, build_tool_schemas
from pydantic import ValidationError
from state_schema import AgentState, ToolExecution

def execute_tool(name, args, verbose: bool = False):
    if verbose:
        print(f"Tool call: {name} with arguments {args}")

    tool = TOOLS.get(name)

    if tool is None:
        return json.dumps({"error": f"Tool {name} not found"})

    try:
        args = tool["args_model"].model_validate(args)
    except ValidationError as e:
        return json.dumps({"error": str(e)})

    try:
        return tool['function'](**args.model_dump())
    except Exception as e:
        return json.dumps({"error": f"Tool failed: {str(e)}"})


def handle_tool_calls(state: AgentState, tool_calls: list):
    for call in tool_calls:
        name = call['function']['name']
        args = call['function']['arguments']

        result = execute_tool(name, args)

        success = not (
            isinstance(result, dict)
            and "error" in result
        )

        state.tool_history.append(
            ToolExecution(
                name=name,
                arguments=args,
                result=result,
                success=success,
            )
        )

        state.messages.append({
            "role": "tool",
            "tool_name": name,
            "content": json.dumps(result),
        })

def agent_loop(state: AgentState):
    tool_schemas = build_tool_schemas()

    while state.status == "running":

        if state.step_count >= state.max_steps:
            state.status = "error"
            state.error = f"Agent exceeded maximum of {state.max_steps} steps"
            break

        state.step_count += 1

        response = call_model(messages=state.messages, tool_values=tool_schemas).json()
        message = response['message']

        state.messages.append(message)

        tool_calls = message.get("tool_calls", None)

        if tool_calls is None:
            state.status = "completed"
            state.final_answer = message["content"]
            break

        handle_tool_calls(state, tool_calls)
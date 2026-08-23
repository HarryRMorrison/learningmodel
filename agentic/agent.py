import json
from llm import call_model
from tools import TOOLS, build_tool_schemas
from pydantic import ValidationError
from state_schema import AgentState, ToolExecution
from errors_handling import RetryableToolError

def execute_tool(tool, args):
    try:
        validated_args = tool["args_model"].model_validate(args)

    except ValidationError as e:
        return {
            "status": "validation_error",
            "data": None,
            "error": e.errors(),
        }

    try:
        return {
            "status": "success",
            "data": tool["function"](**validated_args.model_dump()),
            "error": None,
        }

    except RetryableToolError as e:
        return {
            "status": "retryable_error",
            "data": None,
            "error": str(e),
        }

    except Exception as e:
        return {
            "status": "fatal_error",
            "data": None,
            "error": str(e),
        }

def handle_tool_calls(
    state: AgentState,
    tool_calls: list
):
    for call in tool_calls:

        name = call["function"]["name"]
        args = call["function"]["arguments"]

        tool = TOOLS.get(name)

        # Unknown tool
        if tool is None:
            result = {
                "status": "fatal_error",
                "data": None,
                "error": f"Tool not found: {name}",
            }

            attempts = 0

        else:
            attempts = 1

            result = execute_tool(tool, args)

            # Only runtime errors are automatically retried
            while (result["status"] == "retryable_error" and attempts < tool["max_calls"]):
                attempts += 1

                result = execute_tool(tool, args)

        state.tool_history.append(
            ToolExecution(
                name=name,
                arguments=args,
                data=result["data"],
                error=result["error"],
                attempts=attempts,
                status=result["status"],
            )
        )

        state.messages.append({
            "role": "tool",
            "tool_name": name,
            "content": json.dumps({
                "status": result["status"],
                "data": result["data"],
                "error": result["error"],
            }),
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

        tool_calls = message.get("tool_calls", [])

        if not tool_calls:
            state.status = "completed"
            state.final_answer = message["content"]
            break

        handle_tool_calls(state, tool_calls)
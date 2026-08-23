from pydantic import BaseModel, Field
from typing import Literal, Any

class ToolExecution(BaseModel):
    name: str
    arguments: dict[str, Any]
    result: Any
    success: bool

class AgentState(BaseModel):

    user_input: str | None = Field(default=None, exclude=True)
    messages: list[dict] = Field(default_factory=list)

    status: Literal["running", "completed", "error"] = "running"

    step_count: int = 0
    max_steps: int = 10

    tool_history: list[ToolExecution] = Field(default_factory=list)

    final_answer: str | None = None
    error: str | None = None

    def model_post_init(self, __context):
        if self.user_input and not self.messages:
            self.messages.append({"role": "user", "content": self.user_input})
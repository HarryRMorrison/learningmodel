from pydantic import BaseModel, Field
from typing import Literal, Any
from uuid import uuid4
from datetime import datetime, timezone

class ToolExecution(BaseModel):
    name: str
    arguments: dict[str, Any]

    status: Literal[
        "success",
        "validation_error",
        "retryable_error",
        "fatal_error",
    ]

    data: Any = None
    error: Any = None
    attempts: int
    duration_ms: float = 0
    step: int

class ModelExecution(BaseModel):
    step: int
    model: str | None = None

    duration_ms: float

    prompt_tokens: int | None = None
    completion_tokens: int | None = None

    model_duration_ms: float | None = None
    load_duration_ms: float | None = None

    done_reason: str | None = None

class AgentState(BaseModel):

    user_input: str | None
    messages: list[dict] = Field(default_factory=list)

    status: Literal[
        "running", 
        "completed", 
        "error", 
        "failed"] = "running"

    step_count: int = 0
    max_steps: int = 10

    tool_history: list[ToolExecution] = Field(default_factory=list)
    model_history: list[ModelExecution] = Field(default_factory=list)

    final_answer: str | None = None
    error: str | None = None

    run_id: str = Field(
        default_factory=lambda: str(uuid4())
    )

    started_at: datetime = Field(
        default_factory=lambda: datetime.now(timezone.utc)
    )

    completed_at: datetime | None = None
    duration_ms: float | None = None

    def model_post_init(self, __context):
        if self.user_input and not self.messages:
            self.messages.append({"role": "user", "content": self.user_input})

    @property
    def total_prompt_tokens(self) -> int:
        return sum(
            x.prompt_tokens or 0
            for x in self.model_history
        )

    @property
    def total_completion_tokens(self) -> int:
        return sum(
            x.completion_tokens or 0
            for x in self.model_history
        )

    @property
    def total_tool_calls(self) -> int:
        return len(self.tool_history)
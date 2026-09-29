from __future__ import annotations

from typing import List, Optional

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel, Field

from app.agent import AgentWorkflow

app = FastAPI(title="Manus AI Agent API", version="0.1.0")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


class ChatMessage(BaseModel):
    message: str = Field(..., min_length=1, max_length=4000)
    conversation_id: Optional[str] = None


class TaskStep(BaseModel):
    order: int
    title: str
    status: str = "pending"


class TaskResponse(BaseModel):
    task_id: str
    summary: str
    status: str
    plan: List[TaskStep]
    answer: str


TASK_STORE: dict[str, TaskResponse] = {}


@app.get("/api/health")
def health() -> dict:
    return {"status": "ok", "service": "manus-ai-agent-backend"}


@app.post("/api/chat", response_model=TaskResponse)
def chat(message: ChatMessage) -> TaskResponse:
    workflow = AgentWorkflow(message.message)
    task = workflow.run()
    TASK_STORE[task.task_id] = task
    return task


@app.get("/api/tasks")
def list_tasks() -> dict:
    return {"tasks": list(TASK_STORE.values())}


@app.get("/")
def root() -> dict:
    return {"message": "Manus AI Agent API is running"}

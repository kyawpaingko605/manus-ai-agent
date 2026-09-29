from __future__ import annotations

import os
import uuid
from typing import List

from openai import OpenAI


class AgentWorkflow:
    def __init__(self, prompt: str):
        self.prompt = prompt.strip()
        self.task_id = str(uuid.uuid4())

    def build_plan(self) -> List[dict]:
        return [
            {"order": 1, "title": "Understand user intent", "status": "completed"},
            {"order": 2, "title": "Collect required information", "status": "in_progress"},
            {"order": 3, "title": "Execute the work plan", "status": "pending"},
            {"order": 4, "title": "Deliver final result", "status": "pending"},
        ]

    def _mock_answer(self) -> str:
        return (
            f"I received your request: '{self.prompt}'.\n\n"
            "This app is running in MVP mode and is ready for a Manus-style autonomous workflow. "
            "The agent has generated a task plan, identified the key steps, and is prepared to gather data, "
            "perform research, or execute work as the next phase.\n\n"
            "To enable real AI reasoning and generation, add OPENAI_API_KEY in the backend environment. "
            "Once configured, the backend will produce richer responses and structured task execution outputs."
        )

    def _generate_openai_answer(self) -> str:
        api_key = os.getenv("OPENAI_API_KEY")
        if not api_key:
            return self._mock_answer()

        client = OpenAI(api_key=api_key)
        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {
                    "role": "system",
                    "content": (
                        "You are a helpful autonomous AI assistant. "
                        "Be concise but useful. The user is asking for a task to be executed. "
                        "Provide a high-level plan and practical next steps."
                    ),
                },
                {"role": "user", "content": self.prompt},
            ],
            temperature=0.7,
        )
        return response.choices[0].message.content or self._mock_answer()

    def run(self):
        from app.main import TaskResponse, TaskStep

        plan = self.build_plan()
        steps = [TaskStep(order=item["order"], title=item["title"], status=item["status"]) for item in plan]

        summary = (
            "Task received and structured for autonomous execution. "
            "The workflow is ready to investigate, plan, and complete the request."
        )

        answer = self._generate_openai_answer()

        return TaskResponse(
            task_id=self.task_id,
            summary=summary,
            status="in_progress",
            plan=steps,
            answer=answer,
        )

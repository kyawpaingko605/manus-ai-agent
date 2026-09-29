# Manus-style AI Agent MVP

A lightweight autonomous AI agent application inspired by Manus-style workflows. This project includes:

- A modern Next.js frontend
- A FastAPI backend
- AI task planning and response generation
- Browser-ready app layout for future expansion
- Task history and status tracking

## Features

- Chat-based task submission
- AI-generated execution plan
- Task status and workflow steps
- Optional OpenAI-powered responses
- CORS-enabled API for frontend integration

## Architecture

- Frontend: `frontend/`
- Backend: `backend/`

## Quick start

### 1) Backend

```bash
cd backend
python -m venv .venv
source .venv/bin/activate  # Windows: .venv\Scripts\activate
pip install -r requirements.txt
uvicorn app.main:app --reload --host 0.0.0.0 --port 8000
```

### 2) Frontend

```bash
cd frontend
npm install
cp .env.example .env.local
npm run dev
```

Then open:

- Frontend: http://localhost:3000
- Backend API: http://localhost:8000

## Environment variables

Backend:

```env
OPENAI_API_KEY=your_openai_api_key_here
```

Frontend:

```env
NEXT_PUBLIC_API_URL=http://localhost:8000
```

## Notes

This is an MVP for a Manus-like experience. It provides the orchestration and UI foundation to expand into:

- browser automation
- document analysis
- file operations
- code execution
- web research
- multi-agent workflows

## License

MIT

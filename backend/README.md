# ATS Backend

FastAPI-based backend service for Arrow Tuning System.

## Tech Stack
- FastAPI
- Python 3.11
- SQLAlchemy (async)
- Pydantic v2
- TimescaleDB
- Redis

## Setup
```bash
pip install -e ".[dev]"
uvicorn app.main:app --reload
```


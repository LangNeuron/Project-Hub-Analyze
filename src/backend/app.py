"""project hub analyze."""

# src/backend/main.py
from __future__ import annotations

from fastapi import FastAPI

app = FastAPI(
    description="project hub analyze",
    title="project hub analyze",
    version="0.0.1",
)


@app.get("/")
def base_root() -> str:
    """base_root check connection."""
    return "Success"

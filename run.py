"""Start application server."""

from __future__ import annotations

from src.backend import app

if __name__ == "__main__":
    import uvicorn

    uvicorn.run(
        app=app, host="localhost", port=8080,
        )

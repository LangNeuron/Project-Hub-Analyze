"""For test api."""

from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def root() -> dict[str, str]:
    """Root."""
    return {"message": "Hello User"}

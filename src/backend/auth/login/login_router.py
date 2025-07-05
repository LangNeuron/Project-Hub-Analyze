"""Login Router."""

from __future__ import annotations

from fastapi import APIRouter

from src.backend.auth.user_controller import user_controller
from src.backend.auth.user_model import UserDB, UserLogin

router = APIRouter()


@router.post("/login")
def login(user_login: UserLogin) -> UserDB | None:
    """Login."""
    return user_controller.login(user_login=user_login)

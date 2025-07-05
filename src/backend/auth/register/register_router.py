"""Register view."""

from __future__ import annotations

from fastapi import APIRouter

from src.backend.auth.user_controller import user_controller
from src.backend.auth.user_model import User, UserRegister

router = APIRouter()


@router.post("/register")
def register(user_register_form: UserRegister) -> User:
    """Registration user."""
    return user_controller.add_user(user_register_form)

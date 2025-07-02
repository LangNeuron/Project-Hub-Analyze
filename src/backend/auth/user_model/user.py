"""Pydantic models."""

from __future__ import annotations

from pydantic import BaseModel

min_password_length = 8


class User(BaseModel):
    """User model."""

    name: str
    email: str
    password: str


class UserRegister(User):
    """User model for registration."""

    confirm_password: str

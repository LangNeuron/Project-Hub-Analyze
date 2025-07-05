"""Pydantic models."""

from __future__ import annotations

from pydantic import BaseModel, EmailStr, model_validator

from .user_exception import NotConfirmPasswordError, PasswordTooSmallError

min_password_length = 8  # TODO: move to config


class User(BaseModel):
    """User model."""

    name: str
    email: EmailStr
    password: str


class UserDB(User):
    """User model in database."""

    user_id: int


class UserRegister(User):
    """User model for registration."""

    confirm_password: str

    @model_validator(mode="after")
    def check_passwords_match(self: UserRegister) -> UserRegister:
        """Check if passwords match."""
        if len(self.password) < min_password_length:
            raise PasswordTooSmallError(message="password is too short")
        if self.password != self.confirm_password:
            raise NotConfirmPasswordError(message="not confirm password")
        # TODO: add more matchs
        return self

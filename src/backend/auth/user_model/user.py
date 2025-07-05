"""Pydantic models."""

from __future__ import annotations

from pydantic import BaseModel, EmailStr, model_validator

from .user_exception import (
    NotConfirmPasswordError,
    PasswordTooSmallError,
    UserNameTooSmallError,
)

min_password_length = 8  # TODO: move to config
min_name_length = 4  # TODO: move to config


class User(BaseModel):
    """User model."""

    name: str
    email: EmailStr
    password: str

    @model_validator(mode="after")
    def check_username(self: UserRegister) -> UserRegister:
        """Check len user name."""
        if len(self.name) < min_name_length:
            raise UserNameTooSmallError(
                message=f"username is too short need at least  \
                    {min_name_length} characters",
            )
        return self

    @model_validator(mode="after")
    def check_len_username(self: UserRegister) -> UserRegister:
        """Check len password."""
        if len(self.password) < min_password_length:
            raise PasswordTooSmallError(
                message=f"username is too short need at least  \
                    {min_password_length} characters",
            )
        return self


class UserDB(User):
    """User model in database."""

    user_id: int


class UserRegister(User):
    """User model for registration."""

    confirm_password: str

    @model_validator(mode="after")
    def check_passwords_confirm(self: UserRegister) -> UserRegister:
        """Check if passwords confirm."""
        if self.password != self.confirm_password:
            raise NotConfirmPasswordError(message="not confirm password")
        return self

"""database."""

from __future__ import annotations

from src.backend.auth.user_model import User


class UserDBModel:
    """Test storage db."""

    def __init__(self) -> None:
        """Initialize."""
        self.storage = {}

    def add_user(self, user: User) -> User:
        self.storage[user.name] = user
        return user


user_db = UserDBModel()

__all__ = ["user_db"]

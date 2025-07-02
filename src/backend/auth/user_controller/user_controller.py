"""User controller."""

from __future__ import annotations

from src.backend.auth.database import user_db
from src.backend.auth.user_model import User, UserRegister


class UserController:
    """Manage user data."""

    def add_user(self, user_register: UserRegister) -> None:
        """Add user to database."""
        # TODO: check if user exists
        return user_db.add_user(
            user=User(
                name=user_register.name,
                email=user_register.email,
                password=user_register.password,
            ),
        )

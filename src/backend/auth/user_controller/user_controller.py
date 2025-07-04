"""User controller."""

from __future__ import annotations

from src.backend.auth.database import user_db
from src.backend.auth.user_model import User, UserRegister

from .user_exceptions import UserExistsError


class UserController:
    """Manage user data."""

    def add_user(self, user_register: UserRegister) -> None:
        """Add user to database."""
        if (
            self.get_user(email=user_register.email, name=user_register.name)
            is not None
        ):
            raise UserExistsError(message="User already exists.")
        return user_db.add_user(
            user=User(
                name=user_register.name,
                email=user_register.email,
                password=user_register.password,
            ),
        )

    def get_user(
        self,
        user_id: int | None = None,
        email: str | None = None,
        name: str | None = None,
    ) -> User:
        """Get user in database."""
        user = None
        if user_id is not None:
            user = user_db.get_user_by_id(user_id)
            if user is not None:
                return user
        if email is not None:
            user = user_db.get_user_by_email(email)
            if user is not None:
                return user
        if name is not None:
            user = user_db.get_user_by_name(name)
            if user is not None:
                return user
        return user

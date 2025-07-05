"""database."""

from __future__ import annotations

from src.backend.auth.user_model import User, UserDB

# TODO: add real database


class UserDBModel:
    """Test storage db."""

    def __init__(self) -> None:
        """Initialize."""
        self.last_id = 0
        self.storage_by_id = {}
        self.storage_by_email = {}
        self.storage_by_name = {}

    def add_user(self, user: User) -> UserDB:
        user_in_db = UserDB(
            **user.model_dump(),
            id=self.last_id,
        )
        self.storage_by_name[user_in_db.name] = user_in_db
        self.storage_by_email[user_in_db.email] = user_in_db
        self.storage_by_id[user_in_db.id] = user_in_db
        self.last_id += 1
        return user

    def get_user_by_id(self, user_id: int) -> UserDB | None:
        return self.storage_by_id.get(user_id, None)

    def get_user_by_email(self, email: str) -> UserDB | None:
        return self.storage_by_email.get(email, None)

    def get_user_by_name(self, name: str) -> User | None:
        return self.storage_by_name.get(name, None)


user_db = UserDBModel()

__all__ = ["user_db"]

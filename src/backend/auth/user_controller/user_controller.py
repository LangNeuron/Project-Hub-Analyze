"""User controller."""

from __future__ import annotations

from src.backend.auth.database import user_db
from src.backend.auth.user_model import User, UserLogin, UserRegister

from .user_exceptions import CredentionalError, UserExistsError


class UserController:
    """Manage user data."""

    def add_user(self, user_register: UserRegister) -> None:
        """Add user to database with checking user exists."""
        if (
            self.get_user(email=user_register.email, name=user_register.name)
            is not None
        ):
            raise UserExistsError(message="User already exists.")
        # add hashed password
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

    def login(self, user_login: UserLogin) -> User:
        """Login user.

        Args:
            user_login (UserLogin): credentionals of user

        Returns:
            User: user data from database

        """
        if user_login.by_name:
            user = self.get_user(name=user_login.name)
            if user is None:
                raise UserExistsError(message="User not found.")
        else:
            user = self.get_user(email=user_login.email)
            if user is None:
                raise UserExistsError(message="User not found.")
        if self.check_password(user_login.password, user.password):
            return user
        raise CredentionalError(message="Wrong password.")

    def check_password(self, password: str, user_password: str) -> None:
        """Verify password."""
        #  TODO: add hashed_password
        return password == user_password

"""Exception for user controller."""

from __future__ import annotations


class UserExistsError(Exception):
    """Raise when user already exists."""

    def __init__(self, message: str) -> None:
        """Init UserExistsError."""
        super().__init__(message)
        self.message = message

class CredentionalError(Exception):
    """Raise credentioal error."""

    def __init__(self, message: str) -> None:
        """Init CredentionalError."""
        super().__init__(message)
        self.message = message

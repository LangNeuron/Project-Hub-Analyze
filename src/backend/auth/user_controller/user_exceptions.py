"""Exception for user controller."""

from __future__ import annotations


class UserExistsError(Exception):
    """Raise when user already exists."""

    def __init__(self, message: str):
        """Init UserExistsError."""
        super().__init__(message)
        self.message = message

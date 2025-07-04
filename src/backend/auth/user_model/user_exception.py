"""Exception for pydantic model."""

from __future__ import annotations


class NotConfirmPasswordError(ValueError):
    """Exception for not confirm password."""

    def __init__(self, message: str) -> None:
        """__init__ exception."""
        super().__init__(message)


class PasswordTooSmallError(ValueError):
    """Exception for password too small."""

    def __init__(self, message: str) -> None:
        """__init__ exception."""
        super().__init__(message)

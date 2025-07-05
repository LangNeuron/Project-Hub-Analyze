"""Auth module."""

from __future__ import annotations

from fastapi import APIRouter

from src.backend.auth.login import login_router
from src.backend.auth.register import register_router

auth_router = APIRouter(
    prefix="/auth",
    tags=["auth"],
)

auth_router.include_router(register_router)
auth_router.include_router(login_router)

__all__ = ["auth_router"]

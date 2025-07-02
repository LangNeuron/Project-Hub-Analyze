"""Auth module."""

from __future__ import annotations

from fastapi import APIRouter

from src.backend.auth.register import register_router

auth_router = APIRouter(
    prefix="/auth",
    tags=["auth"],
)

__all__ = ["auth_router"]

auth_router.include_router(register_router)

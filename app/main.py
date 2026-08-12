"""FastAPI application factory for the Valorant Sens Calculator API."""

from __future__ import annotations

import os

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.api.v1.router import api_router


def get_allowed_origins() -> list[str]:
    """Return explicitly configured browser origins for CORS.

    Set ALLOWED_ORIGINS as a comma-separated list in deployment, for example:
    https://example.github.io,https://app.example.com
    """

    configured_origins = os.getenv(
        "ALLOWED_ORIGINS",
        "http://localhost:3000,http://127.0.0.1:5500",
    )
    return [origin.strip() for origin in configured_origins.split(",") if origin.strip()]


def create_app() -> FastAPI:
    """Create and configure the API application."""

    app = FastAPI(
        title="Valorant Sens Calculator API",
        version="1.0.0",
        description="Calculate eDPI, approximate cm/360, and trial sensitivity ranges.",
        docs_url="/docs",
        redoc_url="/redoc",
    )

    app.add_middleware(
        CORSMiddleware,
        allow_origins=get_allowed_origins(),
        allow_credentials=False,
        allow_methods=["GET", "POST"],
        allow_headers=["Content-Type"],
    )
    app.include_router(api_router, prefix="/api/v1")

    return app


app = create_app()

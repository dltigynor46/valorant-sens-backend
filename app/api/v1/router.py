"""Aggregates all version-specific API routers.

This router collects individual route modules (e.g. calculator, health) and
exposes them under common tags.  Additional routers can be added here as
features expand.
"""

from fastapi import APIRouter

from .routes.calculator import router as calculator_router
from .routes.health import router as health_router


api_router = APIRouter()

# Health-check route
api_router.include_router(health_router, tags=["health"])

# Calculator route for sensitivity calculations
api_router.include_router(calculator_router, prefix="/calculator", tags=["calculator"])

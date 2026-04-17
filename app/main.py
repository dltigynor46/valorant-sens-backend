"""Application factory for the Valorant Sens Calculator service.

This module creates and configures the FastAPI application.  It mounts
versioned API routers and sets global metadata such as title and version.
"""

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware


from .api.v1.router import api_router


def create_app() -> FastAPI:
    """Assemble the FastAPI application.

    Returns:
        FastAPI: Configured FastAPI instance.
    """
    app = FastAPI(
        title="Valorant Sens Calculator",
        version="1.0.0",
        docs_url="/docs",
        redoc_url="/redoc",
    )

    # Include the versioned API router
    
        # Enable CORS
    app.add_middleware(
        CORSMiddleware,
        allow_origins=["*"],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )
app.include_router(api_router, prefix="/api/v1")
    return app


# Initialize the app for ASGI servers like Uvicorn
app = create_app()

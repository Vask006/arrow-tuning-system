"""
FastAPI application entry point for Arrow Tuning System.
"""

from contextlib import asynccontextmanager
from typing import AsyncIterator

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from loguru import logger


@asynccontextmanager
async def lifespan(app: FastAPI) -> AsyncIterator[None]:
    """Lifespan context manager for startup and shutdown events."""
    logger.info("Starting Arrow Tuning System API")
    yield
    logger.info("Shutting down Arrow Tuning System API")


app = FastAPI(
    title="Arrow Tuning System API",
    version="0.1.0",
    description="Privacy-first performance monitoring and analytics platform",
    lifespan=lifespan,
)

# CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/health")
async def health_check() -> dict[str, str]:
    """Health check endpoint."""
    return {"status": "healthy", "version": "0.1.0"}


@app.get("/")
async def root() -> dict[str, str]:
    """Root endpoint."""
    return {
        "message": "Welcome to Arrow Tuning System API",
        "version": "0.1.0",
        "docs": "/docs",
    }


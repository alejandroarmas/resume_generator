import os
from collections.abc import AsyncGenerator
from contextlib import asynccontextmanager

from fastapi import FastAPI
from motorhead import AgnosticDatabase


async def _create_demo_data(db: AgnosticDatabase) -> None:
    """Creates some data for the application."""
    from app_model.device.model import DeviceCreate
    from app_model.device.service import DeviceService

    svc = DeviceService(db)
    for company, title, job_url, location, description in (
        ("Amazon", "Software Engineer", "https://amazon.com", "Seattle, WA", "sample-description"),
        ("Microsoft", "Software Engineer", "https://microsoft.com", '', "sample-description"),
        ("Nvidia", "Software Engineer", "https://nvidia.com", "Santa Clara, CA", "sample-description"),
    ):
        await svc.create(DeviceCreate(company=company, title=title, job_posting_url=job_url, location=location, description=description))


@asynccontextmanager
async def lifespan(app: FastAPI) -> AsyncGenerator[None, None]:
    from app_model.config import create_indexes

    from .database import get_database

    db = get_database()

    # Create all indexes on startup if they don't exist already.
    await create_indexes(db)

    if create_data := os.environ.get("CREATE_DEMO_DATA", None):
        if create_data.lower() in {"1", "true", "y", "yes"}:
            await _create_demo_data(db)

    yield  # Application starts

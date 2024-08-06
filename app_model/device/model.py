from typing import Literal

from motorhead import BaseDocument, Document, UTCDatetime
from pydantic import Field

DeviceStatus = Literal["idle", "working", "maintenance-required", "error"]
"""Device statuses."""


class HXEventTrigger:
    """Server-side HTMX event triggers (i.e. header names)."""

    after_settle = "HX-Trigger-After-Settle"


class HXDeviceEvent:
    """Server-side, device-related HTMX events."""

    created = "device.created"
    deleted = "device.deleted"
    updated = "device.updated"


class Device(Document):
    """Device database model."""

    company: str = Field(min_length=1)
    title: str
    job_posting_url: str
    location: str | None = Field(default=None)
    description: str | None = Field(default=None)
    created_at: UTCDatetime


class DeviceCreate(BaseDocument):
    """Device creation model."""

    company: str = Field(min_length=1)
    title: str
    job_posting_url: str
    location: str | None = Field(default=None)
    description: str | None = Field(default=None)


class DeviceUpdate(BaseDocument):
    """Device update model."""

    company: str | None = Field(default=None, min_length=1)
    title: str | None = Field(default=None)
    job_posting_url: str | None = Field(default=None)
    location: str | None = Field(default=None)
    description: str | None = Field(default=None)

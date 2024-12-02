from datetime import datetime
from typing import Optional
import uuid
from sqlmodel import Column, Enum, Field, SQLModel

from app.enumerations.device_type import DeviceType


class Device(SQLModel, table=True):
    id: Optional[uuid.UUID] = Field(default_factory=uuid.uuid4, primary_key=True)
    device_slug: str = Field(nullable=False)
    device_internal_name: str = Field(nullable=False)
    device_type: DeviceType = Field(sa_column=Column(Enum(DeviceType), nullable=False))


class Alert(SQLModel, table=True):
    id: Optional[uuid.UUID] = Field(default_factory=uuid.uuid4, primary_key=True)
    device_id: uuid.UUID = Field(default=None, nullable=False, foreign_key="device.id")
    field: str = Field(nullable=False)
    alert_type: str = Field(nullable=False)
    open_event_ts: datetime = Field(nullable=False)
    close_event_ts: datetime = Field(nullable=True)
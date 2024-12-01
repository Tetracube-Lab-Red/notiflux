from datetime import datetime
from typing import Optional
import uuid
from sqlmodel import Column, Enum, Field, SQLModel

from app.enumerations.device_type import DeviceType


class Alert(SQLModel, table=True):
    id: Optional[uuid.UUID] = Field(default_factory=uuid.uuid4, primary_key=True)
    device_type: DeviceType = Field(sa_column=Column(Enum(DeviceType), nullable=False))
    device_slug: str = Field(nullable=False)
    field_reference: str = Field(nullable=False)
    open_event_ts: datetime = Field(nullable=False)
    close_event_ts: datetime = Field(nullable=True)
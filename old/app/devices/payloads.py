from dataclasses import dataclass
import uuid
from pydantic import BaseModel, Field

from app.enumerations.device_type import DeviceType


@dataclass
class DeviceProvisioningRequest(BaseModel):
    device_id: uuid.UUID = Field(alias="deviceId")
    device_type: DeviceType = Field(alias="deviceType")
    internal_name: str = Field(alias="internalName")
    slug: str = Field(alias="slug")
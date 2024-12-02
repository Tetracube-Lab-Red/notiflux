from sqlite3 import IntegrityError
from typing import Annotated
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import Annotated
from psycopg2.errors import UniqueViolation

from app.database.db_context import get_database
from app.database.entities import Device
from app.devices.payloads import DeviceProvisioningRequest


router = APIRouter(
    prefix="/device",
    tags=["devices"],
    dependencies=[Depends(get_database)]
)


@router.post("/provisioning")
async def device_provisioning(request: DeviceProvisioningRequest, db: Annotated[Session, Depends(get_database)]):
    device = Device()
    device.device_type = request.device_type
    device.id = request.device_id
    device.device_internal_name = request.internal_name
    device.device_slug = request.slug
    db.add(device)
    try:
        db.commit()
    except Exception as e:
        assert isinstance(e.orig, UniqueViolation)
        raise HTTPException(status_code=409, detail='Device already exists')
    return

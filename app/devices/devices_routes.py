from fastapi import APIRouter, Depends

from app.database.db_context import get_database


router = APIRouter(
    prefix="/device",
    tags=["devices"],
    dependencies=[Depends(get_database)]
)

@router.post("/provisioning")
async def device_provisioning():
    return [{"username": "Rick"}, {"username": "Morty"}]
from contextlib import asynccontextmanager
from fastapi import Depends, FastAPI

from app.devices import devices_routes as devices_router
from app.core import logger
from app.database.db_context import create_db_and_tables, get_database
from app.engine.rules_scripts_loader import load_scripts
from app.ingestion import mqtt_client


@asynccontextmanager
async def lifespan(app: FastAPI):
    logger.info("Custom startup operations")
    create_db_and_tables()
    load_scripts()
    mqtt_client.start_consume()
    yield
    logger.info("Custom shutdown operations")
    mqtt_client.stop_consume()

    
app = FastAPI(
    title="Notiflux",
    description="Make something useful with TetraCube.Red Platform data",
    version="1.0.0",
    lifespan=lifespan,
    dependencies=[Depends(get_database)]
)
app.include_router(devices_router.router)
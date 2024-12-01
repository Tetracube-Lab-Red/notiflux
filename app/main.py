from contextlib import asynccontextmanager
from typing import Annotated, Union
from fastapi import Depends, FastAPI
from sqlmodel import Session

from app.core import logger
from app.database.db_context import create_db_and_tables
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
    lifespan=lifespan
)

@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}
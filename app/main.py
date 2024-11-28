from contextlib import asynccontextmanager
from typing import Union
from fastapi import FastAPI

from app.ingestion import mqtt_client
from app.engine import rule_engine
from app.core import logger, settings


@asynccontextmanager
async def lifespan(app: FastAPI):
    logger.info("Custom startup operations")
    settings.load_settings()
    rule_engine.load_rules(settings=settings.settings)
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
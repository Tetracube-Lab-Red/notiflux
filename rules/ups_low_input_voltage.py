import logging

HANDLED_DEVICE = "UPS"

logger = logging.getLogger("uvicorn")

def evaluate(telemetry: dict):
    logger.info("Running evaluation method for low input voltage")
    return True
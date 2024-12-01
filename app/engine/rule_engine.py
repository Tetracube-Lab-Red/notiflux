from datetime import datetime

from app.core import logger
from app.database.db_context import get_database
from app.database.entities import Alert
from app.enumerations.device_type import DeviceType
from app.clients import ups_pulsar_api_client as ups_api
from app.engine.rules_scripts_loader import rules_scripts


async def run_rules(device_type: DeviceType, device_name: str):
    logger.info(f"Gatering devices information for {device_name}")
    if device_type not in rules_scripts:
        logger.warning(
            f"No scripts available to handle device type: {device_type}")
        return
    device_telemetry = {}
    match device_type:
        case DeviceType.UPS:
            try:
                device_telemetry = await ups_api.get_telemetry(device_name)
            except Exception as e:
                logger.error(f"Cannot retrieve telemetry data for error {e}")

    for script in rules_scripts[device_type]:
        result = script.evaluate(device_telemetry)

    alert = Alert(device_slug="test", device_type=DeviceType.UPS,
                  field_reference="input_voltage", open_event_ts=datetime.utcnow())
    session = next(get_database(), None)
    session.add(alert)
    session.commit()

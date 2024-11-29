from typing import Annotated

from app.core import logger, settings
from app.enumerations.device_type import DeviceType
from app.clients import ups_pulsar_api_client as ups_api
from app.engine.rules_scripts_loader import rules_scripts

def run_rules(device_type: DeviceType, device_name: str):
    logger.info(f"Gatering devices information for {device_name}")
    if device_type not in rules_scripts:
        print(f"No scripts available to handle device type: {device_type}")
        return
    device_telemetry = {}
    match device_type:
        case DeviceType.UPS:
            device_telemetry = ups_api.get_telemetry(device_name)

    for script in rules_scripts[device_type]:
        result = script.evaluate(device_telemetry)
from datetime import datetime
from sqlmodel import select
from app.core import logger
from app.database.db_context import get_database
from app.database.entities import Alert, Device
from app.enumerations.device_type import DeviceType
from app.clients import ups_pulsar_api_client as ups_api
from app.engine.rules_scripts_loader import rules_scripts


async def open_new_alert(evaluation_dict: dict):
    logger.info('Check if there is another open alert of the same type')
    logger.info('Storing the alert')
    await send_firebase_notification()


async def close_old_alert(evaluation_dict: dict):
    logger.info('Check if there is any open alert of the same type')
    logger.info('Closing the alert')
    await send_firebase_notification()


async def send_firebase_notification():
    logger.info('Notify the app for the notification')


async def run_rules(device_type: DeviceType, device_name: str):
    logger.info(f"Gatering devices information for {device_name}")
    db = next(get_database())
    if device_type not in rules_scripts:
        logger.warning(f'No scripts available to handle device type: {device_type}')
        return
    
    device = db.exec(
        select(Device).where(Device.device_internal_name == device_name)
        
    ).first()
    if device == None:
        logger.error(f'Device {device_name} not found')
        return

    device_telemetry = {}
    match device_type:
        case DeviceType.UPS:
            try:
                device_telemetry = await ups_api.get_telemetry(device_name)
            except Exception as e:
                logger.error(f"Cannot retrieve telemetry data for error {e}")
                return

    for script in rules_scripts[device_type]:
        evaluation_dict = script.evaluate(device_telemetry)
        if 'valid' in evaluation_dict and evaluation_dict['valid'] == True:
            await close_old_alert(evaluation_dict)
        elif 'valid' in evaluation_dict and evaluation_dict['valid'] == False:
            await open_new_alert(evaluation_dict)
        else:
            logger.error(f'Invalid evaluation response: {evaluation_dict}')

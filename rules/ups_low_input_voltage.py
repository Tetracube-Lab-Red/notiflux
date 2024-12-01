import logging

HANDLED_DEVICE = "UPS"
ALERT_TYPE = "INPUT_LOW_VOLTAGE"
FIELD = "INPUT_VOLTAGE"

logger = logging.getLogger("uvicorn")


def evaluate(telemetry: dict) -> dict:
    logger.info("Running evaluation method for low input voltage")
    logger.info(telemetry)
    if 'inVoltage' not in telemetry:
        logger.warning(
            'The telemetry does not contain the input voltage parameter')
        return {}
    input_voltage = telemetry['inVoltage']
    if input_voltage < 500:
        return {
            'valid': False,
            'field': FIELD,
            'alert_type': ALERT_TYPE,
            'telemetry_ts': telemetry['telemetryTS']
        }
    return {
        'valid': True,
        'field': FIELD,
        'alert_type': ALERT_TYPE,
        'telemetry_ts': telemetry['telemetryTS']
    }

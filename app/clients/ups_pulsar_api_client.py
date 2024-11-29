import httpx

from app.core import settings,logger


def get_telemetry(device_internal_name: str):
    r = httpx.get(f'{settings.settings['ups_module_api_url']}/ups-pulsar/device/{device_internal_name}/telemetry')
    return r.json()
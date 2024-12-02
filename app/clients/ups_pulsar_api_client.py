import httpx

from app.core.settings import settings,logger


async def get_telemetry(device_internal_name: str):
    async with httpx.AsyncClient() as client:
        r = await client.get(f'{settings.ups_module_api_url}/ups-pulsar/device/{device_internal_name}/telemetry')
    return r.json()
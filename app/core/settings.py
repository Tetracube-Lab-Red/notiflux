from dataclasses import dataclass
import os
from pathlib import Path
from app.core import logger

settings = {}

def load_settings():
        logger.info("Loading NotiFlux settings")
        settings['roles_folders'] = f'{Path.cwd()}/rules/'
        settings['mqtt_broker_host'] = _load_environment_variable('MQTT_BROKER_HOST')
        settings['ups_module_enabled'] = _load_environment_variable('UPS_MODULE_ENABLED') == 'True'
        settings['ups_module_api_url'] = _load_environment_variable('UPS_MODULE_API_URL')
        
def _load_environment_variable(env_name: str) -> str:
    try:
        return os.environ[env_name]
    except:
        raise Exception(f"Cannot load the variable {env_name}")
from dataclasses import dataclass
import os
from app.core import logger

settings = {}

def load_settings():
        logger.info("Loading NotiFlux settings")
        settings['roles_folders'] = _load_environment_variable('ROLES_FOLDERS').split(',')
        
def _load_environment_variable(env_name: str) -> str:
    try:
        return os.environ[env_name]
    except:
        raise Exception(f"Cannot load the variable {env_name}")
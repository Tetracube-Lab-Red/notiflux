from dataclasses import dataclass
import os
from pathlib import Path
from app.core import logger

@dataclass
class Settings():
    rules_folders: str
    mqtt_broker_host: str
    ups_module_enabled: bool
    ups_module_api_url: str
    db_host: str
    db_port: str
    db_user: str
    db_password: str
    db_name: str

    def __init__(self):
        logger.info("Loading NotiFlux settings")
        self.rules_folders = f'{Path.cwd()}/rules/'
        self.mqtt_broker_host = self._load_environment_variable('MQTT_BROKER_HOST')
        self.ups_module_enabled = self._load_environment_variable('UPS_MODULE_ENABLED') == 'True'
        self.ups_module_api_url = self._load_environment_variable('UPS_MODULE_API_URL')
        self.db_host = self._load_environment_variable('DB_HOST')
        self.db_port = self._load_environment_variable('DB_PORT')
        self.db_user = self._load_environment_variable('DB_USER')
        self.db_password = self._load_environment_variable('DB_PASSWD')
        self.db_name = self._load_environment_variable('DB_NAME')
        
            
    def _load_environment_variable(self, env_name: str) -> str:
        try:
            return os.environ[env_name]
        except:
            raise Exception(f"Cannot load the variable {env_name}")
        

settings = Settings()
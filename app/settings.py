from dataclasses import dataclass
import os
from app import logger

@dataclass
class Settings:
    roles_folder: str

    def __init__(self):
        logger.info("Loading NotiFlux settings")
        self.roles_folder = self._load_environment_variable('ROLES_FOLDER')
        
    def _load_environment_variable(self, env_name: str) -> str:
        try:
            return os.environ[env_name]
        except:
            raise Exception(f"Cannot load the variable {env_name}")

settings = Settings()
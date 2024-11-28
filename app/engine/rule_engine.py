from typing import Annotated

from fastapi import Depends
from app import logger, settings

def load_rules(settings: settings.Settings):
    logger.info(f"Gettings roles from path: ${settings.roles_folder}")
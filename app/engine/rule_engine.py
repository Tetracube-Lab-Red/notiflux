from typing import Annotated

from app.core import logger, settings

def load_rules(settings: dict[str, str]):
    logger.info(f"Gettings roles from path: {settings['roles_folders']}")
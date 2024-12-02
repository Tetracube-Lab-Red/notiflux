from collections import defaultdict
import importlib
import os
from app.core.settings import logger, settings
from app.enumerations.device_type import DeviceType

rules_scripts = defaultdict(list)

def load_script(script_path):
    script_name = os.path.splitext(os.path.basename(script_path))[0]
    spec = importlib.util.spec_from_file_location(script_name, script_path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module

def load_scripts():
    logger.info('Loading rules scripts')
    scripts_folder = settings.rules_folders
    for filename in os.listdir(scripts_folder):
        if filename.endswith(".py"):
            script_path = os.path.join(scripts_folder, filename)
            script = load_script(script_path)
            if (hasattr(script, "HANDLED_DEVICE") and 
                script.HANDLED_DEVICE in DeviceType._member_names_ and 
                isinstance(script.HANDLED_DEVICE, str)
                and hasattr(script, "evaluate")):
                rules_scripts[DeviceType[script.HANDLED_DEVICE]].append(script)
            else:
                logger.error(f"Script {filename} does not specify any handled devices.")
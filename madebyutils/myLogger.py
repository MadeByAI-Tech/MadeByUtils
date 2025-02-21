import logging
from logging.config import fileConfig
import os

# Load config 
from pathlib import Path

def _load_config():
    config_path:str = os.getenv("MADEBYUTIL_LOGGER_CONFIG", Path(__file__).parent.joinpath("./logging.conf"))
    config_path:Path = Path(config_path)
    if(config_path.exists() == False):
        raise FileExistsError(f"Config file at {config_path.absolute()} is not exists.")
    fileConfig(config_path.absolute())
    
_load_config()

import importlib
import importlib.util
from os.path import expanduser

from kbmap.log import *

DEFAULT_CONFIG_PATH = expanduser('~/.config/kbmap/config.py')


def load_config(path):
    path = path if path else DEFAULT_CONFIG_PATH
    debug(f'loading config from "{path}"')
    spec = importlib.util.spec_from_file_location('config', path)
    config = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(config)
    debug(f'config loaded')
    return config

import importlib
import importlib.util
from os import path

DEFAULT_CONFIG_PATH = path.expanduser('~/.config/kbmap/config.py')


def load_config(path=DEFAULT_CONFIG_PATH):
    debug(f'loading config from "{path}"')
    spec = importlib.util.spec_from_file_location('config', path)
    config = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(config)
    debug(f'config loaded')
    return config

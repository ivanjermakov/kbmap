"""
Used to load kbmap configuration from specified path of default config path.
"""

import importlib
import importlib.util
from os.path import expanduser

from kbmap.log import *

DEFAULT_CONFIG_PATH = expanduser('~/.config/kbmap/config.py')
"""
Default config path.
Will be used if no other path is specified.
"""


def load_config(path=None):
    """
    Load config from specified path.
    If path is not specified, use DEFAULT_CONFIG_PATH instead.
    """
    path = path if path else DEFAULT_CONFIG_PATH
    debug(f'loading config from "{path}"')
    spec = importlib.util.spec_from_file_location('config', path)
    config = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(config)
    debug(f'config loaded')
    return config

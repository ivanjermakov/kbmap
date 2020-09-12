"""
Used to load kbmap configuration.
"""

import importlib
import importlib.util
from os.path import expanduser
from typing import *

from kbmap.log import *


class Config:
    """
    Config class.
    """
    physical_layout: List[int]
    keymaps: List[List[int]]
    tapping_term: int
    kbmap_default_enabled: bool

    def __init__(self,
                 physical_layout: List[int],
                 keymaps: List[List[int]],
                 tapping_term: int,
                 kbmap_default_enabled: bool
                 ):
        self.physical_layout = physical_layout
        self.keymaps = keymaps
        self.tapping_term = tapping_term
        self.kbmap_default_enabled = kbmap_default_enabled


DEFAULT_CONFIG_PATH = expanduser('~/.config/kbmap/config.py')
"""
Default config path.
Will be used if no other path is specified.
"""


def from_module(module: Any) -> Config:
    """
    Construct config from config file.
    """
    return Config(
        module.physical_layout,
        module.keymaps,
        module.tapping_term,
        module.kbmap_default_enabled,
    )


def load_config(path=None) -> Config:
    """
    Load config from specified path.
    If path is not specified, use DEFAULT_CONFIG_PATH instead.
    """
    path = path if path else DEFAULT_CONFIG_PATH
    debug(f'loading config from "{path}"')
    spec: Any = importlib.util.spec_from_file_location('config', path)
    config = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(config)
    debug(f'config loaded')
    return from_module(config)

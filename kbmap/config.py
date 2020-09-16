"""
Used to load kbmap configuration.
"""

import importlib
import importlib.util
from os.path import expanduser
from typing import *

from kbmap.log import *


class ErrorList:
    """
    List of errors
    """

    errors: List[str]

    def __init__(self, errors: List[str]) -> None:
        self.errors = errors

    def empty(self) -> bool:
        """
        Check whether error list is empty.
        """
        return len(self.errors) == 0


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
                 ) -> None:
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
        module.physical_layout if hasattr(module, 'physical_layout') else None,
        module.keymaps if hasattr(module, 'keymaps') else None,
        module.tapping_term if hasattr(module, 'tapping_term') else None,
        module.kbmap_default_enabled if hasattr(module, 'kbmap_default_enabled') else None
    )


def load(path=None) -> Config:
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


def validate(config: Config) -> ErrorList:
    """
    Validate config for errors
    """
    errors = []

    if not config.physical_layout:
        errors.append('no physical layout')

    if not config.keymaps:
        errors.append('no keymaps')

    if not config.tapping_term:
        errors.append('no tapping term')

    if not config.kbmap_default_enabled:
        errors.append('no kbmap_default_enabled')

    return ErrorList(errors)

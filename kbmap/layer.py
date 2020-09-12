"""
Layer type
"""

from typing import *


class Layer:
    """
    Merges layer as list of keycodes and activator of it.
    """

    keymap: List[int]
    activator: Any

    def __init__(self, keymap: List[int], activator: Any) -> None:
        self.keymap = keymap
        self.activator = activator

    def __repr__(self) -> str:
        return f'(keymap: {self.keymap}, activator: {self.activator})'

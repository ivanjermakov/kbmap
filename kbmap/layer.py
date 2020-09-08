"""
Layer type
"""

from typing import List


class Layer:
    """
    Merges layer as list of keycodes and activator of it.
    """

    keymap: List[int]
    activator: object

    def __init__(self, keymap, activator):
        self.keymap = keymap
        self.activator = activator

    def __repr__(self):
        return f'(keymap: {self.keymap}, activator: {self.activator})'

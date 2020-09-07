from typing import List


class Layer:
    keymap: List[int]
    activator: object

    def __init__(self, keymap, activator):
        self.keymap = keymap
        self.activator = activator

    def __repr__(self):
        return f'(keymap: {self.keymap}, activator: {self.activator})'

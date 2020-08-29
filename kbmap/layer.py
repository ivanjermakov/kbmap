from typing import List


class Layer:
    keymap: List[int]
    activator: object

    def __init__(self, keymap, activator):
        self.keymap = keymap
        self.activator = activator

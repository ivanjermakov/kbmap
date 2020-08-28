from typing import Tuple

from evdev.events import KeyEvent

import host
from action.action_type import ActionType


class ModifiedKeyAction:
    type: ActionType
    key: int
    modifiers: Tuple[int, ...]

    def __init__(self, key, *modifiers):
        self.type = ActionType.ModifiedKeyAction
        self.modifiers = modifiers
        self.key = key

    def handle(self, ui, e, *args):
        debug('-- handling modified key action --')
        if e.value == KeyEvent.key_down:
            for m in self.modifiers:
                host.write_code(ui, m, e.value)
            if self.key:
                host.write_code(ui, self.key, e.value)
        else:
            if self.key:
                host.write_code(ui, self.key, e.value)
            for m in self.modifiers:
                host.write_code(ui, m, e.value)

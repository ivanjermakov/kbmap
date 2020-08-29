from typing import Tuple

from evdev.events import KeyEvent

from kbmap import host
from kbmap.action.action_type import ActionType
from kbmap.log import debug


class ModKeyAction:
    type: ActionType
    key: int
    modifiers: Tuple[int, ...]

    def __init__(self, key, *modifiers):
        self.type = ActionType.ModKeyAction
        self.modifiers = modifiers
        self.key = key

    def handle(self, ui, e, *args):
        debug('-- handling mod key action --')
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

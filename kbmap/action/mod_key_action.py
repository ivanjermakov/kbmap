from typing import *

from evdev import UInput
from evdev.events import InputEvent, KeyEvent

from kbmap import host
from kbmap.action.action_type import ActionType
from kbmap.log import debug


class ModKeyAction:
    """
    Mod key action.
    """

    type: ActionType
    code: Union[int, None]
    modifiers: Tuple[int, ...]

    def __init__(self, code: Union[int, None], *modifiers) -> None:
        self.type = ActionType.ModKeyAction
        self.modifiers = modifiers
        self.code = code

    def handle(self, ui: UInput, e: InputEvent, *args) -> None:
        debug('-- handling mod key action --')
        if e.value == KeyEvent.key_down:
            for m in self.modifiers:
                host.write_code(ui, m, e.value)
            if self.code:
                host.write_code(ui, self.code, e.value)
        else:
            if self.code:
                host.write_code(ui, self.code, e.value)
            for m in self.modifiers:
                host.write_code(ui, m, e.value)

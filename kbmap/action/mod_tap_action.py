from typing import *

from evdev import UInput
from evdev.events import InputEvent, KeyEvent

from kbmap import mapper, host
from kbmap.action.action_type import ActionType
from kbmap.config import Config
from kbmap.log import debug


class ModTapAction:
    """
    Mod tap action.
    """

    type: ActionType
    code: int
    modifiers: Tuple[int, ...]
    used: bool

    def __init__(self, code: int, *modifiers) -> None:
        self.type = ActionType.ModTapAction
        self.modifiers = modifiers
        self.code = code
        self.used = False

    def __repr__(self) -> str:
        return f'MT{"u" if self.used else ""}({self.code}, {",".join(map(str, self.modifiers))})'

    def handle(self, ui: UInput, e: InputEvent, config: Config, pos: int, *args) -> None:
        debug('-- handling mod tap action --')
        if e.value == KeyEvent.key_down:
            mapper.active_tap_actions[pos] = self
            debug('MT is pressed, pressing modifiers')

            host.write_press(ui, *self.modifiers)
        else:
            mapper.active_tap_actions.pop(pos)

            host.release_weak_keys(ui, config)

            debug('MT is released, releasing modifiers')
            host.write_release(ui, *self.modifiers)

            since_last_press = (e.timestamp() - mapper.last_press_timestamps[pos]) * 1000
            debug(f'since last press: {since_last_press}')
            debug(f'action is used: {self.used}')
            if not self.used and since_last_press <= config.tapping_term:
                debug('writing key press')
                host.write_tap(ui, self.code)
            self.used = False

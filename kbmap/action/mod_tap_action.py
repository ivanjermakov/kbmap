from typing import Any, Tuple

from evdev.events import KeyEvent

from kbmap import mapper, host
from kbmap.action.action_type import ActionType
from kbmap.log import debug


class ModTapAction:
    type: ActionType
    key: int
    modifiers: Tuple[Any, ...]
    used: bool

    def __init__(self, key, *modifiers):
        self.type = ActionType.ModTapAction
        self.modifiers = modifiers
        self.key = key
        self.used = False

    def __repr__(self):
        return f'MT({self.key}, {",".join(map(str, self.modifiers))})'

    def handle(self, ui, e, config, pos, *args):
        debug('-- handling mod tap action --')
        if e.value == KeyEvent.key_down:
            debug('MT is pressed, pressing modifiers')
            host.write_press(ui, *self.modifiers)
            mapper.active_tap_actions[pos] = self
        else:
            host.release_weak_keys(ui, config)
            debug('MT is released, releasing modifiers')
            host.write_release(ui, *self.modifiers)
            since_last_press = (e.timestamp() - mapper.last_press_timestamps[pos]) * 1000
            debug(f'since last press: {since_last_press}')
            debug(f'action is used: {self.used}')
            if not self.used and since_last_press <= config.tapping_term:
                debug('writing key press')
                host.write_tap(ui, self.key)

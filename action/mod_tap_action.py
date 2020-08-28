from typing import Any, Tuple

from evdev.events import KeyEvent

import host
from action.action_type import ActionType
from log import debug


class ModTapAction:
    type: ActionType
    key: int
    modifiers: Tuple[Any, ...]

    def __init__(self, key, *modifiers):
        self.type = ActionType.ModTapAction
        self.modifiers = modifiers
        self.key = key

    def handle(self, ui, e, config, last_press_timestamp):
        debug('-- handling mod tap --')
        if e.value == KeyEvent.key_down:
            debug('MT is pressed, pressing modifiers')
            host.write_press(ui, *self.modifiers)
        else:
            debug('MT is released, releasing modifiers')
            host.write_release(ui, *self.modifiers)
            since_last_press = (e.timestamp() - last_press_timestamp) * 1000
            debug(f'since last press: {since_last_press}')
            if since_last_press <= config.tapping_term:
                debug('writing key press')
                host.write_tap(ui, self.key)

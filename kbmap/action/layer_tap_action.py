from evdev import UInput
from evdev.events import InputEvent, KeyEvent

from kbmap import host
from kbmap import mapper
from kbmap.action.action_type import ActionType
from kbmap.config import Config
from kbmap.log import debug


class LayerTapAction:
    """
    Layer tap action.
    """

    type: ActionType
    layer_index: int
    code: int
    used: bool

    def __init__(self, layer_index: int, code: int) -> None:
        self.type = ActionType.LayerTapAction
        self.layer_index = layer_index
        self.code = code
        self.used = False

    def __repr__(self) -> str:
        return f'LT({self.layer_index}, {self.code})'

    def handle(self, ui: UInput, e: InputEvent, config: Config, pos: int, *args) -> None:
        debug('-- handling layer tap action --')
        if e.value == KeyEvent.key_down:
            mapper.active_tap_actions[pos] = self

            debug(f'LT is pressed, enabling layer [{self.layer_index}]')
            mapper.enable_layer(self.layer_index, self, config)
        else:
            mapper.active_tap_actions.pop(pos)

            host.release_weak_keys(ui, config)
            debug(f'LT is released, disabling layer [{self.layer_index}]')

            mapper.disable_layer(ui, self.layer_index, config)

            since_last_press = (e.timestamp() - mapper.last_press_timestamps[pos]) * 1000
            debug(f'since last press: {since_last_press}')
            debug(f'action is used: {self.used}')
            if not self.used and since_last_press <= config.tapping_term:
                debug('writing key press')
                host.write_tap(ui, self.code)
            self.used = False

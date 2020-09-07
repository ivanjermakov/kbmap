from evdev.events import KeyEvent

from kbmap import mapper, host
from kbmap.action.action_type import ActionType
from kbmap.log import debug


class LayerTapAction:
    type: ActionType
    layer: int
    key: int
    used: bool

    def __init__(self, layer, key):
        self.type = ActionType.LayerTapAction
        self.layer = layer
        self.key = key
        self.used = False

    def handle(self, ui, e, config, pos, *args):
        debug('-- handling layer tap action --')
        if e.value == KeyEvent.key_down:
            debug(f'LT is pressed, enabling layer [{self.layer}]')
            mapper.enable_layer(self.layer, self, config)
            mapper.active_tap_actions[pos] = self
        else:
            debug(f'LT is released, disabling layer [{self.layer}]')
            mapper.disable_layer(ui, self.layer, config)
            mapper.active_tap_actions.pop(pos)
            since_last_press = (e.timestamp() - mapper.last_press_timestamps[pos]) * 1000
            debug(f'since last press: {since_last_press}')
            if not self.used and since_last_press <= config.tapping_term:
                debug('writing key press')
                host.write_tap(ui, self.key)

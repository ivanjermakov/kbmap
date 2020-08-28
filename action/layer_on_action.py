from evdev.events import KeyEvent

import host
import mapper
from action.action_type import ActionType
from log import debug


class LayerOnAction:
    type: ActionType
    layer: int

    def __init__(self, layer):
        self.type = ActionType.LayerOnAction
        self.layer = layer

    def handle(self, ui, e, config, *args):
        debug('-- handling layer on action --')
        mapper.active_layers[self.layer] = e.value == KeyEvent.key_down
        if e.value == KeyEvent.key_up:
            host.release_layer_keys(ui, self.layer, config)

from evdev.events import KeyEvent

from kbmap import mapper
from kbmap.action.action_type import ActionType
from kbmap.log import debug


class LayerOnAction:
    type: ActionType
    layer: int

    def __init__(self, layer):
        self.type = ActionType.LayerOnAction
        self.layer = layer

    def handle(self, ui, e, config, *args):
        debug('-- handling layer on action --')
        if e.value == KeyEvent.key_up:
            mapper.enable_layer(self.layer, self, config)
        else:
            mapper.disable_layer(ui, self.layer, config)

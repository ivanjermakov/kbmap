from evdev.events import KeyEvent

from kbmap import mapper
from kbmap.action.action_type import ActionType
from kbmap.log import debug


class LayerToggleAction:
    type: ActionType
    layer: int

    def __init__(self, layer, ):
        self.type = ActionType.LayerToggleAction
        self.layer = layer

    def handle(self, ui, e, config, *args):
        debug('-- handling layer toggle action --')
        if e.value == KeyEvent.key_down:
            if mapper.active_layers[self.layer]:
                debug(f'disabling layer [{self.layer}]')
                mapper.disable_layer(ui, self.layer, config)
            else:
                debug(f'enabling layer [{self.layer}]')
                mapper.enable_layer(self.layer, self, config)

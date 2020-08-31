from typing import Tuple

from evdev.events import KeyEvent

from kbmap import mapper, host
from kbmap.action.action_type import ActionType
from kbmap.action.mod_key_action import ModKeyAction
from kbmap.log import debug


class LayerModAction:
    type: ActionType
    layer: int
    modifiers: Tuple[int, ...]

    def __init__(self, layer, *modifiers):
        self.type = ActionType.LayerOnAction
        self.layer = layer
        self.modifiers = modifiers

    def handle(self, ui, e, config, *args):
        debug('-- handling layer mod action --')
        if e.value == KeyEvent.key_down:
            mapper.enable_layer(self.layer, self, config)
        else:
            mapper.disable_layer(ui, self.layer, config)

    def handle_layer_key(self, ui, key, e, *args):
        debug('-- handling LM layer key --')
        ModKeyAction(key, *self.modifiers).handle(ui, e)

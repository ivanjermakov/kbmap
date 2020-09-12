from typing import Tuple

from evdev import UInput
from evdev.events import KeyEvent, InputEvent

from kbmap import mapper
from kbmap.action.action_type import ActionType
from kbmap.action.mod_key_action import ModKeyAction
from kbmap.log import debug


class LayerModAction:
    """
    Layer mod action.
    """

    type: ActionType
    layer_index: int
    modifiers: Tuple[int, ...]

    def __init__(self, layer_index: int, *modifiers: int) -> None:
        self.type = ActionType.LayerOnAction
        self.layer_index = layer_index
        self.modifiers = modifiers

    def handle(self, ui: UInput, e, config, *args) -> None:
        debug('-- handling layer mod action --')
        if e.value == KeyEvent.key_down:
            mapper.enable_layer(self.layer_index, self, config)
        else:
            mapper.disable_layer(ui, self.layer_index, config)

    def handle_layer_key(self, ui: UInput, code: int, e: InputEvent, *args) -> None:
        debug('-- handling LM layer key --')
        ModKeyAction(code, *self.modifiers).handle(ui, e)

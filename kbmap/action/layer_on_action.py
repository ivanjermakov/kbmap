from evdev import UInput
from evdev.events import InputEvent
from evdev.events import KeyEvent

from kbmap import mapper
from kbmap.action.action_type import ActionType
from kbmap.config import Config
from kbmap.log import debug


class LayerOnAction:
    """
    Layer on action.
    """

    type: ActionType
    layer_index: int

    def __init__(self, layer_index: int) -> None:
        self.type = ActionType.LayerOnAction
        self.layer_index = layer_index

    def handle(self, ui: UInput, e: InputEvent, config: Config, *args):
        debug('-- handling layer on action --')
        if e.value == KeyEvent.key_down:
            mapper.enable_layer(self.layer_index, self, config)
        else:
            mapper.disable_layer(ui, self.layer_index, config)

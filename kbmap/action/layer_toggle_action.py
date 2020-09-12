from evdev import UInput
from evdev.events import InputEvent, KeyEvent

from kbmap import mapper
from kbmap.action.action_type import ActionType
from kbmap.config import Config
from kbmap.log import debug


class LayerToggleAction:
    """
    Layer toggle action.
    """

    type: ActionType
    layer_index: int

    def __init__(self, layer_index: int) -> None:
        self.type = ActionType.LayerToggleAction
        self.layer_index = layer_index

    def handle(self, ui: UInput, e: InputEvent, config: Config, *args) -> None:
        debug('-- handling layer toggle action --')
        if e.value == KeyEvent.key_down:
            if mapper.active_layers[self.layer_index]:
                debug(f'disabling layer [{self.layer_index}]')
                mapper.disable_layer(ui, self.layer_index, config)
            else:
                debug(f'enabling layer [{self.layer_index}]')
                mapper.enable_layer(self.layer_index, self, config)

"""
Used for handling keyboard events and delegating mapping logic.
"""

from typing import *

from evdev import UInput, ecodes
from evdev.events import KeyEvent, InputEvent

import kbmap.config as c
from kbmap import keyboard, key, host
from kbmap.action.action_type import ActionType
from kbmap.config import Config
from kbmap.layer import Layer
from kbmap.log import *

kbmap_enabled = True
"""
Determines whether mapping is enabled.
If option is False, physical layout keys written directly into UI.
"""

last_press_timestamps: List[Union[float, None]] = []
"""
Store last keypress (key down) event for each keyboard position.
Used in tap actions behavior.
"""

active_layers: List[Union[Layer, None]] = []
"""
List of fixed length, specified by config, equal to the number of layers.
Active layers store Layer objects, inactive store None.
Access it by layer index.
"""

layers_keys_pressed: List[List[bool]] = []
"""
Boolean matrix of currently pressed keys by [layer][position]
"""

active_tap_actions: Dict[int, Any] = {}
"""
Dictionary of active MT and LT actions, stored as pos -> action.
Used in tap actions behavior.
"""


def init_mapper(config: Config) -> None:
    """
    Initialize mapper.
    """
    global kbmap_enabled
    kbmap_enabled = config.kbmap_default_enabled

    global last_press_timestamps
    last_press_timestamps = [None for _ in range(len(config.physical_layout))]

    global active_layers
    active_layers = [None for _ in range(len(config.keymaps))]
    # base layer is always active
    active_layers[0] = Layer(config.keymaps[0], None)

    global layers_keys_pressed
    layers_keys_pressed = [[] for _ in range(len(active_layers))]
    for i in range(len(active_layers)):
        layers_keys_pressed[i] = [False for _ in range(len(config.keymaps[i]))]


def map_device(kb_name: str, config_path: str, ui_name: str = 'kbmap') -> None:
    """
    Create virtual device with ui_name that will remap keyboard events from device with name device_name and
    delegate event handling.

    :param kb_name: source device name. This device will be grabbed
    :param config_path: path to configuration file
    :param ui_name: optional UInput device that will be created to write mapped events
    """

    config = c.load_config(config_path)
    init_mapper(config)

    kb = keyboard.get_device_by_name(kb_name)
    keyboard.grab(kb)

    ui = UInput.from_device(kb, name=ui_name)

    with ui:
        keyboard.listen_key_events(
            kb,
            lambda e: handle_event(e, ui, config),
            False
        )


def handle_event(e: InputEvent, ui: UInput, config: Config) -> None:
    """
    Handle keyboard event.
    Remap it to specified UInput.

    :param e: key event
    :param ui: UInput
    :param config: mapper configuration
    """

    debug(f'-------- handling {e} --------')

    pos = map_code_to_pos(e.code, config)
    if pos is None:
        return

    debug(f'key is {ecodes.KEY[e.code]} ({e.code}) at {pos}')

    if handle_kbmap_toggle(ui, e, pos, config):
        return

    if not kbmap_enabled:
        write_code(ui, e.code, e, 0, config)
        return

    try:
        key, layer_index = find_key(pos, config)

        if hasattr(key, 'type') and hasattr(key, 'handle'):
            debug(f'key is mapped to action of type {key.type} at {pos}')
            key.handle(ui, e, config, pos)
        else:
            debug(f'key is mapped to key: {get_key_name(key)} ({key}) at {pos}')
            write_code(ui, key, e, layer_index, config)

        layers_keys_pressed[layer_index][pos] = e.value == KeyEvent.key_down
        update_active_tap_actions(pos)
        update_timestamps(pos, e)
    except LookupError:
        log(f'no mapping found for key {ecodes.KEY[e.code]} at {pos}')


def get_key_name(code: int) -> str:
    """
    Get string representation of key code based on evdev ecodes.KEY dictionary.
    """

    if code == 999:
        return 'KC_NO'
    return ecodes.KEY.get(code, "UNKNOWN")


def map_code_to_pos(code: int, config: Config) -> Union[int, None]:
    """
    Map key code to position of it on physical layout specified by config
    """

    debug(f'looking for key {ecodes.KEY[code]} with code {code}')
    try:
        return config.physical_layout.index(code)
    except ValueError:
        log(f'no key {ecodes.KEY[code]} in physical config')
        return None


def update_timestamps(pos: int, e: InputEvent) -> None:
    """
    Update timestamps of last key press.
    """

    global last_press_timestamps

    new_value = e.timestamp() if e.value == KeyEvent.key_down else None
    last_press_timestamps[pos] = new_value
    debug(f'updated timestamp at [{pos}] to {new_value}')


def find_key(pos: int, config: Config) -> Tuple[Any, int]:
    """
    Find which key to use regarding active layers and key position.
    Picked up first non-KC_TRANS key within active layers.
    Layers with higher index have higher precedence.

    :param pos
    :param config
    :return tuple of key or action and its layer index
    """
    global active_layers
    for layer_index, layer in reversed(list(enumerate(config.keymaps))):
        layer_key = layer[pos]
        if active_layers[layer_index] and layer_key != key.KC_TRANSPARENT:
            return layer_key, layer_index
    raise LookupError('no key found')


def write_code(ui: UInput, code: int, e: InputEvent, layer_index: int, config: Config) -> None:
    """
    Handle code writing.
    """

    global active_layers
    active_layer = active_layers[layer_index]
    if active_layer and active_layer.activator and hasattr(active_layer.activator, 'handle_layer_key'):
        active_layer.activator.handle_layer_key(ui, code, e, config)
    else:
        host.write_code(ui, code, e.value)


def enable_layer(layer_index: int, activator: object, config: Config) -> None:
    """
    Enable specified layer.
    """

    global active_layers
    active_layers[layer_index] = Layer(config.keymaps[layer_index], activator)


def disable_layer(ui: UInput, layer_index: int, config: Config) -> None:
    """
    Disable specified layer.
    """

    global active_layers
    active_layers[layer_index] = None
    host.release_weak_keys(ui, config)


def handle_kbmap_toggle(ui: UInput, e: InputEvent, pos: int, config: Config) -> bool:
    """
    Handle kbmap toggle on and off.
    """
    try:
        key, layer_index = find_key(pos, config)

        if hasattr(key, 'type') and key.type == ActionType.KbmapToggleAction:
            key.handle(ui, e, config, pos)
            return True
    except LookupError:
        pass
    return False


def update_active_tap_actions(pos: int) -> None:
    """
    Update usage of MT and LT actions.
    """
    for action_pos, action in active_tap_actions.items():
        if action_pos != pos:
            action.used = True

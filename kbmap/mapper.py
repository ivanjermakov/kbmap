import importlib
import importlib.util
from os import path
from typing import List

from evdev import UInput, ecodes
from evdev.events import KeyEvent

from kbmap import keyboard, key, host
from kbmap.layer import Layer
from kbmap.log import debug, log

kbmap_enabled = True
last_press_timestamps: List[float] = []
active_layers: List[Layer] = []
layers_keys_pressed: List[List[int]] = []
from kbmap.action.action_type import ActionType

DEFAULT_CONFIG_PATH = path.expanduser('~/.config/kbmap/config.py')


def load_config(path):
    debug(f'loading config from "{path}"')
    spec = importlib.util.spec_from_file_location('config', path)
    config = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(config)
    debug(f'config loaded')
    return config


def init_mapper(config):
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


def map_device(kb_name, config_path, ui_name='kbmap'):
    """
    Create virtual device with ui_name that will remap keyboard events from device with name device_name.
    :param config_path: path to configuration file
    :param kb_name: source device name. This device will be grabbed
    :param ui_name: optional uinput device that will be created to write mapped events
    """

    config = load_config(config_path if config_path else DEFAULT_CONFIG_PATH)
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


def handle_event(e, ui, config):
    debug(f'-------- handling {e} --------')

    pos = map_key_to_pos(e.code, config)
    if pos is None:
        return

    debug(f'key is {ecodes.KEY[e.code]} ({e.code}) at {pos}')

    if handle_kbmap_toggle(ui, e, pos, config):
        return

    if not kbmap_enabled:
        write_key(ui, e.code, e, 0, config)
        return

    try:
        key, layer_index = find_key(pos, config)

        if hasattr(key, 'type') and hasattr(key, 'handle'):
            debug(f'key is mapped to action of type {key.type} at {pos}')
            key.handle(ui, e, config, pos)
        else:
            debug(f'key is mapped to key: {get_key_name(key)} ({key}) at {pos}')
            write_key(ui, key, e, layer_index, config)

        layers_keys_pressed[layer_index][pos] = e.value == KeyEvent.key_down
        update_timestamps(pos, e)
    except LookupError:
        log(f'no mapping found for key {ecodes.KEY[e.code]} at {pos}')


def get_key_name(key):
    if key == 999:
        return 'KC_NO'
    return ecodes.KEY.get(key, "UNKNOWN")


def map_key_to_pos(code, config):
    debug(f'looking for key {ecodes.KEY[code]} with code {code}')
    try:
        return config.physical_layout.index(code)
    except ValueError:
        log(f'no key {ecodes.KEY[code]} in physical config')


def update_timestamps(pos, e):
    global last_press_timestamps

    new_value = e.timestamp() if e.value == KeyEvent.key_down else None
    last_press_timestamps[pos] = new_value
    debug(f'updated timestamp at [{pos}] to {new_value}')


def find_key(pos, config):
    """
    Find which key to use regarding active layers and key position.
    Picked up first non-KC_TRANS key within active layers.
    Layers with higher index have higher precedence.

    :param pos
    :param config
    :return key or action
    """
    global active_layers
    for layer_index, layer in reversed(list(enumerate(config.keymaps))):
        layer_key = layer[pos]
        if active_layers[layer_index] and layer_key != key.KC_TRANSPARENT:
            return layer_key, layer_index
    raise LookupError('no key found')


def write_key(ui, key, e, layer, config):
    global active_layers
    active_layer = active_layers[layer]
    if active_layer and active_layer.activator and hasattr(active_layer.activator, 'handle_layer_key'):
        active_layer.activator.handle_layer_key(ui, key, e, config)
    else:
        host.write_code(ui, key, e.value)


def enable_layer(layer, activator, config):
    global active_layers
    active_layers[layer] = Layer(config.keymaps[layer], activator)


def disable_layer(ui, layer, config):
    global active_layers
    active_layers[layer] = None
    host.release_weak_keys(ui, config)


def handle_kbmap_toggle(ui, e, pos, config):
    try:
        key, layer_index = find_key(pos, config)

        if hasattr(key, 'type') and key.type == ActionType.KbmapToggleAction:
            key.handle(ui, e, config, pos)
            return True
    except LookupError:
        pass
    return False

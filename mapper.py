import importlib
import importlib.util

import click
from evdev import UInput, ecodes
from evdev.events import KeyEvent

import host
import keyboard
from log import debug

last_press_timestamps = []


def load_config(path):
    debug(f'loading config with path "{path}"')
    spec = importlib.util.spec_from_file_location('config', path)
    config = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(config)
    debug(f'config loaded')
    return config


def map(config_path, kb_name, ui_name='kbmap'):
    """
    Create virtual device with uinput_name that will remap keyboard events from device with name device_name using
    config_pth configuration.
    :param config_path: path to configuration file
    :param kb_name: source device name. This device will be grabbed
    :param ui_name: optional uinput device that will be created to write mapped events
    """

    config = load_config(config_path)

    global last_press_timestamps
    last_press_timestamps = [None for i in range(len(config.physical_layout))]

    kb = keyboard.get_device_by_name(kb_name)
    keyboard.grab(kb)

    ui = UInput.from_device(kb, name=ui_name)

    with ui:
        keyboard.listen_key_events(
            kb,
            lambda e: handle_event(e, kb, ui, config),
            False
        )


def handle_event(e, kb, ui, config):
    global last_press_timestamps

    debug(f'-------- handling {e} --------')
    pos = map_key_to_pos(e.code, config)
    if pos is None:
        return

    debug(f'key is {ecodes.KEY[e.code]} ({e.code}) at {pos}')

    keycode = config.keymaps[0][pos]

    if hasattr(keycode, 'type'):
        debug(f'key is mapped to action of type {keycode.type} at {pos}')
        keycode.handle(ui, e, config, last_press_timestamps[pos])
    else:
        debug(f'key is mapped to key: {ecodes.KEY[keycode]} ({keycode}) at {pos}')
        host.write_code(ui, keycode, e.value)

    update_timestamps(pos, e)


def map_key_to_pos(code, config):
    debug(f'looking for key {ecodes.KEY[code]} with code {code}')
    try:
        return config.physical_layout.index(code)
    except ValueError:
        click.echo(f'no key {ecodes.KEY[code]} in physical config')


def update_timestamps(pos, e):
    global last_press_timestamps

    new_value = e.timestamp() if e.value == KeyEvent.key_down else None
    last_press_timestamps[pos] = new_value
    debug(f'updated timestamp at [{pos}] to {new_value}')

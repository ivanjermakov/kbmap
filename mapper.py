import importlib
import importlib.util

import click
from evdev import UInput, ecodes

import host
import keyboard
from log import log


def load_config(path):
    log(f'loading config with path "{path}"')
    spec = importlib.util.spec_from_file_location('config', path)
    config = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(config)
    log(f'config loaded')
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
    log(f'handling {e}')
    pos = map_key_to_pos(e.code, config)
    if pos is None:
        return

    log(f'key is {ecodes.KEY[e.code]} ({e.code}) at {pos}')

    keycode = config.keymaps[0][pos]
    log(f'mapped keymap: {ecodes.KEY[keycode]} ({keycode}) at {pos}')

    host.write_code(ui, keycode, e.value)


def map_key_to_pos(code, config):
    log(f'looking for key {ecodes.KEY[code]} with code {code}')
    try:
        return config.physical_layout.index(code)
    except ValueError:
        click.echo(f'no key {ecodes.KEY[code]} in physical config')

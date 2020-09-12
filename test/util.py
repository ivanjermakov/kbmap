import time
from dataclasses import make_dataclass
from typing import *
from unittest.mock import Mock

from evdev.events import InputEvent, KeyEvent
from evdev.uinput import UInput

from kbmap import mapper


def generate_key_event(code, is_press):
    return InputEvent(int(time.time()), (time.time() * 1000000) % 1000000, 1, code,
                      KeyEvent.key_down if is_press else KeyEvent.key_up)


def create_ui(on_write):
    ui = UInput()
    ui.write = Mock(side_effect=on_write)
    return ui


def create_config(physical_layout, keymaps, tapping_term=200, kbmap_default_enabled=True):
    config = make_dataclass('config', [
        ('physical_layout', object),
        ('keymaps', object),
        ('tapping_term', int),
        ('kbmap_default_enabled', bool)
    ])
    config.physical_layout = physical_layout
    config.keymaps = keymaps
    config.tapping_term = tapping_term
    config.kbmap_default_enabled = kbmap_default_enabled
    return config


def simulate_keys(config, keys: Union[int, List[Tuple[int, bool]]]) -> List[Tuple[int, bool]]:
    write_keys = []

    def write(_, code, value):
        write_keys.append((code, bool(value)))

    ui = create_ui(write)
    ui.write = Mock(side_effect=write)

    mapper.init_mapper(config)

    for key in keys:
        if type(key) is int:
            time.sleep(key / 1000)
        else:
            mapper.handle_event(generate_key_event(key[0], key[1]), ui, config)

    return write_keys

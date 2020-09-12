"""
Used for operations on UInput, mainly on injecting events.
"""

from evdev import UInput, ecodes
from evdev.events import InputEvent, KeyEvent

from kbmap import mapper, key
from kbmap.config import Config
from kbmap.log import debug


def write(ui: UInput, e: InputEvent) -> None:
    """
    Inject event into specified UInput.
    """
    ui.write(ecodes.EV_KEY, e.code, e.value)
    ui.syn()


def write_code(ui: UInput, code: int, value: int) -> None:
    """
    Inject key event with code and value into specified UInput.
    """
    ui.write(ecodes.EV_KEY, code, value)
    ui.syn()


def write_tap(ui: UInput, code: int) -> None:
    """
    Write press and release.
    """
    write_press(ui, code)
    write_release(ui, code)
    ui.syn()


def write_press(ui: UInput, *codes: int) -> None:
    """
    Inject specified key codes into UInput with key_down.
    """
    for code in codes:
        ui.write(ecodes.EV_KEY, code, KeyEvent.key_down)
    ui.syn()


def write_release(ui: UInput, *codes: int) -> None:
    """
    Inject specified key codes into UInput with key_up.
    """
    for code in codes:
        ui.write(ecodes.EV_KEY, code, KeyEvent.key_up)
    ui.syn()


def release_weak_keys(ui: UInput, config: Config) -> None:
    """
    Release weak keys from all layers.
    Key is weak if it will cause key hold repeat without releasing.
    """
    for layer in range(len(config.keymaps)):
        for pos, is_pressed in enumerate(mapper.layers_keys_pressed[layer]):
            if is_pressed:
                keycode = config.keymaps[layer][pos]
                if keycode != key.KC_TRANSPARENT and key.is_weak(keycode):
                    debug(f'key {keycode} released')
                    write_release(ui, keycode)
                    mapper.layers_keys_pressed[layer][pos] = False


def release_layer_keys(ui: UInput, layer_index: int, config: Config) -> None:
    """
    Release weak keys from specified layer.
    """
    debug(f'releasing layer [{layer_index}] keys')
    for pos, is_pressed in enumerate(mapper.layers_keys_pressed[layer_index]):
        if is_pressed:
            keycode = config.keymaps[layer_index][pos]
            if keycode != key.KC_TRANSPARENT:
                debug(f'key {keycode} released')
                write_release(ui, keycode)
                mapper.layers_keys_pressed[layer_index][pos] = False

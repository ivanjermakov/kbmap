from evdev import *

from kbmap import mapper, key
from kbmap.log import debug


def write(ui, e):
    ui.write(ecodes.EV_KEY, e.code, e.value)
    ui.syn()


def write_code(ui, code, value):
    ui.write(ecodes.EV_KEY, code, value)
    ui.syn()


def write_tap(ui, code):
    write_press(ui, code)
    write_release(ui, code)
    ui.syn()


def write_press(ui, *codes):
    for code in codes:
        ui.write(ecodes.EV_KEY, code, KeyEvent.key_down)
    ui.syn()


def write_release(ui, *codes):
    for code in codes:
        ui.write(ecodes.EV_KEY, code, KeyEvent.key_up)
    ui.syn()


def release_layer_keys(ui, layer, config):
    debug(f'releasing layer [{layer}] keys')
    for pos, is_pressed in enumerate(mapper.layers_keys_pressed[layer]):
        if is_pressed:
            keycode = config.keymaps[layer][pos]
            if keycode != key.KC_TRANSPARENT:
                debug(f'key {keycode} released')
                write_release(ui, keycode)
                mapper.layers_keys_pressed[layer][pos] = False

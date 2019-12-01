from evdev import *


def transparent_write(device, e):
    device.write(e.type, e.code, e.value)
    device.syn()


def write_press(comb, ui, mapping):
    print(f'v: {mapping}')
    for m in mapping.source.modifiers:
        ui.write(comb.key.type, m, KeyEvent.key_up)
    for m in mapping.target.modifiers:
        ui.write(comb.key.type, m, KeyEvent.key_down)
    ui.write(comb.key.type, mapping.target.key, KeyEvent.key_down)
    ui.syn()


def write_release(comb, ui, mapping):
    print(f'^: {mapping}')
    ui.write(comb.key.type, mapping.target.key, KeyEvent.key_up)
    for m in mapping.target.modifiers:
        ui.write(comb.key.type, m, KeyEvent.key_up)
    ui.syn()


def release_keys(device, keyboard):
    active_keys = keyboard.active_keys()
    for k in active_keys:
        device.write(ecodes.EV_KEY, k, KeyEvent.key_up)

from evdev import *


def transparent_write(device, e):
    device.write(e.type, e.code, e.value)
    device.syn()


def write_press(e, device, keyboard, matched_mapping, remapped_code):
    for m in matched_mapping.source.modifiers:
        device.write(e.type, m, KeyEvent.key_up)
    for m in matched_mapping.target.modifiers:
        device.write(e.type, m, KeyEvent.key_down)
    device.write(e.type, remapped_code, KeyEvent.key_down)
    device.syn()


def write_release(e, device, keyboard, matched_mapping, remapped_code):
    device.write(e.type, remapped_code, KeyEvent.key_up)
    for m in matched_mapping.target.modifiers:
        device.write(e.type, m, KeyEvent.key_up)
    device.syn()


def release_keys(device, keyboard):
    active_keys = keyboard.active_keys()
    for k in active_keys:
        device.write(ecodes.EV_KEY, k, KeyEvent.key_up)
        keyboard.write(ecodes.EV_KEY, k, KeyEvent.key_up)

from evdev import *


def transparent_write(ui, e):
    ui.write(ecodes.EV_KEY, e.code, e.value)
    ui.syn()


def write_press(comb, ui, mapping):
    print(f'v: {mapping}')
    for m in mapping.source.modifiers:
        ui.write(ecodes.EV_KEY, m, KeyEvent.key_up)
    for m in mapping.target.modifiers:
        ui.write(ecodes.EV_KEY, m, KeyEvent.key_down)
    ui.write(ecodes.EV_KEY, mapping.target.key, KeyEvent.key_down)
    ui.syn()


def write_release(comb, ui, mapping):
    print(f'^: {mapping}')
    if mapping.target.key:
        ui.write(ecodes.EV_KEY, mapping.target.key, KeyEvent.key_up)
    for m in mapping.target.modifiers:
        ui.write(ecodes.EV_KEY, m, KeyEvent.key_up)
    ui.syn()


def release_keys(ui, kb):
    active_keys = kb.active_keys()
    for k in active_keys:
        ui.write(ecodes.EV_KEY, k, KeyEvent.key_up)
    ui.syn()

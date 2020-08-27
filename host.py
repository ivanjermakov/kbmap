from evdev import *


def write(ui, e):
    ui.write(ecodes.EV_KEY, e.code, e.value)
    ui.syn()


def write_code(ui, code, value):
    ui.write(ecodes.EV_KEY, code, value)
    ui.syn()


def write_press(e):
    ui.write(ecodes.EV_KEY, e.code, KeyEvent.key_down)
    ui.syn()


def write_release(e):
    ui.write(ecodes.EV_KEY, e.code, KeyEvent.key_up)
    ui.syn()


def release_keys(ui, kb):
    active_keys = kb.active_keys()
    for k in active_keys:
        ui.write(ecodes.EV_KEY, k, KeyEvent.key_up)
    ui.syn()

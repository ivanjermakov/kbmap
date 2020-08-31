import atexit

from evdev import *
from kbmap.log import debug


def get_device_by_name(device_name):
    try:
        devices = [InputDevice(fn) for fn in list_devices()]
        return [d for d in devices if device_name == d.name][0]
    except IndexError as e:
        raise type(e)(f'no device with name "{device_name}"')


def is_ctrl_z(e, keyboard):
    return e.code == ecodes.KEY_Z and ecodes.KEY_LEFTCTRL in keyboard.active_keys()


def listen_key_events(keyboard, event_handler, stoppable=True, stop_callback=None):
    for e in keyboard.read_loop():
        if e.type == ecodes.EV_KEY:

            # ignore HOLD events
            if e.value == KeyEvent.key_hold:
                continue

            # handle program stop
            if stoppable:
                if is_ctrl_z(e, keyboard):
                    if stop_callback:
                        stop_callback()
                    return

            event_handler(e)


def grab(keyboard):
    debug(f'grabbing keyboard {keyboard}')
    atexit.register(ungrab, keyboard)
    keyboard.grab()


def ungrab(keyboard):
    debug(f'ungrabbing keyboard {keyboard}')
    keyboard.ungrab()

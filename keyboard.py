import atexit

from evdev import *


def get_device_by_name(device_name):
    try:
        devices = [InputDevice(fn) for fn in list_devices()]
        return [d for d in devices if device_name == d.name][0]
    except IndexError as e:
        raise type(e)('no device with such name')


def is_ctrl_z(e, keyboard):
    return e.code == ecodes.KEY_Z and ecodes.KEY_LEFTCTRL in keyboard.active_keys()


def listen_key_events(keyboard, event_callback, stoppable=True, stop_callback=None):
    for e in keyboard.read_loop():
        if e.type == ecodes.EV_KEY:

            # handle program stop
            if stoppable:
                if is_ctrl_z(e, keyboard):
                    if stop_callback:
                        stop_callback()
                    return

            event_callback(e)


def grab(keyboard):
    atexit.register(keyboard.ungrab)
    keyboard.grab()

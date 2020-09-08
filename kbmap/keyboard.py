"""
Used for physical key device operations.
"""
import atexit

from evdev import *

from kbmap.log import debug


def get_device_by_name(device_name):
    """
    Find a device with a specified name.
    """
    try:
        devices = [InputDevice(fn) for fn in list_devices()]
        return [d for d in devices if device_name == d.name][0]
    except IndexError as e:
        raise type(e)(f'no device with name "{device_name}"')


def is_ctrl_z(e, keyboard):
    """
    Check whether event invokes ^z or not.
    """
    return e.code == ecodes.KEY_Z and ecodes.KEY_LEFTCTRL in keyboard.active_keys()


def listen_key_events(keyboard, event_handler, stoppable=True, stop_callback=None):
    """
    Subscribe for keyboard key events.
    Ignoring KeyEvent.key_hold events.
    Provide event handler to receive events.
    """
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
    """
    Grab keyboard to become a sole recipient of keyboard events.
    In case of program exit, keyboard will be ungrabbed.
    """
    debug(f'grabbing keyboard {keyboard}')
    atexit.register(ungrab, keyboard)
    keyboard.grab()


def ungrab(keyboard):
    """
    Ungrab the grabbed keyboard.
    """
    debug(f'ungrabbing keyboard {keyboard}')
    keyboard.ungrab()

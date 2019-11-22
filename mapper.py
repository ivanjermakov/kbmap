import atexit
import importlib
import importlib.util as iu

from evdev import KeyEvent, ecodes, InputDevice, list_devices, UInput

from combination import Combination


def _get_device_by_name(device_name):
    try:
        devices = [InputDevice(fn) for fn in list_devices()]
        return [d for d in devices if device_name == d.name][0]
    except IndexError as e:
        raise type(e)('no device with such name')


def _transparent_write(device, e):
    device.write(e.type, e.code, e.value)
    device.syn()


def _write_with_modifiers(e, device, matched_mapping, remapped_code):
    for m in matched_mapping.target.modifiers:
        device.write(e.type, m, KeyEvent.key_up)
    device.write(e.type, remapped_code, e.value)
    for m in matched_mapping.target.modifiers:
        device.write(e.type, m, KeyEvent.key_down)
    device.syn()


def _syn_write(e, device, remapped_code):
    device.write(e.type, remapped_code, e.value)
    device.syn()


def _is_ctrl_z(e, keyboard):
    return e.code == ecodes.KEY_Z and ecodes.KEY_LEFTCTRL in keyboard.active_keys()


def _release_keys(device, keyboard):
    active_keys = keyboard.active_keys()
    for k in active_keys:
        device.write(ecodes.EV_KEY, k, KeyEvent.key_up)
        keyboard.write(ecodes.EV_KEY, k, KeyEvent.key_up)


def _listen_key_events(keyboard, event_callback, stop_callback=None):
    for e in keyboard.read_loop():
        if e.type == ecodes.EV_KEY:

            # handle program stop
            if _is_ctrl_z(e, keyboard):
                if stop_callback:
                    stop_callback()
                return

            event_callback(e)


def _get_combination(e, keyboard):
    # work only with EV_KEY events
    if e.type != ecodes.EV_KEY:
        return

    return Combination(
        e.code,
        list(filter(lambda k: k != e.code, keyboard.active_keys()))
    )


def _get_matched_mappings(combination, mappings):
    return list(
        filter(lambda m: m.source.matching(combination), mappings)
    )


def _handle_event(e, mappings, keyboard, device):
    # key event
    if e.type == ecodes.EV_KEY:
        combination = _get_combination(e, keyboard)
        matched_mappings = _get_matched_mappings(combination, mappings)
        # if has any matched mappings
        if matched_mappings:
            # use first matched mapping
            matched_mapping = matched_mappings[0]
            remapped_code = matched_mapping.target.key
            # key press
            if e.value == KeyEvent.key_down:
                _write_with_modifiers(e, device, matched_mapping, remapped_code)
                return
            # key release
            if e.value == KeyEvent.key_up:
                _syn_write(e, device, remapped_code)
                device.syn()
                return

    # in case that incoming event is not suitable for mapping
    _transparent_write(device, e)


def apply(config_path, device_name, uinput_name='kbmap'):
    """
    Create virtual device with uinput_name that will remap keyboard events from device with name device_name using
    config_pth configuration.
    :param config_path: absolute or relative path to configuration file
    :param device_name: source device name. This device will be grabbed
    :param uinput_name: optional uinput device that will be created to write mapped events
    """
    mappings = load_mappings(config_path)

    keyboard = _get_device_by_name(device_name)
    atexit.register(keyboard.ungrab)
    keyboard.grab()

    device = UInput.from_device(keyboard, name=uinput_name)

    with device:
        _listen_key_events(
            keyboard,
            lambda e: _handle_event(e, mappings, keyboard, device),
            lambda: _release_keys(device, keyboard)
        )


def _test_event_handler(e, mappings, keyboard, callback):
    # display only KeyEvent.key_down
    if e.value != KeyEvent.key_down:
        return

    matched_mappings = _get_matched_mappings(
        _get_combination(e, keyboard),
        mappings
    )

    if not matched_mappings:
        return

    callback(matched_mappings)


def test(config_path, device_name, mapping_callback):
    mappings = load_mappings(config_path)

    keyboard = _get_device_by_name(device_name)
    atexit.register(keyboard.ungrab)
    keyboard.grab()

    _listen_key_events(
        keyboard,
        lambda e: _test_event_handler(e, mappings, keyboard, mapping_callback)
    )


def load_mappings(path):
    spec = iu.spec_from_file_location('config', path)
    config = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(config)
    return config.mappings

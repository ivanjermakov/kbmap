import atexit
import importlib
import importlib.util as iu

from evdev import KeyEvent, ecodes, InputDevice, list_devices, UInput

from combination import Combination


def _transparent(dev, e):
    dev.write(e.type, e.code, e.value)


def _load_mappings(path):
    spec = iu.spec_from_file_location("config", path)
    config = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(config)
    return config.mappings


def apply(config_path, device_name, uinput_name='kbmap'):
    mappings = _load_mappings(config_path)

    devices = [InputDevice(fn) for fn in list_devices()]
    keyboard = [d for d in devices if device_name == d.name][0]
    atexit.register(keyboard.ungrab)
    keyboard.grab()

    dev = UInput.from_device(keyboard, name=uinput_name)
    with dev:
        for e in keyboard.read_loop():
            # key event
            if e.type == ecodes.EV_KEY:
                combination = Combination(
                    e.code,
                    list(filter(lambda k: k != e.code, keyboard.active_keys()))
                )
                # print(f'combination: {combination}')
                matched_mappings = list(
                    filter(lambda m: m.source.matching(combination), mappings)
                )
                if e.code in map(lambda m: m.source.key, mappings) and matched_mappings:
                    matched_mapping = matched_mappings[0]
                    # print(f'matched mapping: {matched_mapping}')
                    remapped_code = matched_mapping.target.key
                    # key press
                    if e.value == KeyEvent.key_down:
                        for m in matched_mapping.target.modifiers:
                            dev.write(e.type, m, KeyEvent.key_up)
                        dev.write(e.type, remapped_code, e.value)
                        for m in matched_mapping.target.modifiers:
                            dev.write(e.type, m, KeyEvent.key_down)
                    # key release
                    elif e.value == KeyEvent.key_up:
                        dev.write(e.type, remapped_code, e.value)
                    # key hold
                    else:
                        _transparent(dev, e)
                else:
                    _transparent(dev, e)
            else:
                _transparent(dev, e)


apply("config.py", 'SINO WEALTH USB KEYBOARD')

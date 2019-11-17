import atexit

from evdev import KeyEvent, ecodes, InputDevice, list_devices, UInput

from combination import Combination
from mapping import Mapping


def _transparent(e):
    dev.write(e.type, e.code, e.value)


# TODO
def _release_all_keys(dev):
    for k in ecodes.keys:
        dev.write(ecodes.EV_KEY, k, KeyEvent.key_up)


mappings = [
    Mapping(Combination(ecodes.KEY_J, [ecodes.KEY_CAPSLOCK]), Combination(ecodes.KEY_LEFT)),
    Mapping(Combination(ecodes.KEY_K, [ecodes.KEY_CAPSLOCK]), Combination(ecodes.KEY_DOWN)),
    Mapping(Combination(ecodes.KEY_L, [ecodes.KEY_CAPSLOCK]), Combination(ecodes.KEY_RIGHT)),
    Mapping(Combination(ecodes.KEY_I, [ecodes.KEY_CAPSLOCK]), Combination(ecodes.KEY_UP)),
]

device_fn = '/dev/input/event7'
devices = [InputDevice(fn) for fn in list_devices()]
keyboard = [d for d in devices if device_fn in d.fn][0]
atexit.register(keyboard.ungrab)
keyboard.grab()

dev = UInput.from_device(keyboard, name='kbmap')
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
                    _transparent(e)
            else:
                _transparent(e)
        else:
            _transparent(e)

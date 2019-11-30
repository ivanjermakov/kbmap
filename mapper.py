import atexit
import importlib
import importlib.util as iu

from evdev import KeyEvent, ecodes, InputDevice, list_devices, UInput

from combination import Combination
from mapping import Mapping


class Mapper:
    def __init__(self, config_path, device_name, uinput_name='kbmap'):
        self.config_path = config_path
        self.mappings = self.load_mappings(config_path)
        self.modifiers = self._get_modifiers()
        self.device_name = device_name
        self.keyboard = self._get_device_by_name(device_name)
        self.device = UInput.from_device(self.keyboard, name=uinput_name)

    def apply(self):
        """
        Create virtual device with uinput_name that will remap keyboard events from device with name device_name using
        config_pth configuration.
        """
        atexit.register(self.keyboard.ungrab)
        self.keyboard.grab()

        with self.device:
            self._listen_key_events(
                self.keyboard,
                lambda e: self._handle_event(e),
                False
            )

    def test(self, mapping_callback):
        atexit.register(self.keyboard.ungrab)
        self.keyboard.grab()

        self._listen_key_events(
            self.keyboard,
            lambda e: self._test_event_handler(e, mapping_callback)
        )

    @staticmethod
    def load_mappings(path):
        spec = iu.spec_from_file_location('config', path)
        config = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(config)
        return config.mappings

    def _get_modifiers(self):
        flatten = lambda l: [item for sublist in l for item in sublist]

        return list(set(
            flatten(
                map(lambda m: m.source.modifiers, self.mappings)
            )
        ))

    def _get_device_by_name(self, device_name):
        try:
            devices = [InputDevice(fn) for fn in list_devices()]
            return [d for d in devices if device_name == d.name][0]
        except IndexError as e:
            raise type(e)('no device with such name')

    def _transparent_write(self, e):
        self.device.write(e.type, e.code, e.value)
        self.device.syn()

    def _write_with_modifiers(self, e, matched_mapping, remapped_code):
        for m in matched_mapping.target.modifiers:
            self.device.write(e.type, m, KeyEvent.key_up)
        self.device.write(e.type, remapped_code, e.value)
        for m in matched_mapping.target.modifiers:
            self.device.write(e.type, m, KeyEvent.key_down)
        self.device.syn()

    def _write(self, e, remapped_code):
        self.device.write(e.type, remapped_code, e.value)
        self.device.syn()

    def _is_ctrl_z(self, e, keyboard):
        return e.code == ecodes.KEY_Z and ecodes.KEY_LEFTCTRL in keyboard.active_keys()

    def _release_keys(self, device, keyboard):
        active_keys = keyboard.active_keys()
        for k in active_keys:
            device.write(ecodes.EV_KEY, k, KeyEvent.key_up)
            keyboard.write(ecodes.EV_KEY, k, KeyEvent.key_up)

    def _listen_key_events(self, keyboard, event_callback, stoppable=True, stop_callback=None):
        for e in keyboard.read_loop():
            if e.type == ecodes.EV_KEY:
                # handle program stop
                if stoppable:
                    if self._is_ctrl_z(e, keyboard):
                        if stop_callback:
                            stop_callback()
                        return
                event_callback(e)
            else:
                self._transparent_write(e)

    def _handle_event(self, e):
        combination = self._get_combination(e, self.keyboard)
        matched_mappings = self._get_matched_mappings(combination, self.mappings)
        # if has any matched mappings
        if matched_mappings:
            # use first matched mapping
            matched_mapping = matched_mappings[0]
            remapped_code = matched_mapping.target.key
            # key press
            if e.value == KeyEvent.key_down:
                self._write_with_modifiers(e, matched_mapping, remapped_code)
                return
            # key release
            if e.value == KeyEvent.key_up:
                self._write(e, remapped_code)
                self.device.syn()
                return

        # write unmatched
        self._transparent_write(e)

    def _get_combination(self, e, keyboard):
        # work only with EV_KEY events
        if e.type != ecodes.EV_KEY:
            return

        return Combination(
            e.code,
            list(filter(lambda k: k != e.code, keyboard.active_keys()))
        )

    def _get_matched_mappings(self, combination, mappings):
        return list(
            filter(lambda m: m.source.matching(combination), mappings)
        )

    def _test_event_handler(self, e, callback):
        # display only KeyEvent.key_down
        # if e.value != KeyEvent.key_down:
        #     return
        print(KeyEvent(e))
        combination = self._get_combination(e, self.keyboard)

        matched_mappings = self._get_matched_mappings(
            combination,
            self.mappings
        )

        if not matched_mappings:
            return callback([Mapping(combination, combination)])

        callback(matched_mappings)

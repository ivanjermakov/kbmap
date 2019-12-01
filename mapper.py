import importlib
import importlib.util

from evdev import KeyEvent, UInput

import keyboard
import uinput
from combination import Combination
from mapping import Mapping

LAST_MAPPING = None


def _get_matched_mappings(combination, mappings):
    return list(
        filter(lambda m: m.source.matching(combination), mappings)
    )


def _handle_event(e, mappings, kb, ui):
    global LAST_MAPPING
    print(f'last mapping: {LAST_MAPPING}')

    combination = Combination.from_event(e, kb)
    matched_mappings = _get_matched_mappings(combination, mappings)

    # # if last recent mapping is no longer mapped
    # if LAST_MAPPING and LAST_MAPPING not in matched_mappings:
    #     # release that mapping
    #     print(f'release mapping: {LAST_MAPPING}')
    #     uinput.write_release(combination, ui, LAST_MAPPING)

    # if has any matched mappings
    if matched_mappings:
        # use first matched mapping
        mapping = matched_mappings[0]
        LAST_MAPPING = mapping

        if not mapping.target.key:
            return

        # key press
        if e.value == KeyEvent.key_down:
            uinput.write_press(combination, ui, mapping)
            return
        # key release
        if e.value == KeyEvent.key_up:
            uinput.write_release(combination, ui, mapping)
            return
    else:
        uinput.transparent_write(ui, e)
        LAST_MAPPING = None


def _test_event_handler(e, mappings, kb, callback):
    # display only KeyEvent.key_down
    if e.value != KeyEvent.key_down:
        return

    combination = Combination.from_event(e, kb)

    matched_mappings = _get_matched_mappings(combination, mappings)

    if not matched_mappings:
        return callback([Mapping(combination, combination)])

    callback(matched_mappings)


def load_mappings(path):
    spec = importlib.util.spec_from_file_location('config', path)
    config = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(config)
    return config.mappings


def apply(config_path, kb_name, ui_name='kbmap'):
    """
    Create virtual device with uinput_name that will remap keyboard events from device with name device_name using
    config_pth configuration.
    :param config_path: absolute or relative path to configuration file
    :param kb_name: source device name. This device will be grabbed
    :param ui_name: optional uinput device that will be created to write mapped events
    """
    mappings = load_mappings(config_path)

    kb = keyboard.get_device_by_name(kb_name)
    keyboard.grab(kb)

    device = UInput.from_device(kb, name=ui_name)

    with device:
        keyboard.listen_key_events(
            kb,
            lambda e: _handle_event(e, mappings, kb, device),
            False
        )


def test(config_path, kb_name, mapping_callback):
    mappings = load_mappings(config_path)

    kb = keyboard.get_device_by_name(kb_name)
    keyboard.grab(kb)

    keyboard.listen_key_events(
        kb,
        lambda e: _test_event_handler(e, mappings, kb, mapping_callback)
    )

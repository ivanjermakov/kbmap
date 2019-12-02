import importlib
import importlib.util

from evdev import KeyEvent, UInput

import keyboard
import uinput
from combination import Combination
from mapping import Mapping


def _get_matched_mappings(combination, mappings):
    return list(
        filter(lambda m: m.source.matching(combination), mappings)
    )


def _get_matched_subset_mappings(combination, mappings):
    return list(
        filter(lambda m: m.source.matching_subset(combination), mappings)
    )


def _handle_event(e, mappings, kb, ui):
    combination = Combination.from_event(e, kb)

    if e.value == KeyEvent.key_down:
        matched_mappings = _get_matched_mappings(combination, mappings)
        if matched_mappings:
            uinput.write_press(combination, ui, matched_mappings[0])
            return

    if e.value == KeyEvent.key_up:
        matched_subset = _get_matched_subset_mappings(combination, mappings)
        if matched_subset:
            uinput.write_release(combination, ui, matched_subset[0])
            return

    uinput.transparent_write(ui, e)


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

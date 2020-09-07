from kbmap.key import *
from test.test_action import ActionTest
from test.util import *


class ModTapActionTest(ActionTest):

    def test_mod_tap_action_tap(self):
        self.assert_mapping(
            create_config(
                [KC_A, KC_B, KC_C],
                [
                    [MT(KC_A, KC_LSFT), KC_B, KC_C]
                ]
            ),
            [(KC_A, True), (KC_A, False), (KC_B, True), (KC_B, False)],
            [(KC_LSFT, True), (KC_LSFT, False), (KC_A, True), (KC_A, False), (KC_B, True), (KC_B, False)]
        )

    def test_mod_tap_action_tap_slip(self):
        self.assert_mapping(
            create_config(
                [KC_A, KC_B, KC_C],
                [
                    [MT(KC_A, KC_LSFT), KC_B, KC_C]
                ]
            ),
            [(KC_A, True), (KC_B, True), (KC_A, False)],
            [(KC_LSFT, True), (KC_B, True), (KC_B, False), (KC_LSFT, False)]
        )

    def test_mod_tap_action_hold(self):
        self.assert_mapping(
            create_config(
                [KC_A, KC_B, KC_C],
                [
                    [MT(KC_A, KC_LSFT), KC_B, KC_C]
                ]
            ),
            [(KC_A, True), (KC_B, True), (KC_B, False), (KC_A, False)],
            [(KC_LSFT, True), (KC_B, True), (KC_B, False), (KC_LSFT, False)]
        )

    def test_mod_tap_short_hold(self):
        self.assert_mapping(
            create_config(
                [KC_A, KC_B, KC_C],
                [
                    [MT(KC_A, KC_LSFT), KC_B, KC_C]
                ]
            ),
            [(KC_A, True), 100, (KC_A, False)],
            [(KC_LSFT, True), (KC_LSFT, False), (KC_A, True), (KC_A, False)]
        )

    def test_mod_tap_action_long_hold(self):
        self.assert_mapping(
            create_config(
                [KC_A, KC_B, KC_C],
                [
                    [MT(KC_A, KC_LSFT), KC_B, KC_C]
                ]
            ),
            [(KC_A, True), 300, (KC_A, False)],
            [(KC_LSFT, True), (KC_LSFT, False)]
        )

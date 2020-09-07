from unittest import skip

from kbmap.key import *
from test.test_action import ActionTest
from test.util import *


class LayerTapActionTest(ActionTest):

    def test_layer_tap(self):
        self.assert_mapping(
            create_config(
                [KC_A, KC_B, KC_C],
                [
                    [LT(1, KC_A), KC_B, KC_C],
                    [KC_TRNS, KC_D, KC_TRNS]
                ]
            ),
            [(KC_A, True), (KC_A, False), (KC_B, True), (KC_B, False)],
            [(KC_A, True), (KC_A, False), (KC_B, True), (KC_B, False)]
        )

    def test_layer_tap_slip(self):
        self.assert_mapping(
            create_config(
                [KC_A, KC_B, KC_C],
                [
                    [LT(1, KC_A), KC_B, KC_C],
                    [KC_TRNS, KC_D, KC_TRNS]
                ]
            ),
            [(KC_A, True), (KC_B, True), (KC_A, False)],
            [(KC_D, True), (KC_D, False)]
        )

    def test_layer_tap_hold(self):
        self.assert_mapping(
            create_config(
                [KC_A, KC_B, KC_C],
                [
                    [LT(1, KC_A), KC_B, KC_C],
                    [KC_TRNS, KC_D, KC_TRNS]
                ]
            ),
            [(KC_A, True), (KC_B, True), (KC_B, False), (KC_A, False)],
            [(KC_D, True), (KC_D, False)]
        )

    def test_layer_tap_short_hold(self):
        self.assert_mapping(
            create_config(
                [KC_A, KC_B, KC_C],
                [
                    [LT(1, KC_A), KC_B, KC_C],
                    [KC_TRNS, KC_D, KC_TRNS]
                ]
            ),
            [(KC_A, True), 100, (KC_A, False)],
            [(KC_A, True), (KC_A, False)]
        )

    def test_layer_tap_long_hold(self):
        self.assert_mapping(
            create_config(
                [KC_A, KC_B, KC_C],
                [
                    [LT(1, KC_A), KC_B, KC_C],
                    [KC_TRNS, KC_D, KC_TRNS]
                ]
            ),
            [(KC_A, True), 300, (KC_A, False)],
            []
        )

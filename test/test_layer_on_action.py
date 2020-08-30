from kbmap import log
from kbmap.key import *
from test.test_action import ActionTest
from test.util import *


class LayerOnAction(ActionTest):

    def test_layer_on(self):
        self.assert_mapping(
            create_config(
                [KC_A, KC_B, KC_C],
                [
                    [MO(1), KC_B, KC_C],
                    [KC_TRNS, KC_A, KC_TRNS]
                ]
            ),
            [(KC_A, True), (KC_A, False)],
            []
        )

    def test_layer_on_keypress(self):
        self.assert_mapping(
            create_config(
                [KC_A, KC_B, KC_C],
                [
                    [MO(1), KC_B, KC_C],
                    [KC_TRNS, KC_D, KC_TRNS]
                ]
            ),
            [(KC_A, True), (KC_B, True), (KC_B, False), (KC_A, False)],
            [(KC_D, True), (KC_D, False)]
        )

    def test_layer_on_keypress_slip(self):
        self.assert_mapping(
            create_config(
                [KC_A, KC_B, KC_C],
                [
                    [MO(1), KC_B, KC_C],
                    [KC_TRNS, KC_D, KC_TRNS]
                ]
            ),
            [(KC_A, True), (KC_B, True), (KC_A, False)],
            [(KC_D, True), (KC_D, False)]
        )

    def test_layer_on_transparent(self):
        self.assert_mapping(
            create_config(
                [KC_A, KC_B, KC_C],
                [
                    [MO(1), KC_B, KC_C],
                    [KC_TRNS, KC_D, KC_TRNS]
                ]
            ),
            [(KC_A, True), (KC_C, True), (KC_C, False), (KC_A, False)],
            [(KC_C, True), (KC_C, False)]
        )

    def test_layer_on_transparent_slip(self):
        self.assert_mapping(
            create_config(
                [KC_A, KC_B, KC_C],
                [
                    [MO(1), KC_B, KC_C],
                    [KC_TRNS, KC_D, KC_TRNS]
                ]
            ),
            [(KC_A, True), (KC_C, True), (KC_A, False)],
            [(KC_C, True), (KC_C, False)]
        )

    def test_layer_on_nested(self):
        self.assert_mapping(
            create_config(
                [KC_A, KC_B, KC_C],
                [
                    [MO(1), KC_B, KC_C],
                    [KC_TRNS, MO(2), KC_TRNS],
                    [KC_TRNS, KC_TRNS, KC_D]
                ]
            ),
            [(KC_A, True), (KC_B, True), (KC_C, True), (KC_C, False), (KC_B, False), (KC_A, False)],
            [(KC_D, True), (KC_D, False)]
        )

    def test_layer_on_nested_slip(self):
        self.assert_mapping(
            create_config(
                [KC_A, KC_B, KC_C],
                [
                    [MO(1), KC_B, KC_C],
                    [KC_TRNS, MO(2), KC_TRNS],
                    [KC_TRNS, KC_TRNS, KC_D]
                ]
            ),
            [(KC_A, True), (KC_B, True), (KC_C, True), (KC_B, False), (KC_A, False)],
            [(KC_D, True), (KC_D, False)]
        )

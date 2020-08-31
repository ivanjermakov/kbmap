from kbmap.key import *
from test.test_action import ActionTest
from test.util import *


class LayerToggleAction(ActionTest):

    def test_layer_toggle(self):
        self.assert_mapping(
            create_config(
                [KC_A, KC_B, KC_C],
                [
                    [TG(1), KC_B, KC_C],
                    [KC_TRNS, KC_A, KC_TRNS]
                ]
            ),
            [(KC_A, True), (KC_A, False), (KC_A, True), (KC_A, False)],
            []
        )

    def test_layer_keypress(self):
        self.assert_mapping(
            create_config(
                [KC_A, KC_B, KC_C],
                [
                    [TG(1), KC_B, KC_C],
                    [KC_TRNS, KC_D, KC_TRNS]
                ]
            ),
            [(KC_A, True), (KC_A, False), (KC_B, True), (KC_B, False), (KC_A, True), (KC_A, False), (KC_B, True), (KC_B, False)],
            [(KC_D, True), (KC_D, False), (KC_B, True), (KC_B, False)]
        )

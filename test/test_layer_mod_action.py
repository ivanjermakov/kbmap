from kbmap.key import *
from test.test_action import ActionTest
from test.util import *


class LayerModActionTest(ActionTest):

    def test_layer_mod(self):
        self.assert_mapping(
            create_config(
                [KC_A, KC_B, KC_C],
                [
                    [LM(1, KC_LSFT), KC_B, KC_C],
                    [KC_TRNS, KC_D, KC_TRNS]
                ]
            ),
            [(KC_A, True), (KC_A, False)],
            []
        )

    def test_layer_mod_hold(self):
        self.assert_mapping(
            create_config(
                [KC_A, KC_B, KC_C],
                [
                    [LM(1, KC_LSFT), KC_B, KC_C],
                    [KC_TRNS, KC_D, KC_TRNS]
                ]
            ),
            [(KC_A, True), (KC_B, True), (KC_B, False), (KC_A, False)],
            [(KC_LSFT, True), (KC_D, True), (KC_D, False), (KC_LSFT, False)]
        )

    def test_layer_mod_hold_trans(self):
        self.assert_mapping(
            create_config(
                [KC_A, KC_B, KC_C],
                [
                    [LM(1, KC_LSFT), KC_B, KC_C],
                    [KC_TRNS, KC_D, KC_TRNS]
                ]
            ),
            [(KC_A, True), (KC_C, True), (KC_C, False), (KC_A, False)],
            [(KC_C, True), (KC_C, False)]
        )

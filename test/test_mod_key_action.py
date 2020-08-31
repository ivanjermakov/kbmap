from kbmap.key import *
from test.test_action import ActionTest
from test.util import *


class ModKeyActionTest(ActionTest):

    def test_mod_key_action(self):
        self.assert_mapping(
            create_config(
                [KC_A, KC_B, KC_C],
                [
                    [MK(KC_A, KC_LSFT), KC_B, KC_C]
                ]
            ),
            [(KC_A, True), (KC_A, False)],
            [(KC_LSHIFT, True), (KC_A, True), (KC_A, False), (KC_LSHIFT, False)]
        )

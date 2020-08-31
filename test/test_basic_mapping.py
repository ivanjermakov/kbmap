from kbmap.key import *
from test.test_action import ActionTest
from test.util import *


class BasicMappingTest(ActionTest):

    def test_basic_mapping_same_keys(self):
        self.assert_mapping(
            create_config(
                [KC_A, KC_B, KC_C],
                [
                    [KC_A, KC_B, KC_C]
                ]
            ),
            [(KC_A, True), (KC_A, False)],
            [(KC_A, True), (KC_A, False)]
        )

    def test_basic_mapping_other_keys(self):
        self.assert_mapping(
            create_config(
                [KC_A, KC_B, KC_C],
                [
                    [KC_B, KC_C, KC_A]
                ]
            ),
            [(KC_A, True), (KC_A, False)],
            [(KC_B, True), (KC_B, False)]
        )

    def test_kc_no_mapping(self):
        self.assert_mapping(
            create_config(
                [KC_A, KC_B, KC_C],
                [
                    [KC_NO, KC_B, KC_C]
                ]
            ),
            [(KC_A, True), (KC_A, False)],
            [(KC_NO, True), (KC_NO, False)]
        )

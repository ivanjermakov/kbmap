from kbmap.key import *
from test.test_action import ActionTest
from test.util import *


class KbmapToggleActionTest(ActionTest):

    def test_kbmap_toggle(self):
        self.assert_mapping(
            create_config(
                [KC_A, KC_B, KC_C],
                [
                    [KT(), KC_D, KC_C]
                ]
            ),
            [(KC_B, True), (KC_B, False), (KC_A, True), (KC_A, False), (KC_B, True), (KC_B, False)],
            [(KC_D, True), (KC_D, False), (KC_B, True), (KC_B, False)]
        )

    def test_kbmap_toggle_from_disabled(self):
        self.assert_mapping(
            create_config(
                [KC_A, KC_B, KC_C],
                [
                    [KT(), KC_D, KC_C]
                ],
                kbmap_default_enabled=False
            ),
            [(KC_B, True), (KC_B, False), (KC_A, True), (KC_A, False), (KC_B, True), (KC_B, False)],
            [(KC_B, True), (KC_B, False), (KC_D, True), (KC_D, False)]
        )

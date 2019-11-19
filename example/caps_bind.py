from keys import *

from mapping import Mapping

mappings = Mapping.bind(
    [CAPSLOCK],
    [
        J, K, L, I, U, O, E
    ],
    [],
    [
        LEFT, DOWN, RIGHT, UP, BACKSPACE, DELETE, ESC
    ]
)

from keys import *

from mapping import Mapping

mappings = Mapping.bind(
    [CAPSLOCK],
    [
        ESC, F1, F2, F3, F4, F5, F6, F7, F8, F9, F10, F11, F12, SYSRQ, SCROLLLOCK, PAUSE,
        GRAVE, K1, K2, K3, K4, K5, K6, K7, K8, K9, K0, MINUS, EQUAL, BACKSPACE, INSERT, HOME, PAGEUP,
        TAB, Q, W, E, R, T, Y, U, I, O, P, LEFTBRACE, RIGHTBRACE, BACKSLASH, DELETE, END, PAGEDOWN,
        CAPSLOCK, A, S, D, F, G, H, J, K, L, SEMICOLON, APOSTROPHE, ENTER,
        LEFTSHIFT, Z, X, C, V, B, N, M, COMMA, DOT, SLASH, RIGHTSHIFT, UP,
        LEFTCTRL, LEFTMETA, LEFTALT, SPACE, RIGHTALT, COMPOSE, RIGHTCTRL, LEFT, DOWN, RIGHT,
    ],
    [],
    [
        NO, NO, NO, NO, NO, NO, NO, NO, NO, NO, NO, NO, NO, NO, NO, NO,
        NO, NO, NO, NO, NO, NO, NO, NO, NO, NO, NO, NO, NO, NO, NO, NO, NO,
        NO, NO, NO, ESC, NO, NO, NO, BACKSPACE, UP, DELETE, NO, NO, NO, NO, NO, NO, NO,
        NO, NO, NO, NO, NO, NO, LEFT, DOWN, RIGHT, NO, NO, NO, NO,
        NO, NO, NO, NO, NO, NO, NO, NO, NO, NO, NO, NO, NO,
        NO, NO, NO, NO, NO, NO, NO, NO, NO, NO,
    ]
)

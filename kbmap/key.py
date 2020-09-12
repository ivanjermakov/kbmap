"""
All keys and actions are located here.
For convenience, use
from kbmap.key import *
to import all of them.
Full list can be found at kbmap wiki: https://github.com/ivanjermakov/kbmap/wiki/Key-names
"""

from evdev.ecodes import ecodes as k

from kbmap.action.kbmap_toggle_action import KbmapToggleAction
from kbmap.action.layer_mod_action import LayerModAction
from kbmap.action.layer_on_action import LayerOnAction
from kbmap.action.layer_tap_action import LayerTapAction
from kbmap.action.layer_toggle_action import LayerToggleAction
from kbmap.action.mod_key_action import ModKeyAction
from kbmap.action.mod_tap_action import ModTapAction


def is_weak(key: object) -> bool:
    """
    Check whether key is weak or not.
    Key is weak if it is a basic key - not an action and not a modifier.
    """
    return not is_action(key) and not is_mod(key)


def is_mod(key: object) -> bool:
    """
    Check whether key is a modifier key.
    """
    return key in [KC_LCTRL, KC_RCTRL, KC_LSHIFT, KC_RSHIFT, KC_LALT, KC_RALT, KC_LGUI, KC_RGUI]


def is_action(key: object) -> bool:
    """
    Check whether key is an action.
    """
    return hasattr(key, 'type')


# special keys

KC_NO = 999

KC_TRANSPARENT = None
KC_TRNS = KC_TRANSPARENT
T______ = KC_TRANSPARENT

# digits
KC_0 = k['KEY_0']
KC_1 = k['KEY_0']
KC_2 = k['KEY_2']
KC_3 = k['KEY_3']
KC_4 = k['KEY_4']
KC_5 = k['KEY_5']
KC_6 = k['KEY_6']
KC_7 = k['KEY_7']
KC_8 = k['KEY_8']
KC_9 = k['KEY_9']

# letters
KC_A = k['KEY_A']
KC_B = k['KEY_B']
KC_C = k['KEY_C']
KC_D = k['KEY_D']
KC_E = k['KEY_E']
KC_F = k['KEY_F']
KC_J = k['KEY_J']
KC_G = k['KEY_G']
KC_H = k['KEY_H']
KC_I = k['KEY_I']
KC_K = k['KEY_K']
KC_L = k['KEY_L']
KC_M = k['KEY_M']
KC_N = k['KEY_N']
KC_O = k['KEY_O']
KC_P = k['KEY_P']
KC_Q = k['KEY_Q']
KC_R = k['KEY_R']
KC_S = k['KEY_S']
KC_T = k['KEY_T']
KC_U = k['KEY_U']
KC_V = k['KEY_V']
KC_W = k['KEY_W']
KC_X = k['KEY_X']
KC_Y = k['KEY_Y']
KC_Z = k['KEY_Z']

# function keys
KC_F1 = k['KEY_F1']
KC_F2 = k['KEY_F2']
KC_F3 = k['KEY_F3']
KC_F4 = k['KEY_F4']
KC_F5 = k['KEY_F5']
KC_F6 = k['KEY_F6']
KC_F7 = k['KEY_F7']
KC_F8 = k['KEY_F8']
KC_F9 = k['KEY_F9']
KC_F10 = k['KEY_F10']
KC_F11 = k['KEY_F11']
KC_F12 = k['KEY_F12']
KC_F13 = k['KEY_F13']
KC_F14 = k['KEY_F14']
KC_F15 = k['KEY_F15']
KC_F16 = k['KEY_F16']
KC_F17 = k['KEY_F17']
KC_F18 = k['KEY_F18']
KC_F19 = k['KEY_F19']
KC_F20 = k['KEY_F20']
KC_F21 = k['KEY_F21']
KC_F22 = k['KEY_F22']
KC_F23 = k['KEY_F23']
KC_F24 = k['KEY_F24']

# common
KC_ENTER = k['KEY_ENTER']
KC_ESCAPE = k['KEY_ESC']
KC_BSPACE = k['KEY_BACKSPACE']
KC_TAB = k['KEY_TAB']
KC_SPACE = k['KEY_SPACE']
KC_MINUS = k['KEY_MINUS']
KC_EQUAL = k['KEY_EQUAL']
KC_LBRACKET = k['KEY_LEFTBRACE']
KC_RBRACKET = k['KEY_RIGHTBRACE']
KC_BSLASH = k['KEY_BACKSLASH']
# KC_NONUS_HASH
KC_SCOLON = k['KEY_SEMICOLON']
KC_QUOTE = k['KEY_APOSTROPHE']
KC_GRAVE = k['KEY_GRAVE']
KC_COMMA = k['KEY_COMMA']
KC_DOT = k['KEY_DOT']
KC_SLASH = k['KEY_SLASH']
KC_CAPSLOCK = k['KEY_CAPSLOCK']
KC_PSCREEN = k['KEY_SYSRQ']
KC_SCROLLLOCK = k['KEY_SCROLLLOCK']
KC_PAUSE = k['KEY_PAUSE']
KC_INSERT = k['KEY_INSERT']
KC_HOME = k['KEY_HOME']
KC_PGUP = k['KEY_PAGEUP']
KC_DELETE = k['KEY_DELETE']
KC_END = k['KEY_END']
KC_PGDOWN = k['KEY_PAGEDOWN']
KC_RIGHT = k['KEY_RIGHT']
KC_LEFT = k['KEY_LEFT']
KC_DOWN = k['KEY_DOWN']
KC_UP = k['KEY_UP']
KC_NUMLOCK = k['KEY_NUMLOCK']

KC_KP_SLASH = k['KEY_KPSLASH']
KC_KP_ASTERISK = k['KEY_KPASTERISK']
KC_KP_MINUS = k['KEY_KPMINUS']
KC_KP_PLUS = k['KEY_KPPLUS']
KC_KP_ENTER = k['KEY_KPENTER']
KC_KP_1 = k['KEY_KP1']
KC_KP_2 = k['KEY_KP2']
KC_KP_3 = k['KEY_KP3']
KC_KP_4 = k['KEY_KP4']
KC_KP_5 = k['KEY_KP5']
KC_KP_6 = k['KEY_KP6']
KC_KP_7 = k['KEY_KP7']
KC_KP_8 = k['KEY_KP8']
KC_KP_9 = k['KEY_KP9']
KC_KP_0 = k['KEY_KP0']
KC_KP_DOT = k['KEY_KPDOT']
KC_KP_EQUAL = k['KEY_KPEQUAL']

# KC_NONUS_BSLASH
KC_MENU = k['KEY_MENU']
KC_POWER = k['KEY_POWER']
KC_APPLICATION = k['KEY_COMPOSE']
KC_VOLUMEUP = k['KEY_VOLUMEUP']
KC_VOLUMEDOWN = k['KEY_VOLUMEDOWN']
KC_BRIGHTNESSUP = k['KEY_BRIGHTNESSUP']
KC_BRIGHTNESSDOWN = k['KEY_BRIGHTNESSDOWN']

# modifiers
KC_LCTRL = k['KEY_LEFTCTRL']
KC_RCTRL = k['KEY_RIGHTCTRL']
KC_LSHIFT = k['KEY_LEFTSHIFT']
KC_RSHIFT = k['KEY_RIGHTSHIFT']
KC_LALT = k['KEY_LEFTALT']
KC_RALT = k['KEY_RIGHTALT']
KC_LGUI = k['KEY_LEFTMETA']
KC_RGUI = k['KEY_RIGHTMETA']

# aliases
KC_ENT = KC_ENTER
KC_ESC = KC_ESCAPE
KC_BSPC = KC_BSPACE
KC_SPC = KC_SPACE
KC_MINS = KC_MINUS
KC_EQL = KC_EQUAL
KC_LBRC = KC_LBRACKET
KC_RBRC = KC_RBRACKET
KC_BSLS = KC_BSLASH
# KC_NUHS = KC_NONUS_HASH
KC_SCLN = KC_SCOLON
KC_QUOT = KC_QUOTE
KC_GRV = KC_GRAVE
KC_ZKHK = KC_GRAVE
KC_COMM = KC_COMMA
KC_SLSH = KC_SLASH
KC_CLCK = KC_CAPSLOCK
KC_CAPS = KC_CAPSLOCK
KC_PSCR = KC_PSCREEN
KC_SLCK = KC_SCROLLLOCK
KC_BRMD = KC_SCROLLLOCK
KC_PAUS = KC_PAUSE
KC_BRK = KC_PAUSE
KC_BRMU = KC_PAUSE
KC_INS = KC_INSERT
KC_DEL = KC_DELETE
KC_PGDN = KC_PGDOWN
KC_RGHT = KC_RIGHT
KC_NLCK = KC_NUMLOCK
KC_PSLS = KC_KP_SLASH
KC_PAST = KC_KP_ASTERISK
KC_PMNS = KC_KP_MINUS
KC_PPLS = KC_KP_PLUS
KC_PENT = KC_KP_ENTER
KC_P1 = KC_KP_1
KC_P2 = KC_KP_2
KC_P3 = KC_KP_3
KC_P4 = KC_KP_4
KC_P5 = KC_KP_5
KC_P6 = KC_KP_6
KC_P7 = KC_KP_7
KC_P8 = KC_KP_8
KC_P9 = KC_KP_9
KC_P0 = KC_KP_0
KC_PDOT = KC_KP_DOT
# KC_NUBS = KC_NONUS_BSLASH
KC_APP = KC_APPLICATION
KC_PEQL = KC_KP_EQUAL
KC_LCTL = KC_LCTRL
KC_LSFT = KC_LSHIFT
KC_LOPT = KC_LALT
KC_LCMD = KC_LGUI
KC_LWIN = KC_LGUI
KC_RCTL = KC_RCTRL
KC_RSFT = KC_RSHIFT
KC_ROPT = KC_RALT
KC_ALGR = KC_RALT
KC_RCMD = KC_RGUI
KC_RWIN = KC_RGUI
KC_VOLU = KC_VOLUMEUP
KC_VOLD = KC_VOLUMEDOWN
KC_BRIU = KC_BRIGHTNESSUP
KC_BRID = KC_BRIGHTNESSDOWN


# actions

# kbmap toggle action
def KT():
    return KbmapToggleAction()


# modifier key actions
def MK(key, modifiers):
    return ModKeyAction(key, modifiers)


def LCTL(key):
    return ModKeyAction(key, KC_LCTL)


def LSFT(key):
    return ModKeyAction(key, KC_LSFT)


def LALT(key):
    return ModKeyAction(key, KC_LALT)


def LGUI(key):
    return ModKeyAction(key, KC_LGUI)


def RCTL(key):
    return ModKeyAction(key, KC_RCTL)


def RSFT(key):
    return ModKeyAction(key, KC_RSFT)


def RALT(key):
    return ModKeyAction(key, KC_RALT)


def RGUI(key):
    return ModKeyAction(key, KC_RGUI)


def SGUI(key):
    return ModKeyAction(key, KC_LSFT, KC_LGUI)


def LCA(key):
    return ModKeyAction(key, KC_LCTL, KC_LALT)


def LSA(key):
    return ModKeyAction(key, KC_LSFT, KC_LALT)


def RSA(key):
    return ModKeyAction(key, KC_RSFT, KC_RALT)


def RCS(key):
    return ModKeyAction(key, KC_RCTL, KC_RSFT)


def LCAG(key):
    return ModKeyAction(key, KC_LCTL, KC_LALT, KC_LGUI)


def MEH(key):
    return ModKeyAction(key, KC_LCTL, KC_LSHIFT, KC_LALT)


def HYPR(key):
    return ModKeyAction(key, KC_LCTL, KC_LSHIFT, KC_LALT, KC_LGUI)


KC_MEH = ModKeyAction(None, KC_LCTL, KC_LSHIFT, KC_LALT)
KC_HYPR = ModKeyAction(None, KC_LCTL, KC_LSHIFT, KC_LALT, KC_LGUI)

C = LCTL
S = LSFT
A = LALT
LOPT = LALT
G = LGUI
LCMD = LGUI
LWIN = LGUI
ROPT = RALT
ALGR = RALT
SAGR = RSA


# mod tap actions
def MT(key, modifier):
    return ModTapAction(key, modifier)


def LCTL_T(key):
    return ModTapAction(key, KC_LCTL)


def LSFT_T(key):
    return ModTapAction(key, KC_LSFT)


def LALT_T(key):
    return ModTapAction(key, KC_LALT)


def LGUI_T(key):
    return ModTapAction(key, KC_LGUI)


def RCTL_T(key):
    return ModTapAction(key, KC_RCTL)


def RSFT_T(key):
    return ModTapAction(key, KC_RSFT)


def RALT_T(key):
    return ModTapAction(key, KC_RALT)


def RGUI_T(key):
    return ModTapAction(key, KC_RGUI)


def SGUI_T(key):
    return ModTapAction(key, KC_LSFT, KC_LGUI)


def LCA_T(key):
    return ModTapAction(key, KC_LCTL, KC_LALT)


def LSA_T(key):
    return ModTapAction(key, KC_LSFT, KC_LALT)


def RSA_T(key):
    return ModTapAction(key, KC_RSFT, KC_RALT)


def RCS_T(key):
    return ModTapAction(key, KC_RCTL, KC_RSFT)


def LCAG_T(key):
    return ModTapAction(key, KC_LCTL, KC_LALT, KC_LGUI)


def MEH_T(key):
    return ModTapAction(key, KC_LCTL, KC_LSHIFT, KC_LALT)


def HYPR_T(key):
    return ModTapAction(key, KC_LCTL, KC_LSHIFT, KC_LALT, KC_LGUI)


CTL_T = LCTL_T
SFT_T = LSFT_T
LOPT_T = LALT_T
ALT_T = LALT_T
OPT_T = LALT_T
LCMD_T = LGUI_T
LWIN_T = LGUI_T
GUI_T = LGUI_T
CMD_T = LGUI_T
WIN_T = LGUI_T
ROPT_T = RALT_T
ALGR_T = RALT_T
RCMD_T = RGUI_T
RWIN_T = RGUI_T
SCMD_T = SGUI_T
SWIN_T = SGUI_T
SAGR_T = RSA_T
ALL_T = HYPR_T


# layer actions

def MO(layer):
    return LayerOnAction(layer)


def LM(layer, *modifiers):
    return LayerModAction(layer, *modifiers)


def TG(layer):
    return LayerToggleAction(layer)


def LT(layer, key):
    return LayerTapAction(layer, key)


# shifted symbols
KC_TILDE = LSFT(KC_GRAVE)
KC_EXCLAIM = LSFT(KC_1)
KC_AT = LSFT(KC_2)
KC_HASH = LSFT(KC_3)
KC_DOLLAR = LSFT(KC_4)
KC_PERCENT = LSFT(KC_5)
KC_CIRCUMFLEX = LSFT(KC_6)
KC_AMPERSAND = LSFT(KC_7)
KC_ASTERISK = LSFT(KC_8)
KC_LEFT_PAREN = LSFT(KC_9)
KC_RIGHT_PAREN = LSFT(KC_0)
KC_UNDERSCORE = LSFT(KC_MINS)
KC_PLUS = LSFT(KC_EQUAL)
KC_LEFT_CURLY_BRACE = LSFT(KC_LBRC)
KC_RIGHT_CURLY_BRACE = LSFT(KC_RBRC)
KC_PIPE = LSFT(KC_BSLS)
KC_COLON = LSFT(KC_SCLN)
KC_DOUBLE_QUOTE = LSFT(KC_QUOT)
KC_LEFT_ANGLE_BRACKET = LSFT(KC_COMM)
KC_RIGHT_ANGLE_BRACKET = LSFT(KC_DOT)
KC_QUESTION = LSFT(KC_SLSH)

KC_TILD = KC_TILDE
KC_EXLM = KC_EXCLAIM
KC_DLR = KC_DOLLAR
KC_PERC = KC_PERCENT
KC_CIRC = KC_CIRCUMFLEX
KC_AMPR = KC_AMPERSAND
KC_ASTR = KC_ASTERISK
KC_LPRN = KC_LEFT_PAREN
KC_RPRN = KC_RIGHT_PAREN
KC_UNDS = KC_UNDERSCORE
KC_LCBR = KC_LEFT_CURLY_BRACE
KC_RCBR = KC_RIGHT_CURLY_BRACE
KC_COLN = KC_COLON
KC_DQUO = KC_DOUBLE_QUOTE
KC_DQT = KC_DOUBLE_QUOTE
KC_LABK = KC_LEFT_ANGLE_BRACKET
KC_LT = KC_LEFT_ANGLE_BRACKET
KC_RABK = KC_RIGHT_ANGLE_BRACKET
KC_GT = KC_RIGHT_ANGLE_BRACKET
KC_QUES = KC_QUESTION

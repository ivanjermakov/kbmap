from evdev.ecodes import *

# special keys
KC_NO = None
"""
Special 'no mapping' key.
When used in mapping, combination with this key will not be encountered.
"""

KC_TRANSPARENT = None
KC_TRNS = KC_TRANSPARENT
_______ = KC_TRANSPARENT
"""
Special key.
Used to indicate that current layer has no keys to assign.
Layer with lower precedence will be used instead.
"""

# digits
KC_0 = KEY_0
KC_1 = KEY_1
KC_2 = KEY_2
KC_3 = KEY_3
KC_4 = KEY_4
KC_5 = KEY_5
KC_6 = KEY_6
KC_7 = KEY_7
KC_8 = KEY_8
KC_9 = KEY_9

# letters
KC_A = KEY_A
KC_B = KEY_B
KC_C = KEY_C
KC_D = KEY_D
KC_E = KEY_E
KC_F = KEY_F
KC_J = KEY_J
KC_G = KEY_G
KC_H = KEY_H
KC_I = KEY_I
KC_K = KEY_K
KC_L = KEY_L
KC_M = KEY_M
KC_N = KEY_N
KC_O = KEY_O
KC_P = KEY_P
KC_Q = KEY_Q
KC_R = KEY_R
KC_S = KEY_S
KC_T = KEY_T
KC_U = KEY_U
KC_V = KEY_V
KC_W = KEY_W
KC_X = KEY_X
KC_Y = KEY_Y
KC_Z = KEY_Z

# function keys
KC_F1 = KEY_F1
KC_F2 = KEY_F2
KC_F3 = KEY_F3
KC_F4 = KEY_F4
KC_F5 = KEY_F5
KC_F6 = KEY_F6
KC_F7 = KEY_F7
KC_F8 = KEY_F8
KC_F9 = KEY_F9
KC_F10 = KEY_F10
KC_F11 = KEY_F11
KC_F12 = KEY_F12
KC_F13 = KEY_F13
KC_F14 = KEY_F14
KC_F15 = KEY_F15
KC_F16 = KEY_F16
KC_F17 = KEY_F17
KC_F18 = KEY_F18
KC_F19 = KEY_F19
KC_F20 = KEY_F20
KC_F21 = KEY_F21
KC_F22 = KEY_F22
KC_F23 = KEY_F23
KC_F24 = KEY_F24

# common
KC_ENTER = KEY_ENTER
KC_ESCAPE = KEY_ESC
KC_BSPACE = KEY_BACKSPACE
KC_TAB = KEY_TAB
KC_SPACE = KEY_SPACE
KC_MINUS = KEY_MINUS
KC_EQUAL = KEY_EQUAL
KC_LBRACKET = KEY_LEFTBRACE
KC_RBRACKET = KEY_RIGHTBRACE
KC_BSLASH = KEY_BACKSLASH
# KC_NONUS_HASH
KC_SCOLON = KEY_SEMICOLON
KC_QUOTE = KEY_APOSTROPHE
KC_GRAVE = KEY_GRAVE
KC_COMMA = KEY_COMMA
KC_DOT = KEY_DOT
KC_SLASH = KEY_SLASH
KC_CAPSLOCK = KEY_CAPSLOCK
KC_PSCREEN = KEY_SYSRQ
KC_SCROLLLOCK = KEY_SCROLLLOCK
KC_PAUSE = KEY_PAUSE
KC_INSERT = KEY_INSERT
KC_HOME = KEY_HOME
KC_PGUP = KEY_PAGEUP
KC_DELETE = KEY_DELETE
KC_END = KEY_END
KC_PGDOWN = KEY_PAGEDOWN
KC_RIGHT = KEY_RIGHT
KC_LEFT = KEY_LEFT
KC_DOWN = KEY_DOWN
KC_UP = KEY_UP
KC_NUMLOCK = KEY_NUMLOCK

KC_KP_SLASH = KEY_KPSLASH
KC_KP_ASTERISK = KEY_KPASTERISK
KC_KP_MINUS = KEY_KPMINUS
KC_KP_PLUS = KEY_KPPLUS
KC_KP_ENTER = KEY_KPENTER
KC_KP_1 = KEY_KP1
KC_KP_2 = KEY_KP2
KC_KP_3 = KEY_KP3
KC_KP_4 = KEY_KP4
KC_KP_5 = KEY_KP5
KC_KP_6 = KEY_KP6
KC_KP_7 = KEY_KP7
KC_KP_8 = KEY_KP8
KC_KP_9 = KEY_KP9
KC_KP_0 = KEY_KP0
KC_KP_DOT = KEY_KPDOT
KC_KP_EQUAL = KEY_KPEQUAL

# KC_NONUS_BSLASH
KC_MENU = KEY_MENU
KC_POWER = KEY_POWER
KC_APPLICATION = KEY_COMPOSE

# modifiers
KC_LCTRL = KEY_LEFTCTRL
KC_RCTRL = KEY_RIGHTCTRL
KC_LSHIFT = KEY_LEFTSHIFT
KC_RSHIFT = KEY_RIGHTSHIFT
KC_LALT = KEY_LEFTALT
KC_RALT = KEY_RIGHTALT
KC_LGUI = KEY_LEFTMETA
KC_RGUI = KEY_RIGHTMETA

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

# others
KC_KP_COMMA = KEY_KPCOMMA
KC_KP_JPCOMMA = KEY_KPJPCOMMA
KC_KP_LEFTPAREN = KEY_KPLEFTPAREN
KC_KP_PLUSMINUS = KEY_KPPLUSMINUS
KC_KP_RIGHTPAREN = KEY_KPRIGHTPAREN
KC_AB = KEY_AB
KC_ADDRESSBOOK = KEY_ADDRESSBOOK
KC_K3D_MODE = KEY_3D_MODE
KC_K102ND = KEY_102ND
KC_K10CHANNELSDOWN = KEY_10CHANNELSDOWN
KC_K10CHANNELSUP = KEY_10CHANNELSUP
KC_AGAIN = KEY_AGAIN
KC_ALS_TOGGLE = KEY_ALS_TOGGLE
KC_ALTERASE = KEY_ALTERASE
KC_ANGLE = KEY_ANGLE
KC_APPSELECT = KEY_APPSELECT
KC_ARCHIVE = KEY_ARCHIVE
KC_ASSISTANT = KEY_ASSISTANT
KC_ATTENDANT_OFF = KEY_ATTENDANT_OFF
KC_ATTENDANT_ON = KEY_ATTENDANT_ON
KC_ATTENDANT_TOGGLE = KEY_ATTENDANT_TOGGLE
KC_AUDIO = KEY_AUDIO
KC_AUDIO_DESC = KEY_AUDIO_DESC
KC_AUX = KEY_AUX
KC_BACK = KEY_BACK
KC_BASSBOOST = KEY_BASSBOOST
KC_BATTERY = KEY_BATTERY
KC_BLUE = KEY_BLUE
KC_BLUETOOTH = KEY_BLUETOOTH
KC_BOOKMARKS = KEY_BOOKMARKS
KC_BRIGHTNESSDOWN = KEY_BRIGHTNESSDOWN
KC_BRIGHTNESSUP = KEY_BRIGHTNESSUP
KC_BRIGHTNESS_AUTO = KEY_BRIGHTNESS_AUTO
KC_BRIGHTNESS_CYCLE = KEY_BRIGHTNESS_CYCLE
KC_BRIGHTNESS_MAX = KEY_BRIGHTNESS_MAX
KC_BRIGHTNESS_MIN = KEY_BRIGHTNESS_MIN
KC_BRIGHTNESS_TOGGLE = KEY_BRIGHTNESS_TOGGLE
KC_BRIGHTNESS_ZERO = KEY_BRIGHTNESS_ZERO
KC_BRL_DOT1 = KEY_BRL_DOT1
KC_BRL_DOT10 = KEY_BRL_DOT10
KC_BRL_DOT2 = KEY_BRL_DOT2
KC_BRL_DOT3 = KEY_BRL_DOT3
KC_BRL_DOT4 = KEY_BRL_DOT4
KC_BRL_DOT5 = KEY_BRL_DOT5
KC_BRL_DOT6 = KEY_BRL_DOT6
KC_BRL_DOT7 = KEY_BRL_DOT7
KC_BRL_DOT8 = KEY_BRL_DOT8
KC_BRL_DOT9 = KEY_BRL_DOT9
KC_BUTTONCONFIG = KEY_BUTTONCONFIG
KC_CALC = KEY_CALC
KC_CALENDAR = KEY_CALENDAR
KC_CAMERA = KEY_CAMERA
KC_CAMERA_DOWN = KEY_CAMERA_DOWN
KC_CAMERA_FOCUS = KEY_CAMERA_FOCUS
KC_CAMERA_LEFT = KEY_CAMERA_LEFT
KC_CAMERA_RIGHT = KEY_CAMERA_RIGHT
KC_CAMERA_UP = KEY_CAMERA_UP
KC_CAMERA_ZOOMIN = KEY_CAMERA_ZOOMIN
KC_CAMERA_ZOOMOUT = KEY_CAMERA_ZOOMOUT
KC_CANCEL = KEY_CANCEL
KC_CD = KEY_CD
KC_CHANNEL = KEY_CHANNEL
KC_CHANNELDOWN = KEY_CHANNELDOWN
KC_CHANNELUP = KEY_CHANNELUP
KC_CHAT = KEY_CHAT
KC_CLEAR = KEY_CLEAR
KC_CLOSE = KEY_CLOSE
KC_CLOSECD = KEY_CLOSECD
KC_CNT = KEY_CNT
KC_COFFEE = KEY_COFFEE
KC_COMPUTER = KEY_COMPUTER
KC_CONFIG = KEY_CONFIG
KC_CONNECT = KEY_CONNECT
KC_CONTEXT_MENU = KEY_CONTEXT_MENU
KC_CONTROLPANEL = KEY_CONTROLPANEL
KC_COPY = KEY_COPY
KC_CUT = KEY_CUT
KC_CYCLEWINDOWS = KEY_CYCLEWINDOWS
KC_DASHBOARD = KEY_DASHBOARD
KC_DATA = KEY_DATA
KC_DATABASE = KEY_DATABASE
KC_DELETEFILE = KEY_DELETEFILE
KC_DEL_EOL = KEY_DEL_EOL
KC_DEL_EOS = KEY_DEL_EOS
KC_DEL_LINE = KEY_DEL_LINE
KC_DIGITS = KEY_DIGITS
KC_DIRECTION = KEY_DIRECTION
KC_DIRECTORY = KEY_DIRECTORY
KC_DISPLAYTOGGLE = KEY_DISPLAYTOGGLE
KC_DISPLAY_OFF = KEY_DISPLAY_OFF
KC_DOCUMENTS = KEY_DOCUMENTS
KC_DOLLAR = KEY_DOLLAR
KC_DVD = KEY_DVD
KC_EDIT = KEY_EDIT
KC_EDITOR = KEY_EDITOR
KC_EJECTCD = KEY_EJECTCD
KC_EJECTCLOSECD = KEY_EJECTCLOSECD
KC_EMAIL = KEY_EMAIL
KC_EPG = KEY_EPG
KC_EURO = KEY_EURO
KC_EXIT = KEY_EXIT
KC_FASTFORWARD = KEY_FASTFORWARD
KC_FASTREVERSE = KEY_FASTREVERSE
KC_FAVORITES = KEY_FAVORITES
KC_FILE = KEY_FILE
KC_FINANCE = KEY_FINANCE
KC_FIND = KEY_FIND
KC_FIRST = KEY_FIRST
KC_FN = KEY_FN
KC_FN_1 = KEY_FN_1
KC_FN_2 = KEY_FN_2
KC_FN_B = KEY_FN_B
KC_FN_D = KEY_FN_D
KC_FN_E = KEY_FN_E
KC_FN_ESC = KEY_FN_ESC
KC_FN_F = KEY_FN_F
KC_FN_F1 = KEY_FN_F1
KC_FN_F10 = KEY_FN_F10
KC_FN_F11 = KEY_FN_F11
KC_FN_F12 = KEY_FN_F12
KC_FN_F2 = KEY_FN_F2
KC_FN_F3 = KEY_FN_F3
KC_FN_F4 = KEY_FN_F4
KC_FN_F5 = KEY_FN_F5
KC_FN_F6 = KEY_FN_F6
KC_FN_F7 = KEY_FN_F7
KC_FN_F8 = KEY_FN_F8
KC_FN_F9 = KEY_FN_F9
KC_FN_S = KEY_FN_S
KC_FORWARD = KEY_FORWARD
KC_FORWARDMAIL = KEY_FORWARDMAIL
KC_FRAMEBACK = KEY_FRAMEBACK
KC_FRAMEFORWARD = KEY_FRAMEFORWARD
KC_FRONT = KEY_FRONT
KC_GAMES = KEY_GAMES
KC_GOTO = KEY_GOTO
KC_GRAPHICSEDITOR = KEY_GRAPHICSEDITOR
KC_GREEN = KEY_GREEN
KC_HANGEUL = KEY_HANGEUL
KC_HANGUEL = KEY_HANGUEL
KC_HANJA = KEY_HANJA
KC_HELP = KEY_HELP
KC_HENKAN = KEY_HENKAN
KC_HIRAGANA = KEY_HIRAGANA
KC_HOMEPAGE = KEY_HOMEPAGE
KC_HP = KEY_HP
KC_IMAGES = KEY_IMAGES
KC_INFO = KEY_INFO
KC_INS_LINE = KEY_INS_LINE
KC_ISO = KEY_ISO
KC_JOURNAL = KEY_JOURNAL
KC_KATAKANA = KEY_KATAKANA
KC_KATAKANAHIRAGANA = KEY_KATAKANAHIRAGANA
KC_KBDILLUMDOWN = KEY_KBDILLUMDOWN
KC_KBDILLUMTOGGLE = KEY_KBDILLUMTOGGLE
KC_KBDILLUMUP = KEY_KBDILLUMUP
KC_KBDINPUTASSIST_ACCEPT = KEY_KBDINPUTASSIST_ACCEPT
KC_KBDINPUTASSIST_CANCEL = KEY_KBDINPUTASSIST_CANCEL
KC_KBDINPUTASSIST_NEXT = KEY_KBDINPUTASSIST_NEXT
KC_KBDINPUTASSIST_NEXTGROUP = KEY_KBDINPUTASSIST_NEXTGROUP
KC_KBDINPUTASSIST_PREV = KEY_KBDINPUTASSIST_PREV
KC_KBDINPUTASSIST_PREVGROUP = KEY_KBDINPUTASSIST_PREVGROUP
KC_KEYBOARD = KEY_KEYBOARD
KC_LANGUAGE = KEY_LANGUAGE
KC_LAST = KEY_LAST
KC_LEFT_DOWN = KEY_LEFT_DOWN
KC_LEFT_UP = KEY_LEFT_UP
KC_LIGHTS_TOGGLE = KEY_LIGHTS_TOGGLE
KC_LINEFEED = KEY_LINEFEED
KC_LIST = KEY_LIST
KC_LOGOFF = KEY_LOGOFF
KC_MACRO = KEY_MACRO
KC_MAIL = KEY_MAIL
KC_MAX = KEY_MAX
KC_MEDIA = KEY_MEDIA
KC_MEDIA_REPEAT = KEY_MEDIA_REPEAT
KC_MEDIA_TOP_MENU = KEY_MEDIA_TOP_MENU
KC_MEMO = KEY_MEMO
KC_MESSENGER = KEY_MESSENGER
KC_MHP = KEY_MHP
KC_MICMUTE = KEY_MICMUTE
KC_MIN_INTERESTING = KEY_MIN_INTERESTING
KC_MODE = KEY_MODE
KC_MOVE = KEY_MOVE
KC_MP3 = KEY_MP3
KC_MSDOS = KEY_MSDOS
KC_MUHENKAN = KEY_MUHENKAN
KC_MUTE = KEY_MUTE
KC_NEW = KEY_NEW
KC_NEWS = KEY_NEWS
KC_NEXT = KEY_NEXT
KC_NEXTSONG = KEY_NEXTSONG
KC_NEXT_FAVORITE = KEY_NEXT_FAVORITE
KC_NUMERIC_A = KEY_NUMERIC_A
KC_NUMERIC_B = KEY_NUMERIC_B
KC_NUMERIC_C = KEY_NUMERIC_C
KC_NUMERIC_D = KEY_NUMERIC_D
KC_NUMERIC_POUND = KEY_NUMERIC_POUND
KC_NUMERIC_STAR = KEY_NUMERIC_STAR
KC_OK = KEY_OK
KC_ONSCREEN_KEYBOARD = KEY_ONSCREEN_KEYBOARD
KC_OPEN = KEY_OPEN
KC_OPTION = KEY_OPTION
KC_PASTE = KEY_PASTE
KC_PAUSECD = KEY_PAUSECD
KC_PAUSE_RECORD = KEY_PAUSE_RECORD
KC_PC = KEY_PC
KC_PHONE = KEY_PHONE
KC_PLAY = KEY_PLAY
KC_PLAYCD = KEY_PLAYCD
KC_PLAYER = KEY_PLAYER
KC_PLAYPAUSE = KEY_PLAYPAUSE
KC_POWER2 = KEY_POWER2
KC_PRESENTATION = KEY_PRESENTATION
KC_PREVIOUS = KEY_PREVIOUS
KC_PREVIOUSSONG = KEY_PREVIOUSSONG
KC_PRINT = KEY_PRINT
KC_PROG1 = KEY_PROG1
KC_PROG2 = KEY_PROG2
KC_PROG3 = KEY_PROG3
KC_PROG4 = KEY_PROG4
KC_PROGRAM = KEY_PROGRAM
KC_PROPS = KEY_PROPS
KC_PVR = KEY_PVR
KC_QUESTION = KEY_QUESTION
KC_RADIO = KEY_RADIO
KC_RECORD = KEY_RECORD
KC_RED = KEY_RED
KC_REDO = KEY_REDO
KC_REFRESH = KEY_REFRESH
KC_REPLY = KEY_REPLY
KC_RESERVED = KEY_RESERVED
KC_RESTART = KEY_RESTART
KC_REWIND = KEY_REWIND
KC_RFKILL = KEY_RFKILL
KC_RIGHT_DOWN = KEY_RIGHT_DOWN
KC_RIGHT_UP = KEY_RIGHT_UP
KC_RO = KEY_RO
KC_ROOT_MENU = KEY_ROOT_MENU
KC_ROTATE_DISPLAY = KEY_ROTATE_DISPLAY
KC_SAT = KEY_SAT
KC_SAT2 = KEY_SAT2
KC_SAVE = KEY_SAVE
KC_SCALE = KEY_SCALE
KC_SCREEN = KEY_SCREEN
KC_SCREENLOCK = KEY_SCREENLOCK
KC_SCREENSAVER = KEY_SCREENSAVER
KC_SCROLLDOWN = KEY_SCROLLDOWN
KC_SCROLLUP = KEY_SCROLLUP
KC_SEARCH = KEY_SEARCH
KC_SELECT = KEY_SELECT
KC_SEND = KEY_SEND
KC_SENDFILE = KEY_SENDFILE
KC_SETUP = KEY_SETUP
KC_SHOP = KEY_SHOP
KC_SHUFFLE = KEY_SHUFFLE
KC_SLEEP = KEY_SLEEP
KC_SLOW = KEY_SLOW
KC_SLOWREVERSE = KEY_SLOWREVERSE
KC_SOUND = KEY_SOUND
KC_SPELLCHECK = KEY_SPELLCHECK
KC_SPORT = KEY_SPORT
KC_SPREADSHEET = KEY_SPREADSHEET
KC_STOP = KEY_STOP
KC_STOPCD = KEY_STOPCD
KC_STOP_RECORD = KEY_STOP_RECORD
KC_SUBTITLE = KEY_SUBTITLE
KC_SUSPEND = KEY_SUSPEND
KC_SWITCHVIDEOMODE = KEY_SWITCHVIDEOMODE
KC_TAPE = KEY_TAPE
KC_TASKMANAGER = KEY_TASKMANAGER
KC_TEEN = KEY_TEEN
KC_TEXT = KEY_TEXT
KC_TIME = KEY_TIME
KC_TITLE = KEY_TITLE
KC_TOUCHPAD_OFF = KEY_TOUCHPAD_OFF
KC_TOUCHPAD_ON = KEY_TOUCHPAD_ON
KC_TOUCHPAD_TOGGLE = KEY_TOUCHPAD_TOGGLE
KC_TUNER = KEY_TUNER
KC_TV = KEY_TV
KC_TV2 = KEY_TV2
KC_TWEN = KEY_TWEN
KC_UNDO = KEY_UNDO
KC_UNKNOWN = KEY_UNKNOWN
KC_UNMUTE = KEY_UNMUTE
KC_UWB = KEY_UWB
KC_VCR = KEY_VCR
KC_VCR2 = KEY_VCR2
KC_VENDOR = KEY_VENDOR
KC_VIDEO = KEY_VIDEO
KC_VIDEOPHONE = KEY_VIDEOPHONE
KC_VIDEO_NEXT = KEY_VIDEO_NEXT
KC_VIDEO_PREV = KEY_VIDEO_PREV
KC_VOD = KEY_VOD
KC_VOICECOMMAND = KEY_VOICECOMMAND
KC_VOICEMAIL = KEY_VOICEMAIL
KC_VOLUMEDOWN = KEY_VOLUMEDOWN
KC_VOLUMEUP = KEY_VOLUMEUP
KC_WAKEUP = KEY_WAKEUP
KC_WIMAX = KEY_WIMAX
KC_WLAN = KEY_WLAN
KC_WORDPROCESSOR = KEY_WORDPROCESSOR
KC_WPS_BUTTON = KEY_WPS_BUTTON
KC_WWAN = KEY_WWAN
KC_WWW = KEY_WWW
KC_XFER = KEY_XFER
KC_YELLOW = KEY_YELLOW
KC_YEN = KEY_YEN
KC_ZENKAKUHANKAKU = KEY_ZENKAKUHANKAKU
KC_ZOOM = KEY_ZOOM
KC_ZOOMIN = KEY_ZOOMIN
KC_ZOOMOUT = KEY_ZOOMOUT

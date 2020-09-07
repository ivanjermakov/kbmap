from evdev.events import KeyEvent

from kbmap import mapper
from kbmap.action.action_type import ActionType
from kbmap.log import debug


class KbmapToggleAction:
    type: ActionType

    def __init__(self):
        self.type = ActionType.KbmapToggleAction

    def handle(self, _, e, *args):
        debug('-- handling kbmap toggle action --')
        if e.value == KeyEvent.key_down:
            debug(f'now kbmap is {"enabled" if mapper.kbmap_enabled else "disabled"}')
            mapper.kbmap_enabled = not mapper.kbmap_enabled
            debug(f'toggle kbmap {"enabled" if mapper.kbmap_enabled else "disabled"}')
        else:
            debug('key release, skipping')


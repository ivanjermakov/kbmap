from pynput.keyboard import Controller, Listener

from kb_state import KbState


class KbMap:
    def __init__(self, mappings):
        self.mappings = mappings
        self.controller = Controller()
        self.listener = Listener(
            on_press=self._on_press,
            on_release=self._on_release,
            suppress=True
        )
        self.kb_state = KbState()

    def start(self):
        with self.listener:
            self.listener.join()

    def match(self, combination, callback):
        pass

    def _on_press(self, key):
        print(str(key))
        self.kb_state.press(key)
        print(self.kb_state.__str__())

    def _on_release(self, key):
        self.kb_state.release(key)


KbMap(None).start()

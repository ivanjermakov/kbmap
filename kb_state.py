class KbState:
    """
    Contains and supports map of currently pressed keys.

    Dictionary of (key, bool) containing state of each key.
    If the value is true: key is currently pressed.
    If the value is false or not exits: key is not currently pressed
    """
    map = {}

    def press(self, key):
        self.map[key] = True

    def release(self, key):
        self.map[key] = False

    def __str__(self) -> str:
        return self.map.__str__()

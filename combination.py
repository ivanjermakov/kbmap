import evdev


class Combination:
    """
    Describe keystroke.
    Contains pressed key (mostly character key) and list of currently pressed modifiers.
    """

    def __init__(self, key, modifiers=None):
        """
        Initialize combination object.
        :param key: Keycode of pressed key
        :param modifiers: List of keycodes of currently pressed modifiers. Default is []
        """
        if modifiers is None:
            modifiers = []
        self.key = key
        self.modifiers = modifiers

    def __eq__(self, other):
        """
        Combinations are equal if they match key and modifiers.
        :param other: combination compare to
        :return: true is objects are equal, false otherwise
        """
        return self.key == other.key and self.modifiers == other.modifiers

    def __str__(self):
        """
        Convert object to string in format ((modifier)? (+ modifier)*)? + key
        :return: string version of object
        """
        keys = self.modifiers + [self.key]
        verbose = list(map(lambda k: str(evdev.ecodes.keys[k]).replace('KEY_', ''), keys))
        return '+'.join(verbose)

    def matching(self, combination):
        """
        Check whether combination match another one.
        Combinations match if they keys are equal and all modifiers of target combination are contained in self
        combination.
        :param combination: another combination
        :return: true if combinations match, false otherwise
        """
        return self.key == combination.key and all(m in combination.modifiers for m in self.modifiers)

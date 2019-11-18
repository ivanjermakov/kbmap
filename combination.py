import evdev


class Combination:
    def __init__(self, key, modifiers=None):
        if modifiers is None:
            modifiers = []
        self.key = key
        self.modifiers = modifiers

    def __eq__(self, other):
        return self.key == other.key and self.modifiers == other.modifiers

    def __str__(self):
        keys = self.modifiers + [self.key]
        verbose = list(map(lambda k: str(evdev.ecodes.keys[k]).replace('KEY_', ''), keys))
        return '+'.join(verbose)

    def matching(self, combination):
        return self.key == combination.key and all(m in combination.modifiers for m in self.modifiers)

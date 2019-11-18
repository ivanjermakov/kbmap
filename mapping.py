from enum import Enum


class MappingType(Enum):
    copyModifiers = 1
    """when source mapping appear in combination with not included modifiers - copy them to target combination"""
    matchModifiers = 2
    """when source mapping appear in combination with not included modifiers - do not match source combination"""


class Mapping:
    def __init__(self, source, target, type=MappingType.copyModifiers):
        self.source = source
        self.target = target
        self.type = type

    def __str__(self):
        return f'{self.source} -> {self.target} ({self.type.name})'

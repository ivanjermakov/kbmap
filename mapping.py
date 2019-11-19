from enum import Enum

from combination import Combination


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

    @classmethod
    def bind(cls, source_modifiers, source_keys, target_modifiers, target_keys):
        if len(source_keys) != len(target_keys):
            raise Exception(f'length of source and target keys does not match: '
                            f'({len(source_keys)}, {len(target_keys)}'
                            f')')

        return list(
            filter(
                lambda c: c.source.key and c.target.key,
                map(
                    lambda i: Mapping(
                        Combination(source_keys[i], source_modifiers),
                        Combination(target_keys[i], target_modifiers)
                    ),
                    range(len(source_keys))
                )
            )
        )

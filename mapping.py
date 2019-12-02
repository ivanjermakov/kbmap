from enum import Enum

from combination import Combination
from util import flatten


# TODO
class MappingType(Enum):
    """
    Behavior of modifiers after mapping matching
    """
    copyModifiers = 1
    """
    when source mapping appear in combination with not included modifiers - copy them to target combination
    """
    matchModifiers = 2
    """
    when source mapping appear in combination with not included modifiers - do not match source combination
    """


class Mapping:
    """
    Pair of combinations to be matched during key mapping.
    """

    def __init__(self, source, target, type=MappingType.copyModifiers):
        """
        Initialize mapping instance.
        :param source: source combination
        :param target: target combination
        :param type: mapping type
        """
        self.source = source
        self.target = target
        self.type = type

    def __str__(self):
        """
        Create string version of object in format source -> target (type.name).
        :return: string version of object
        """
        return f'{self.source} -> {self.target} ({self.type.name})'

    def __repr__(self):
        return str(self)

    @classmethod
    def bind(cls, source_modifiers, source_keys, target_modifiers, target_keys):
        """
        Create mapping list binding each mapping with specified parameters.
        source_modifiers match one-to-one with target_modifiers.
        Must be the same length
        :param source_modifiers: source modifiers of each mapping
        :param source_keys: source keys
        :param target_modifiers: target modifiers of each mapping
        :param target_keys: target keys
        :return: bind mapping list
        """
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

    @staticmethod
    def merge(mappings_list):
        return flatten(mappings_list)

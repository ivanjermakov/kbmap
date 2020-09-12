from enum import Enum


class ActionType(Enum):
    """
    Action type
    """
    ModKeyAction = 1
    ModTapAction = 2
    LayerOnAction = 3
    LayerModAction = 4
    LayerToggleAction = 5
    LayerTapAction = 6
    KbmapToggleAction = 7

from enum import Enum

class DataType(Enum):
    MARKERS = 0
    VIRTUAL_MARKERS = 1
    MODELED_MARKERS = 2
    ANGLES = 3
    FORCES = 4
    MOMENTS = 5
    POWERS = 6
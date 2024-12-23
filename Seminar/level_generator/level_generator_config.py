from enum import Enum

WIDTH = 60
HEIGHT = 50
BG_COLOR = 0, 0, 0
DEFAULT_CHANCE = 10000
PROB_DECREASE = 500
POINT_COLOR = 255, 255, 0
STABLE_MOVES = 2


class Direction(Enum):
    """ Enum for directions."""
    UP = (0, -1)
    DOWN = (0, 1)
    LEFT = (-1, 0)
    RIGHT = (1, 0)

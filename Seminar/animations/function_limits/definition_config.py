from dataclasses import dataclass
from manim import *


@dataclass
class SkipSectionAnims:
    formal: bool = False
    graph: bool = False
    point_and_limit: bool = False
    epsilon: bool = False
    delta: bool = False
    moving_epsilon: bool = False
    moving_a: bool = False
    right_limit: bool = False
    both_limits: bool = False


@dataclass
class Colors:
    axes = BLUE
    time = YELLOW
    graph = GREEN
    point = RED
    limit = PINK
    epsilon = TEAL
    delta = ORANGE

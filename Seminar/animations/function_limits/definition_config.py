from dataclasses import dataclass
from manim import *


@dataclass
class SkipSectionAnims:
    formal: bool = True
    graph: bool = False


@dataclass
class Colors:
    axes = BLUE
    time = YELLOW
    graph = GREEN

import numpy as np

from manim import *
from counting_config import *

from typing import List


def get_vertical_set(size: int, color: str,
                     set_label: str, element_labels: List[str],
                     arrange_labels: np.ndarray) -> VGroup:
    """ Create a set represented by vertical dots with labels. """

    dots = VGroup(*[Dot(color=color) for _ in range(size)]).arrange(DOWN)
    element_labels = VGroup(*[
        MathTex(label, color=LABEL_COLOR, font_size=ELEMENT_LABEL_SIZE)
        for label in element_labels
    ]).arrange(DOWN)
    set_label = MathTex(set_label, color=color, font_size=SET_LABEL_SIZE)

    return VGroup(dots, set_label, element_labels).arrange(arrange_labels)


class Counting(Scene):
    def construct(self):
        # Counting all maps A -> B.
        self.next_section("Counting Maps", skip_animations=False)

        A = get_vertical_set(4, A_COLOR, "A", ["1", "2", "3", "4"], LEFT)
        A.move_to(4 * LEFT)

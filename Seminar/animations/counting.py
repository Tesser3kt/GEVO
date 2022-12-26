from typing import List, Tuple
import numpy as np

from manim import *
from counting_config import *


def get_vertical_set(size: int, color: str,
                     set_label: str, element_labels: List[str],
                     arrange_labels: np.ndarray) -> VGroup:
    """ Create a set represented by vertical dots with labels. """

    dots = VGroup(*[Dot(color=color)
                  for _ in range(size)]).arrange(DOWN, buff=1)
    element_labels = VGroup(*[
        Tex(label, color=LABEL_COLOR, font_size=ELEMENT_LABEL_SIZE).next_to(
            dots[i], arrange_labels)
        for i, label in enumerate(element_labels)
    ])
    set_label = Tex(set_label, color=color,
                    font_size=SET_LABEL_SIZE).next_to(dots, UP, buff=1)

    return VGroup(dots, set_label, element_labels)


def get_set_arrow(set1: VGroup, set2: VGroup,
                  elem1: int, elem2: int) -> VMobject:
    """ Create an arrow between two elements in two sets. """

    arrow = Arrow(set1[0][elem1].get_center(), set2[0]
                  [elem2].get_center(), color=ARROW_COLOR,
                  max_stroke_width_to_length_ratio=0.5,
                  max_tip_length_to_length_ratio=0.04)

    return arrow


class Counting(Scene):
    def play_set_creation(self, set: VGroup) -> None:
        self.play(
            *[DrawBorderThenFill(dot) for dot in set[0]]
        )
        self.play(Write(set[1]), Write(set[2]))

    def show_arrows(self, set1: VGroup, set2: VGroup,
                    set1_labels: List[str], set2_labels: List[str],
                    elem1: int, elems2: List[int],
                    main_text: MathTex) -> Tuple[VGroup, MathTex]:
        arrows = VGroup(get_set_arrow(set1, set2, elem1, elems2[0]))
        main_arrow = arrows[0].copy()

        next_text = MathTex(
            'f', '(', set1_labels[elem1], ')', '=', set2_labels[elems2[0]],
            color=ARROW_COLOR, font_size=ELEMENT_LABEL_SIZE
        ).move_to(ARROW_TEXT_POS)
        next_text[2].set_color(A_COLOR)
        next_text[-1].set_color(B_COLOR)

        if not main_text:
            self.play(AnimationGroup(
                GrowArrow(main_arrow),
                Write(next_text),
                lag_ratio=0.3
            ))
            main_text = next_text
            self.pause(1)
        else:
            self.play(
                AnimationGroup(
                    GrowArrow(main_arrow),
                    Transform(main_text, next_text),
                    lag_ratio=0.3
                ))

        for elem2 in elems2[:-1]:
            prev_arrow = main_arrow.copy()
            next_arrow = get_set_arrow(set1, set2, elem1, elem2 + 1)
            self.add(prev_arrow)
            arrows.add(next_arrow.copy())

            next_text = MathTex(
                'f', '(', set1_labels[elem1], ')', '=',
                set2_labels[elems2[elem2 + 1]],
                color=ARROW_COLOR, font_size=ELEMENT_LABEL_SIZE
            ).move_to(ARROW_TEXT_POS)
            next_text[2].set_color(A_COLOR)
            next_text[-1].set_color(B_COLOR)

            self.play(
                Transform(main_arrow, next_arrow),
                Transform(main_text, next_text),
                prev_arrow.animate.set_opacity(0.3)
            )
        self.play(main_arrow.animate.set_opacity(0.3))

        return arrows, main_text

    def construct(self):
        # Counting all maps A -> B.
        self.next_section("Counting Maps", skip_animations=False)

        A_elems = ["1", "2", "3", "4"]
        B_elems = ["a", "b", "c"]

        A = get_vertical_set(4, A_COLOR, "A", A_elems, LEFT)
        A.shift(3 * LEFT)

        B = get_vertical_set(3, B_COLOR, "B", B_elems, RIGHT)
        B.align_to(A, UP, UP)
        B.shift(3 * RIGHT)

        self.play_set_creation(A)
        self.pause(1)
        self.play_set_creation(B)

        arrow_groups = []
        main_text = None

        for i, _ in enumerate(A_elems):
            arrows, text = self.show_arrows(
                A, B, A_elems, B_elems, i, list(range(len(B[0]))), main_text
            )
            arrow_groups.append(arrows)
            main_text = text

        self.pause(2)

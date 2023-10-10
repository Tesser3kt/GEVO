import numpy as np
from random import random
from manim import *

INT_COLOR = TEAL_C
EX_COLOR = RED_C
SEQ_COLOR = WHITE
BRACKET_COLOR = [YELLOW_C, PINK, GREEN_C]


class BolzanoWeierstrass(Scene):
    def construct(self):
        # section
        self.next_section("start", skip_animations=False)

        interval = Line(LEFT * 4.2, RIGHT * 4.2, color=INT_COLOR, z_index=-10)
        infimum = Line(LEFT * 3.8 + UP * 0.2, LEFT * 3.8 + DOWN * 0.2, color=EX_COLOR)
        supremum = Line(
            RIGHT * 3.8 + UP * 0.2, RIGHT * 3.8 + DOWN * 0.2, color=EX_COLOR
        )
        extremes = VGroup(infimum, supremum)
        infimum_label = MathTex("s", color=EX_COLOR).next_to(infimum, UP)
        supremum_label = MathTex("S", color=EX_COLOR).next_to(supremum, UP)

        self.play(Create(interval), Create(extremes))
        self.play(Write(infimum_label), Write(supremum_label))

        # section
        self.next_section("show seq", skip_animations=False)

        seq = VGroup(
            *[
                Dot(LEFT * 3.6 + RIGHT * 7.2 * random(), color=SEQ_COLOR, radius=0.1)
                for _ in range(10)
            ]
        )
        seq += VGroup(
            *[
                Dot(LEFT * 1.7 + RIGHT * r, color=SEQ_COLOR, radius=0.1)
                for r in np.arange(0, 0.8, 0.08)
            ]
        )
        seq_label = MathTex("x_n", color=SEQ_COLOR).next_to(interval, UP, buff=0.5)
        self.play(AnimationGroup(Create(seq), Write(seq_label), lag_ratio=0.5))

        # section
        self.next_section("first int", skip_animations=False)

        left = MathTex("[", color=BRACKET_COLOR[0]).move_to(LEFT * 3.8)
        right = MathTex("]", color=BRACKET_COLOR[0]).move_to(RIGHT * 3.8)
        left_label = MathTex("a_1", color=BRACKET_COLOR[0]).next_to(left, DOWN)
        right_label = MathTex("b_1", color=BRACKET_COLOR[0]).next_to(right, DOWN)
        int_label = MathTex("I_1", color=BRACKET_COLOR[0]).next_to(
            np.array([0, 0, 0]), DOWN, buff=0.5
        )

        self.play(
            Transform(infimum, left, replace_mobject_with_target_in_scene=True),
            Transform(supremum, right, replace_mobject_with_target_in_scene=True),
        )
        self.play(Write(left_label), Write(right_label), Write(int_label))

        # section
        self.next_section("second int", skip_animations=False)

        first_int = VGroup(
            left,
            right,
            left_label,
            right_label,
            int_label,
            seq,
            seq_label,
            interval,
            infimum_label,
            supremum_label,
        )
        self.play(first_int.animate.shift(UP * 3))

        second_int = first_int.copy()
        second_int.set_opacity(0)

        self.play(
            second_int.animate.set_opacity(1).shift(DOWN * 3),
            run_time=2,
        )

        new_left_label = MathTex("a_2", color=BRACKET_COLOR[1]).next_to(
            second_int[0], DOWN
        )
        new_right_label = MathTex("b_2", color=BRACKET_COLOR[1]).next_to(
            second_int[1], DOWN
        )
        new_right_label.add_updater(lambda m: m.next_to(second_int[1], DOWN))
        new_int_label = MathTex("I_2", color=BRACKET_COLOR[1]).next_to(
            LEFT * 1.9, DOWN, buff=0.5
        )
        self.play(
            second_int[0].animate.set_color(BRACKET_COLOR[1]),
            second_int[1].animate.set_color(BRACKET_COLOR[1]).shift(LEFT * 3.8),
            Transform(second_int[2], new_left_label),
            Transform(second_int[3], new_right_label),
            Transform(second_int[4], new_int_label),
        )

        # section
        self.next_section("third int", skip_animations=False)

        third_int = second_int.copy()
        third_int.set_opacity(0)

        self.play(third_int.animate.set_opacity(1).shift(DOWN * 3), run_time=2)
        new_left_label = MathTex("a_3", color=BRACKET_COLOR[2]).next_to(
            third_int[0], DOWN
        )
        new_right_label = MathTex("b_3", color=BRACKET_COLOR[2]).next_to(
            third_int[1], DOWN
        )
        new_left_label.add_updater(lambda m: m.next_to(third_int[0], DOWN))
        new_int_label = MathTex("I_3", color=BRACKET_COLOR[2]).next_to(
            DOWN * 3 + LEFT * 0.95, DOWN, buff=0.5
        )
        self.play(
            third_int[0].animate.set_color(BRACKET_COLOR[2]).shift(RIGHT * 1.9),
            third_int[1].animate.set_color(BRACKET_COLOR[2]),
            Transform(third_int[2], new_left_label),
            Transform(third_int[3], new_right_label),
            Transform(third_int[4], new_int_label),
        )

        self.pause(2)

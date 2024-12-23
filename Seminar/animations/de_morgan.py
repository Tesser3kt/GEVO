from hashlib import algorithms_available
import numpy as np
from manim import *

A_CIRCLE_RADIUS = 1
A_CIRCLE_COLORS = [
    RED_C,
    BLUE_C,
    GREEN_C
]
LABEL_FONT_SIZE = 60

UNION_COLOR = PINK

X_CIRCLE_RADIUS = 3
X_CIRCLE_COLOR = WHITE

FINAL_SET_SCALE_FACTOR = 0.6

PARTIAL_SET_SCALE_FACTOR = 0.3


class DeMorgan(Scene):
    def construct(self):
        # self.add(NumberPlane())
        # set circles
        A_1 = Circle(A_CIRCLE_RADIUS, A_CIRCLE_COLORS[0])
        A_2 = A_1.copy()
        A_3 = A_1.copy()

        self.play(Create(A_1))
        self.play(
            A_1.animate.shift(0.25 * DOWN + 0.75 * LEFT),
            A_2.animate.shift(0.25 * DOWN + 0.75 *
                              RIGHT).set_color(A_CIRCLE_COLORS[1]),
            A_3.animate.shift(0.75 * UP).set_color(A_CIRCLE_COLORS[2])
        )

        # create copies for second section
        A_1c = A_1.copy()
        A_2c = A_2.copy()
        A_3c = A_3.copy()

        # set labels
        A_1_label = MathTex(
            r'A_1', color=A_CIRCLE_COLORS[0], font_size=LABEL_FONT_SIZE)
        A_2_label = MathTex(
            r'A_2', color=A_CIRCLE_COLORS[1], font_size=LABEL_FONT_SIZE)
        A_3_label = MathTex(
            r'A_3', color=A_CIRCLE_COLORS[2], font_size=LABEL_FONT_SIZE)

        A_1_label.next_to(A_1, DOWN + LEFT, buff=0.8, aligned_edge=UP + RIGHT)
        A_2_label.next_to(A_2, DOWN + RIGHT, buff=0.8, aligned_edge=UP + LEFT)
        A_3_label.next_to(A_3, UP, buff=1.2, aligned_edge=DOWN)

        self.play(Write(A_1_label), Write(A_2_label), Write(A_3_label))
        self.pause(2)

        # union
        union = VGroup(A_1, A_2, A_3).set_z_index(1)
        union_label = MathTex(r'A_1 \cup A_2 \cup A_3',
                              color=UNION_COLOR,
                              font_size=LABEL_FONT_SIZE)
        union_label.set_z_index(1)
        union_label.next_to(union, DOWN, buff=0.6, aligned_edge=DOWN)
        A_12_labels = VGroup(A_1_label, A_2_label)
        self.play(
            A_1.animate.set_color(UNION_COLOR).set_fill(opacity=1),
            A_2.animate.set_color(UNION_COLOR).set_fill(opacity=1),
            A_3.animate.set_color(UNION_COLOR).set_fill(opacity=1),
            FadeTransform(A_12_labels, union_label),
            FadeOut(A_3_label)
        )

        # superset
        X = Circle(X_CIRCLE_RADIUS, X_CIRCLE_COLOR).set_z_index(0)
        X_label = MathTex(r'X', color=X_CIRCLE_COLOR,
                          font_size=LABEL_FONT_SIZE)
        X_label.next_to(X, UP, buff=0.4)
        X_c = X.copy()
        X_labelc = X_label.copy()

        # final set
        backslash = MathTex(r'\setminus', color=X_CIRCLE_COLOR,
                            font_size=LABEL_FONT_SIZE)
        backslash.next_to(X_label, RIGHT)
        backslash.shift(2.4 * LEFT)
        open_par = MathTex(
            r'(', color=X_CIRCLE_COLOR,
            font_size=LABEL_FONT_SIZE).next_to(backslash, RIGHT)
        closed_par = MathTex(r')', color=X_CIRCLE_COLOR,
                             font_size=LABEL_FONT_SIZE).next_to(open_par,
                                                                RIGHT)
        closed_par.shift(union_label.width * RIGHT)
        final_set_label = VGroup(X_label, backslash, open_par,
                                 union_label, closed_par)
        self.play(Create(X), Write(X_label))
        self.pause(3)
        self.play(X.animate.set_fill(opacity=1))
        self.play(
            union.animate.set_color(color=BLACK),
            X_label.animate.shift(2.4 * LEFT),
            FadeIn(backslash, shift=0.2 * RIGHT),
            union_label.animate.next_to(backslash, RIGHT, 0.1)
        )
        self.play(
            FadeIn(open_par, shift=0.2 * LEFT),
            FadeIn(closed_par, shift=0.2 * RIGHT),
            union_label.animate.next_to(
                open_par, RIGHT, 0.1).set_color(X_CIRCLE_COLOR)
        )

        self.pause(2)
        # finishing section
        final_set = VGroup(final_set_label, union, X)
        self.play(final_set.animate.scale(FINAL_SET_SCALE_FACTOR))
        frame = SurroundingRectangle(final_set, color=TEAL_C, buff=0.5)
        final_set = VGroup(final_set, frame)
        self.play(Create(frame))
        self.play(final_set.animate.move_to(4 * LEFT))

        # next section
        self.next_section()

        final_set_tex = MathTex(
            r'(',
            r'X',
            r'\setminus',
            r'A_1',
            r')',
            r'\cap',
            r'(',
            r'X',
            r'\setminus',
            r'A_2',
            r')',
            r'\cap',
            r'(',
            r'X',
            r'\setminus',
            r'A_3',
            r')',
            color=BLACK,
            font_size=LABEL_FONT_SIZE * FINAL_SET_SCALE_FACTOR
        )

        # X \ A_1
        X_c.scale(FINAL_SET_SCALE_FACTOR).move_to(3 * RIGHT).set_z_index(0)

        final_set_tex.move_to(
            X_c.get_center() +
            (X_CIRCLE_RADIUS * FINAL_SET_SCALE_FACTOR + 0.4) *
            UP + (final_set_tex[0].width + 0.2) * LEFT,
            aligned_edge=LEFT)

        A_1c.scale(FINAL_SET_SCALE_FACTOR)
        shift_vector = FINAL_SET_SCALE_FACTOR * (0.25 * DOWN + 0.75 * LEFT)
        A_1c.move_to(3 * RIGHT).shift(shift_vector).set_z_index(1)

        prev_label_positions = {
            'A_1': final_set_tex[3].get_center(),
            'A_2': final_set_tex[9].get_center(),
            'A_3': final_set_tex[15].get_center()
        }

        final_set_tex[3].set_color(
            A_CIRCLE_COLORS[0]).next_to(
                A_1c, DOWN + LEFT,
            buff=0.8 * FINAL_SET_SCALE_FACTOR,
            aligned_edge=UP + RIGHT
        )
        self.play(Create(A_1c), Write(final_set_tex[3]))

        final_set_tex[1].set_color(X_CIRCLE_COLOR)
        final_set_tex[2].set_color(X_CIRCLE_COLOR)
        self.play(Create(X_c), Write(final_set_tex[1]))

        self.pause(2)
        shift_factor = 0.4
        final_set_tex.shift(shift_factor * LEFT)
        final_set_tex[1].shift(shift_factor * RIGHT)
        final_set_tex[3].shift(shift_factor * RIGHT)

        for name in prev_label_positions:
            prev_label_positions[name] += shift_factor * LEFT

        self.play(
            A_1c.animate.set_fill(opacity=1),
            final_set_tex[1].animate.shift(shift_factor * LEFT),
            FadeIn(final_set_tex[2], shift=0.2 * RIGHT),
            final_set_tex[3].animate.move_to(prev_label_positions['A_1']),
            X_c.animate.set_fill(opacity=0.3)
        )

        shift_vector = FINAL_SET_SCALE_FACTOR * (0.25 * DOWN + 0.75 * RIGHT)
        A_2c.move_to(X_c.get_center()).shift(
            shift_vector).scale(FINAL_SET_SCALE_FACTOR).set_z_index(2)
        final_set_tex[9].set_color(
            A_CIRCLE_COLORS[1]).next_to(
                A_2c, DOWN + RIGHT,
                buff=0.8 * FINAL_SET_SCALE_FACTOR,
                aligned_edge=UP + LEFT
        )
        self.play(Create(A_2c), Write(final_set_tex[9]))
        final_set_tex[0].set_color(X_CIRCLE_COLOR)

        for i in range(4, 11):
            if i != 9:
                final_set_tex[i].set_color(X_CIRCLE_COLOR)

        shift_factor = 1
        for name in prev_label_positions:
            prev_label_positions[name] += shift_factor * LEFT

        self.pause(2)
        self.play(
            A_2c.animate.set_fill(opacity=1),
            FadeIn(final_set_tex[0], shift=0.2 * LEFT),
            FadeIn(final_set_tex[4], shift=0.2 * RIGHT),
            *[Write(final_set_tex[i]) for i in range(5, 11) if i != 9],
            *[final_set_tex[i].animate.shift(shift_factor * LEFT)
              for i in range(11) if i != 9],
            final_set_tex[9].animate.move_to(prev_label_positions['A_2'])
        )
        for i in range(11, 17):
            final_set_tex[i].shift(shift_factor * LEFT)

        shift_vector = FINAL_SET_SCALE_FACTOR * (0.75 * UP)
        A_3c.move_to(X_c.get_center()).shift(
            shift_vector).scale(FINAL_SET_SCALE_FACTOR).set_z_index(3)
        final_set_tex[15].set_color(
            A_CIRCLE_COLORS[2]).next_to(
                A_3c, UP,
                buff=1.2 * FINAL_SET_SCALE_FACTOR,
                aligned_edge=DOWN
        )
        self.play(Create(A_3c), Write(final_set_tex[15]))
        for i in range(11, 17):
            if i != 15:
                final_set_tex[i].set_color(X_CIRCLE_COLOR)

        shift_factor = 1
        for name in prev_label_positions:
            prev_label_positions[name] += shift_factor * LEFT

        self.pause(2)
        self.play(
            A_3c.animate.set_fill(opacity=1),
            FadeIn(final_set_tex[12], shift=0.2 * LEFT),
            FadeIn(final_set_tex[16], shift=0.2 * RIGHT),
            *[Write(final_set_tex[i]) for i in range(11, 17) if i != 15],
            *[final_set_tex[i].animate.shift(shift_factor * LEFT)
              for i in range(17) if i != 15],
            final_set_tex[15].animate.move_to(prev_label_positions['A_3'])
        )

        self.pause(2)
        self.play(
            X_c.animate.set_fill(opacity=1),
            A_1c.animate.set_color(BLACK),
            A_2c.animate.set_color(BLACK),
            A_3c.animate.set_color(BLACK),
            *[final_set_tex[i].animate.set_color(X_CIRCLE_COLOR)
              for i in (3, 9, 15)]
        )
        final_set = VGroup(X_c, A_1c, A_2c, A_3c, final_set_tex)
        frame = SurroundingRectangle(
            final_set, TEAL_C, 0.5)
        final_set.add(frame)
        self.play(Create(frame))
        self.play(final_set.animate.move_to(3 * RIGHT))

        self.pause(5)

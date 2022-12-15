from typing import List, Tuple
from manim import *
from variables_config import *


class Variables(Scene):
    def get_scales(self) -> Tuple[VMobject]:
        bowl = VMobject().set_stroke(width=SCALES_STROKE).set_color(
            SCALES_COLOR).set_z_index(1)
        bowl.set_points_as_corners([
            3 * LEFT + UP,
            3 * LEFT + .5 * UP,
            LEFT + .5 * UP,
            LEFT + UP
        ])
        frame = VMobject().set_stroke(width=SCALES_STROKE).set_color(
            SCALES_COLOR).set_z_index(1)
        frame.set_points_as_corners([
            2 * LEFT + .5 * UP,
            2 * LEFT,
            2 * RIGHT,
            2 * RIGHT + .5 * UP,
        ])
        triangle = RegularPolygon(3, color=SCALES_COLOR,
                                  stroke_width=SCALES_STROKE).move_to(
            frame.get_bottom(), UP).set_z_index(0).shift(0.03 * DOWN)

        return triangle, frame, bowl.copy(), bowl.copy().shift(4 * RIGHT)

    def construct(self):
        tex_template = TexTemplate()
        tex_template.add_to_preamble(r"\usepackage{wasysym}")
        self.next_section("Intro", skip_animations=False)

        triangle, frame, bowl1, bowl2 = self.get_scales()
        scales = VGroup(triangle, frame, bowl1, bowl2).scale(1.3)

        self.play(AnimationGroup(
            Create(triangle),
            Create(frame),
            AnimationGroup(Create(bowl1), Create(bowl2)),
            lag_ratio=.3))
        self.play(scales.animate.shift(DOWN))
        self.pause(2)

        self.next_section("One Object", skip_animations=False)

        square = Square(0.5, color=SQUARE_COLOR)

        times_three = MathTex(
            r'3', r'\cdot', r'\square', color=TEXT_COLOR, font_size=TEXT_SIZE
        ).move_to(bowl1.get_center()).shift(3 * UP)
        times_three[-1].set_color(SQUARE_COLOR)

        self.play(Write(times_three))
        self.pause(1)

        three_squares_left = VGroup(
            square,
            square.copy(),
            square.copy()
        ).arrange(RIGHT, buff=0.1).move_to(bowl1.get_center(),
                                           DOWN).shift(0.1 * DOWN)

        self.play(
            AnimationGroup(
                *[FadeIn(three_squares_left[i], shift=0.2 * DOWN)
                    for i in range(3)],
                lag_ratio=0.2
            ))

        self.pause(1)

        equals = MathTex(r'=', color=TEXT_COLOR,
                         font_size=TEXT_SIZE).next_to(
            times_three, RIGHT).shift(1.55 * RIGHT)

        self.play(FadeIn(equals, shift=0.2 * UP))

        plus_three = MathTex(
            r'\square', r'+', r'\square', r'+', r'\square',
            color=TEXT_COLOR, font_size=TEXT_SIZE
        ).move_to(bowl2.get_center()).shift(3 * UP)

        plus_three[0].set_color(SQUARE_COLOR)
        plus_three[2].set_color(SQUARE_COLOR)
        plus_three[-1].set_color(SQUARE_COLOR)

        self.play(Write(plus_three))

        self.pause(1)

        three_squares_right = VGroup(
            square.copy(),
            square.copy(),
            square.copy()
        ).arrange(DOWN, buff=0.1).move_to(bowl2.get_center(),
                                          DOWN).shift(0.1 * DOWN)

        self.play(
            AnimationGroup(
                *[FadeIn(three_squares_right[-i], shift=0.2 * DOWN)
                    for i in range(1, 4)],
                lag_ratio=0.2
            ))

        self.pause(2)

        self.next_section("Two Objects", skip_animations=False)

        self.play(
            FadeOut(times_three),
            FadeOut(plus_three),
            FadeOut(equals),
            FadeOut(three_squares_left),
            FadeOut(three_squares_right),
        )

        triangle = RegularPolygon(3, color=TRIANGLE_COLOR).scale(0.333)
        text_left = MathTex(
            r'3', r'\cdot', r'(', r'\square', r'+', r'\triangle', r')',
            color=TEXT_COLOR, font_size=TEXT_SIZE, tex_template=tex_template
        ).move_to(bowl1.get_center()).shift(3 * UP)

        text_left[3].set_color(SQUARE_COLOR)
        text_left[-2].set_color(TRIANGLE_COLOR)

        self.play(Write(text_left))
        self.pause(1)

        group_left = VGroup(
            triangle.copy(),
            triangle.copy(),
            triangle.copy(),
            square.copy(),
            square.copy(),
            square.copy()
        ).arrange_in_grid(3, 3, row_heights=[0.33, 0.33, 0.33]).move_to(
            bowl1.get_center(),
            DOWN).shift(0.1 * DOWN)

        self.play(
            AnimationGroup(
                FadeIn(group_left[3], shift=0.2 * DOWN),
                FadeIn(group_left[0], shift=0.2 * DOWN),
                lag_ratio=0.2
            ))

        self.pause(1)

        self.play(AnimationGroup(
            AnimationGroup(
                FadeIn(group_left[4], shift=0.2 * DOWN),
                FadeIn(group_left[1], shift=0.2 * DOWN),
                lag_ratio=0.2
            ),
            AnimationGroup(
                FadeIn(group_left[5], shift=0.2 * DOWN),
                FadeIn(group_left[2], shift=0.2 * DOWN),
                lag_ratio=0.2
            ),
            lag_ratio=0.5))

        self.play(FadeIn(equals, shift=0.2 * UP))

        text_right = MathTex(
            r'3', r'\cdot', r'\square', r'+', r'3', r'\cdot', r'\triangle',
            color=TEXT_COLOR, font_size=TEXT_SIZE, tex_template=tex_template
        ).move_to(bowl2.get_center()).shift(3 * UP)
        text_right[2].set_color(SQUARE_COLOR)
        text_right[-1].set_color(TRIANGLE_COLOR)

        self.play(Write(text_right))

        self.pause(1)

        group_right = group_left.copy().move_to(
            bowl2.get_center(),
            DOWN).shift(0.1 * DOWN)

        self.play(AnimationGroup(
            FadeIn(group_right[3], shift=0.2 * DOWN),
            FadeIn(group_right[4], shift=0.2 * DOWN),
            FadeIn(group_right[5], shift=0.2 * DOWN),
            lag_ratio=0.2))

        self.pause(1)

        self.play(AnimationGroup(
            FadeIn(group_right[0], shift=0.2 * DOWN),
            FadeIn(group_right[1], shift=0.2 * DOWN),
            FadeIn(group_right[2], shift=0.2 * DOWN),
            lag_ratio=0.2))

        self.pause(1)

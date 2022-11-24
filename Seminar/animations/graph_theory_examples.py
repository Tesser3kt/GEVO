from typing import Tuple
import numpy as np

from graph_theory_examples_config import *
from manim import *


def get_house(color: str) -> Tuple[VMobject]:
    # mainframe
    frame = Square(side_length=4, color=color)

    # roof
    roof = VMobject(stroke_color=color).set_points_as_corners([
        3 * LEFT + UP,
        4 * UP,
        3 * RIGHT + UP
    ])

    # door
    door = Rectangle(
        color=color,
        height=1.75,
        width=1,
        z_index=1
    ).move_to(2 * DOWN, aligned_edge=DOWN)

    # windows
    window = Square(side_length=1, color=color)
    window = VGroup(
        window,
        Line(window.get_center() + 0.5 * UP,
             window.get_center() + 0.5 * DOWN, color=color),
        Line(window.get_center() + 0.5 * LEFT,
             window.get_center() + 0.5 * RIGHT, color=color)
    )
    window.move_to(LEFT + UP)
    windows = [
        window,
        window.copy().move_to(RIGHT + UP)
    ]

    return frame, roof, door, *windows


def get_well(color: str) -> Tuple[VMobject]:
    well_outer = Circle(radius=2, color=color,
                        fill_color=BLACK, fill_opacity=1, z_index=1)
    well_inner = Circle(radius=1.5, color=color,
                        fill_color=BLACK, fill_opacity=1, z_index=2)

    well_stones = VGroup(*[
        Line(ORIGIN, 2 * UP, color=color,
             z_index=1).rotate(i * TAU / 16, about_point=ORIGIN)
        for i in range(16)
    ])

    return well_outer, well_inner, well_stones


class GraphTheoryExamples(Scene):
    def construct(self):
        self.next_section("Intro", skip_animations=False)

        house1 = VGroup(*get_house(HOUSE_COLOR)).scale(0.3).move_to(ORIGIN)
        house2 = house1.copy()
        house3 = house1.copy()

        self.play(AnimationGroup(
            AnimationGroup(*[Create(house1[i]) for i in range(2)]),
            AnimationGroup(*[Create(house1[i]) for i in range(2, 5)]),
            lag_ratio=0.5
        ))

        house2.set_stroke(opacity=0)
        house3.set_stroke(opacity=0)
        self.play(AnimationGroup(
            house2.animate.set_stroke(opacity=1).shift(4 * LEFT),
            house3.animate.set_stroke(opacity=1).shift(4 * RIGHT),
            run_time=1.5
        ))

        house1[2].set_fill(color=BLACK, opacity=1)
        house2[2].set_fill(color=BLACK, opacity=1)
        house3[2].set_fill(color=BLACK, opacity=1)

        well1 = VGroup(*get_well(WELL_COLOR))
        well2 = well1.copy()
        well3 = well2.copy()

        well1.shift(3 * DOWN).scale(0.2)
        well2.shift(3 * UP).scale(0.2)
        self.play(
            AnimationGroup(
                AnimationGroup(Create(well1[0]), GrowFromCenter(well1[1])),
                AnimationGroup(*[Create(well1[2][i])
                                 for i in range(16)], run_time=1,
                               lag_ratio=0.1),
                lag_ratio=0.5
            ),
            AnimationGroup(
                AnimationGroup(Create(well2[0]), GrowFromCenter(well2[1])),
                AnimationGroup(*[Create(well2[2][i])
                                 for i in range(16)], run_time=1,
                               lag_ratio=0.1),
                lag_ratio=0.5
            )
        )

        self.pause(3)
        self.next_section("Roads", skip_animations=False)

        road11 = Line(house1.get_bottom(),
                      well1.get_center(), color=ROAD_COLOR, stroke_width=6,
                      z_index=-2)
        road21 = Line(house2.get_bottom(),
                      well1.get_center(), color=ROAD_COLOR, stroke_width=6,
                      z_index=-2)
        road31 = Line(house3.get_bottom(),
                      well1.get_center(), color=ROAD_COLOR, stroke_width=6,
                      z_index=-2)
        self.play(Create(road11), Create(road21), Create(road31))

        self.pause(2)
        road12 = CubicBezier(
            house2.get_bottom(),
            house2.get_bottom() + 2 * RIGHT + DOWN,
            well2.get_center() + 2 * LEFT,
            well2.get_center(),
            color=ROAD_COLOR,
            stroke_width=6,
            z_index=-2
        )
        road22 = CubicBezier(
            house1.get_bottom(),
            house1.get_bottom() + 2 * RIGHT + DOWN,
            well2.get_center() + DOWN + RIGHT,
            well2.get_center(),
            color=ROAD_COLOR,
            stroke_width=6,
            z_index=-2
        )
        road32 = CubicBezier(
            house3.get_bottom(),
            house3.get_bottom() + 2 * LEFT + DOWN,
            well2.get_center() + 2 * RIGHT,
            well2.get_center(),
            color=ROAD_COLOR,
            stroke_width=6,
            z_index=-2
        )
        self.play(Create(road12), Create(road22), Create(road32))

        self.pause(1)
        self.next_section("Third Well", skip_animations=False)
        well3.shift(3 * LEFT + 2 * UP).scale(0.2)

        self.play(
            AnimationGroup(
                AnimationGroup(Create(well3[0]), GrowFromCenter(well3[1])),
                AnimationGroup(*[Create(well3[2][i])
                                 for i in range(16)], run_time=1,
                               lag_ratio=0.1),
                lag_ratio=0.5
            )
        )

        self.pause(1)
        road13 = CubicBezier(
            house2.get_bottom(),
            house2.get_bottom() + 3 * LEFT + 2 * DOWN,
            well3.get_center() + 3 * LEFT,
            well3.get_center(),
            color=ROAD_COLOR,
            stroke_width=6,
            z_index=-2
        )
        road33 = CubicBezier(
            house3.get_bottom(),
            house3.get_bottom() + 5 * RIGHT + 2 * DOWN,
            well3.get_center() + 5.5 * UP + 2.5 * RIGHT,
            well3.get_center(),
            color=ROAD_COLOR,
            stroke_width=6,
            z_index=-2
        )
        self.play(Create(road13), Create(road33))

        self.pause(2)
        self.next_section("Playful Road", skip_animations=False)

        road23 = CubicBezier(
            house1.get_bottom(),
            house1.get_bottom() + 2 * LEFT + DOWN,
            well3.get_center() + 2 * RIGHT + 2 * DOWN,
            well3.get_center() + 1.3 * (RIGHT + DOWN),
            color=ROAD_COLOR,
            stroke_width=6,
            z_index=-2
        )
        road23_1 = road23.copy()
        road23_2 = CubicBezier(
            house1.get_bottom(),
            house1.get_bottom() + 4 * LEFT + 2 * DOWN,
            well3.get_center() + 4 * RIGHT + 0.5 * UP,
            well3.get_center() + 2.2 * RIGHT + 0.3 * UP,
            color=CONFUSED_COLORS[0],
            stroke_width=6,
            z_index=-2
        )
        road23_3 = CubicBezier(
            house1.get_bottom(),
            house1.get_bottom() + LEFT + DOWN,
            well3.get_center() + RIGHT + 4 * DOWN,
            well3.get_center() + 0.8 * RIGHT + 2.5 * DOWN,
            color=CONFUSED_COLORS[1],
            stroke_width=6,
            z_index=-2
        )
        self.play(Create(road23))
        self.pause(1)
        self.play(Transform(road23, road23_2))
        self.pause(1)
        self.play(Transform(road23, road23_3))
        self.pause(1)
        self.play(Transform(road23, road23_1))

        self.next_section("Question Marks", skip_animations=False)

        question_mark = Tex("?").scale(4).set_color(MARK_COLOR)
        question_mark.move_to(road23.get_center())
        question_marks = [
            question_mark.copy().shift(UP + LEFT).rotate(PI / 8),
            question_mark.copy().shift(DOWN + 0.3 * LEFT).rotate(-PI / 11),
            question_mark.copy().shift(1.5 * UP + 2 * RIGHT).rotate(-3 * PI / 11),
            question_mark.copy().shift(0.5 * DOWN + 2 * LEFT).rotate(17 * PI / 14)
        ]

        self.play(
            AnimationGroup(*[
                GrowFromCenter(mark,
                               rate_func=rate_functions.ease_out_bounce)
                for mark in question_marks
            ],
                lag_ratio=0.2
            ))

        self.pause(2)

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
        width=1
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


def get_well(color: str) -> VGroup:
    well = Circle(radius=2, color=color)
    well.add(Circle(radius=1.5, color=color,
             fill_color=BLACK, fill_opacity=1, z_index=2))

    well.add(*[
        Line(ORIGIN, 2 * UP, color=color,
             z_index=1).rotate(i * TAU / 16, about_point=ORIGIN)
        for i in range(16)
    ])

    return well


class GraphTheoryExamples(Scene):
    def construct(self):
        house1 = VGroup(*get_house(HOUSE_COLOR)).scale(0.3).move_to(ORIGIN)
        house2 = house1.copy()
        house3 = house1.copy()

        self.play(AnimationGroup(
            AnimationGroup(
                AnimationGroup(*[Create(house1[i]) for i in range(2)]),
                AnimationGroup(*[Create(house1[i]) for i in range(2, 5)]),
                lag_ratio=0.5
            ),
            AnimationGroup(
                house2.animate.shift(4 * LEFT).set_stroke(opacity=1),
                house3.animate.shift(4 * RIGHT).set_stroke(opacity=1),
                run_time=1
            ),
            lag_ratio=0.6
        ))

        # well = get_well(WELL_COLOR)
        # self.add(well)

        self.pause(2)

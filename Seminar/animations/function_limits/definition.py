import numpy as np
import logging
from manim import *
from enum import Enum

from definition_config import *


class LimitDirection(Enum):
    LEFT = "left"
    RIGHT = "right"
    BOTH = "both"


def smooth_func(x):
    return -((np.sin(np.exp(x / 2))) ** 2) + 1


class Definition(Scene):
    def limit_expression(self, direction: LimitDirection) -> VGroup:
        if direction == LimitDirection.LEFT:
            limit_interval = MathTex(r"\forall x \in (a - \delta, a)")
        elif direction == LimitDirection.RIGHT:
            limit_interval = MathTex(r"\forall x \in (a, a + \delta)")
        elif direction == LimitDirection.BOTH:
            limit_interval = MathTex(r"\forall 0 < |x - a| < \delta")

        return VGroup(
            *[
                MathTex(r"\forall \epsilon > 0", substrings_to_isolate=[r"\epsilon"]),
                MathTex(r"\exists \delta > 0"),
                limit_interval,
                MathTex(r" : "),
                MathTex(r"|f(x) - L| < \epsilon"),
            ]
        ).arrange(RIGHT, buff=0.25)

    @property
    def axes(self) -> Axes:
        axes = Axes(
            x_range=[-0.5, 4],
            y_range=[-0.5, 2],
            x_length=10,
            y_length=5,
            axis_config={
                "color": BLUE,
                "include_ticks": False,
                "tip_width": 0.2,
                "tip_height": 0.3,
            },
        )
        return axes

    def axes_labels(self, axes: Axes) -> VGroup:
        x_label = axes.get_x_axis_label(MathTex("x", color=Colors.time))
        y_label = axes.get_y_axis_label(MathTex("f(x)", color=Colors.graph))

        x_label.next_to(axes.x_axis.get_right(), DOWN)
        y_label.next_to(axes.y_axis.get_top(), LEFT)
        return VGroup(x_label, y_label)

    def highlight_and_recolor(self, eq: VMobject, letter: str, new_color) -> VMobject:
        return AnimationGroup(
            Circumscribe(eq[eq.index_of_part_by_tex(letter)], color=new_color),
            eq.animate.set_color_by_tex(letter, new_color),
            run_time=1.5,
        )

    def construct(self):
        # Formal definition
        self.next_section("Expression", skip_animations=SkipSectionAnims.formal)
        expression = self.limit_expression(LimitDirection.LEFT)
        self.play(Write(expression))

        self.play(expression.animate.to_edge(UP))

        # Graph
        self.next_section("Function graph", skip_animations=SkipSectionAnims.graph)
        axes = self.axes.to_edge(DOWN)
        axes_labels = self.axes_labels(axes)
        graph = axes.plot(smooth_func, x_range=[0, 3.5], color=Colors.graph)

        self.play(self.highlight_and_recolor(expression[0], r"\epsilon", TEAL))

        anims = AnimationGroup(
            FadeIn(axes),
            Write(axes_labels),
            Create(graph, rate_func=rate_functions.ease_in_out_expo, run_time=3),
            lag_ratio=0.4,
        )
        self.play(anims)

        self.wait()

import numpy as np
from manim import *


class Skips:
    graph = True
    interval_division = False


def function(x):
    x = 0.3 * x
    return 2 * (
        -2 * (x - 1) ** 5 - (x - 1) ** 4 + 2 * (x - 1) ** 3 - (x - 1) ** 2 + x + 1
    )


class Riemann(Scene):
    def get_axes(self):
        axes = Axes(
            x_range=[-1, 7],
            y_range=[-1, 7],
            tips=False,
            axis_config={"color": WHITE},
        ).to_edge(LEFT, buff=1)
        return axes

    def construct(self):
        self.next_section("Graph", skip_animations=Skips.graph)

        axes = self.get_axes()
        self.play(Create(axes))

        # Draw graph
        graph = axes.plot(function, color=TEAL, x_range=[0, 7])
        self.play(Create(graph))

        self.wait()

        self.next_section("Interval division", skip_animations=Skips.interval_division)

        # Choose a,b
        a = ValueTracker(2)
        b = ValueTracker(5)

        a_dot = Dot(axes.coords_to_point(a.get_value(), 0), color=YELLOW)
        b_dot = Dot(axes.coords_to_point(b.get_value(), 0), color=YELLOW)

        a_label = MathTex("a", color=YELLOW).next_to(a_dot, DOWN)
        b_label = MathTex("b", color=YELLOW).next_to(b_dot, DOWN)

        fa = function(a.get_value())
        fb = function(b.get_value())

        fa_dot = Dot(axes.coords_to_point(a.get_value(), fa), color=YELLOW)
        fb_dot = Dot(axes.coords_to_point(b.get_value(), fb), color=YELLOW)

        fa_label = MathTex("f(a)", color=YELLOW).next_to(fa_dot, UP)
        fb_label = MathTex("f(b)", color=YELLOW).next_to(fb_dot, UP)

        a_line = Line(a_dot, fa_dot, color=YELLOW, stroke_width=2)
        b_line = Line(b_dot, fb_dot, color=YELLOW, stroke_width=2)

        self.play(
            AnimationGroup(
                AnimationGroup(
                    Create(a_dot),
                    Create(b_dot),
                    Write(a_label),
                    Write(b_label),
                    lag_ratio=0,
                ),
                AnimationGroup(
                    Create(fa_dot),
                    Create(fb_dot),
                    Write(fa_label),
                    Write(fb_label),
                    lag_ratio=0,
                ),
                AnimationGroup(Create(a_line), Create(b_line), lag_ratio=0),
                lag_ratio=0.6,
            )
        )

        self.wait()

        # Interval division
        div_points = [int(x) for x in np.arange(a.get_value(), b.get_value(), 1)][1:]
        div_dots = [Dot(axes.coords_to_point(x, 0), color=PINK) for x in div_points]
        fdiv_dots = [
            Dot(axes.coords_to_point(x, function(x)), color=PINK) for x in div_points
        ]
        div_labels = [
            MathTex(f"x_{i + 1}", color=PINK).next_to(div_dots[i], DOWN)
            for i in range(len(div_points))
        ]

        self.play(
            *[Create(dot) for dot in div_dots], *[Write(label) for label in div_labels]
        )

        start_label = (
            MathTex("x_0 =", color=PINK).next_to(a_label, LEFT).shift(0.05 * DOWN)
        )
        end_label = (
            MathTex("= x_3", color=PINK).next_to(b_label, RIGHT).shift(0.05 * DOWN)
        )

        self.play(
            FadeIn(start_label, shift=LEFT),
            FadeIn(end_label, shift=RIGHT),
        )

        self.wait()

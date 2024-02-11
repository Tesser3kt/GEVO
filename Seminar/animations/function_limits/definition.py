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
            limit_interval = MathTex(
                r"\forall",
                "x",
                r"\in",
                "(",
                "a",
                "-",
                r"\delta",
                ",",
                "a",
                ")",
            )
        elif direction == LimitDirection.RIGHT:
            limit_interval = MathTex(
                r"\forall",
                "x",
                r"\in",
                "(",
                "a",
                ",",
                "a",
                "+",
                r"\delta",
                ")",
            )
        elif direction == LimitDirection.BOTH:
            limit_interval = MathTex(
                r"\forall",
                "0",
                "<",
                "|",
                "x",
                "-",
                "a",
                "|",
                "<",
                r"\delta",
            )

        return VGroup(
            *[
                MathTex(r"\forall", r"\epsilon", ">", "0"),
                MathTex(r"\exists", r"\delta", ">", "0"),
                limit_interval,
                MathTex(":"),
                MathTex("|", "f(x)", "-", "L", "|", "<", r"\epsilon"),
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

    def highlight_and_recolor(
        self, eq: VMobject, rng: tuple[int, int], new_color
    ) -> VMobject:
        return AnimationGroup(
            Circumscribe(eq[rng[0] : rng[1]], color=new_color),
            eq[rng[0] : rng[1]].animate.set_color(new_color),
            run_time=1.5,
        )

    def construct(self):
        # Updaters

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

        self.play(
            self.highlight_and_recolor(expression[2], (1, 2), Colors.time),
            self.highlight_and_recolor(expression[4], (1, 2), Colors.graph),
        )

        anims = AnimationGroup(
            FadeIn(axes),
            Write(axes_labels),
            Create(graph, rate_func=rate_functions.ease_in_out_expo, run_time=3),
            lag_ratio=0.4,
        )
        self.play(anims)

        # Point and limit
        self.next_section(
            "Point and limit", skip_animations=SkipSectionAnims.point_and_limit
        )

        # Highlight point
        self.play(
            self.highlight_and_recolor(expression[2], (4, 5), Colors.point),
            self.highlight_and_recolor(expression[2], (8, 9), Colors.point),
        )

        # Create point with updaters
        a = ValueTracker(2)
        point = Dot(
            axes.coords_to_point(a.get_value(), smooth_func(a.get_value())),
            color=Colors.point,
        ).add_updater(
            lambda m: m.move_to(
                axes.coords_to_point(a.get_value(), smooth_func(a.get_value()))
            )
        )
        line_to_point = DashedLine(
            point, axes.coords_to_point(a.get_value(), 0), color=Colors.point
        ).add_updater(
            lambda m: m.put_start_and_end_on(
                point.get_center(), axes.coords_to_point(a.get_value(), 0)
            )
        )
        point_label = (
            MathTex("a", color=Colors.point)
            .next_to(axes.coords_to_point(a.get_value(), 0), DOWN, buff=0.2)
            .add_updater(
                lambda m: m.next_to(
                    axes.coords_to_point(a.get_value(), 0), DOWN, buff=0.2
                )
            )
        )

        anims = AnimationGroup(
            Create(point),
            Create(line_to_point),
            Write(point_label),
            lag_ratio=0.7,
        )
        self.play(anims)

        self.wait()

        # Create limit with updaters
        limit_point = Circle(radius=0.15, color=Colors.limit).move_to(
            point.get_center()
        )
        L = ValueTracker(smooth_func(a.get_value()))
        line_to_limit = DashedLine(
            point,
            axes.coords_to_point(0, L.get_value()),
            color=Colors.limit,
        ).add_updater(
            lambda m: m.put_start_and_end_on(
                point.get_center(), axes.coords_to_point(0, L.get_value())
            )
        )
        limit_label = (
            MathTex("L", color=Colors.limit)
            .next_to(axes.coords_to_point(0, L.get_value()), LEFT, buff=0.2)
            .add_updater(
                lambda m: m.next_to(
                    axes.coords_to_point(0, L.get_value()), LEFT, buff=0.2
                )
            )
        )

        self.play(
            self.highlight_and_recolor(expression[4], (3, 4), Colors.limit),
        )
        anims = AnimationGroup(
            Create(limit_point),
            Create(line_to_limit),
            Write(limit_label),
            lag_ratio=0.7,
        )
        self.play(anims)

        # Epsilon
        # Preparing delta for easier computation
        delta = ValueTracker(0.3)

        self.next_section("Epsilon", skip_animations=SkipSectionAnims.epsilon)
        epsilon = ValueTracker(
            abs(
                smooth_func(a.get_value())
                - smooth_func(a.get_value() - delta.get_value())
            )
        ).add_updater(
            lambda m: m.set_value(
                abs(
                    smooth_func(a.get_value())
                    - smooth_func(a.get_value() - delta.get_value())
                )
            )
        )

        # Highlight epsilon
        self.play(
            self.highlight_and_recolor(expression[0], (1, 2), Colors.epsilon),
            self.highlight_and_recolor(expression[-1], (6, 7), Colors.epsilon),
        )

        # Show epsilon interval
        epsilon_points = (
            axes.coords_to_point(0, smooth_func(a.get_value()) + epsilon.get_value()),
            axes.coords_to_point(0, smooth_func(a.get_value()) - epsilon.get_value()),
        )
        epsilon_dots = (
            Dot(epsilon_points[0], radius=0.08, color=Colors.epsilon),
            Dot(epsilon_points[1], radius=0.08, color=Colors.epsilon),
        )
        epsilon_interval = Line(
            *epsilon_points,
            color=Colors.epsilon,
            stroke_width=6,
        ).add_updater(
            lambda m: m.put_start_and_end_on(
                axes.coords_to_point(
                    0, smooth_func(a.get_value()) + epsilon.get_value()
                ),
                axes.coords_to_point(
                    0, smooth_func(a.get_value()) - epsilon.get_value()
                ),
            )
        )
        self.play(
            Create(epsilon_interval), Create(epsilon_dots[0]), Create(epsilon_dots[1])
        )
        self.play(
            epsilon.animate.set_value(0.1),
        )

        self.wait()

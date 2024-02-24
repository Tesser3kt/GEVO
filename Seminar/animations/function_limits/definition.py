import numpy as np
import logging
from manim import *
from enum import Enum
from scipy.optimize import fsolve

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

    def epsilon_intersection(self, a: float, epsilon: float) -> float:
        return fsolve(lambda x: smooth_func(x) - epsilon, a)[0]

    def construct(self):
        # Updaters

        # Formal definition
        self.next_section("Expression", skip_animations=SkipSectionAnims.formal)
        expression = self.limit_expression(LimitDirection.LEFT)
        self.play(Write(expression))

        self.play(expression.animate.to_edge(UP))

        self.wait()

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

        self.wait()

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
        L = ValueTracker(smooth_func(a.get_value())).add_updater(
            lambda m: m.set_value(smooth_func(a.get_value()))
        )
        limit_point = (
            Circle(radius=0.15, color=Colors.limit)
            .move_to(point.get_center())
            .add_updater(lambda m: m.move_to(point.get_center()))
        )
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

        self.wait()

        self.next_section("Epsilon", skip_animations=SkipSectionAnims.epsilon)
        epsilon = ValueTracker(
            abs(
                smooth_func(a.get_value())
                - smooth_func(a.get_value() - delta.get_value())
            )
        )

        # Highlight epsilon
        self.play(
            self.highlight_and_recolor(expression[0], (1, 2), Colors.epsilon),
            self.highlight_and_recolor(expression[-1], (6, 7), Colors.epsilon),
        )

        # Show epsilon interval
        epsilon_dots = VGroup(
            Dot(
                axes.coords_to_point(
                    0, smooth_func(a.get_value()) + epsilon.get_value()
                ),
                radius=0.08,
                color=Colors.epsilon,
            ).add_updater(
                lambda m: m.move_to(
                    axes.coords_to_point(
                        0, smooth_func(a.get_value()) + epsilon.get_value()
                    )
                )
            ),
            Dot(
                axes.coords_to_point(
                    0, smooth_func(a.get_value()) - epsilon.get_value()
                ),
                radius=0.08,
                color=Colors.epsilon,
            ).add_updater(
                lambda m: m.move_to(
                    axes.coords_to_point(
                        0, smooth_func(a.get_value()) - epsilon.get_value()
                    )
                )
            ),
        )
        epsilon_interval = Line(
            *[dot.get_center() for dot in epsilon_dots],
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

        epsilon_labels = VGroup(
            MathTex(r"L + \epsilon", color=Colors.epsilon, font_size=36)
            .next_to(
                axes.coords_to_point(
                    0, smooth_func(a.get_value()) + epsilon.get_value()
                ),
                LEFT,
                buff=0.2,
            )
            .add_updater(
                lambda m: m.next_to(
                    axes.coords_to_point(
                        0, smooth_func(a.get_value()) + epsilon.get_value()
                    ),
                    LEFT,
                    buff=0.2,
                )
            ),
            MathTex(r"L - \epsilon", color=Colors.epsilon, font_size=36)
            .next_to(
                axes.coords_to_point(
                    0, smooth_func(a.get_value()) - epsilon.get_value()
                ),
                LEFT,
                buff=0.2,
            )
            .add_updater(
                lambda m: m.next_to(
                    axes.coords_to_point(
                        0, smooth_func(a.get_value()) - epsilon.get_value()
                    ),
                    LEFT,
                    buff=0.2,
                )
            ),
        )
        self.play(Write(epsilon_labels))

        epsilon_lines = VGroup(
            DashedLine(
                epsilon_dots[0].get_center(),
                epsilon_dots[0].get_center() + 8 * RIGHT,
                color=Colors.epsilon,
                dashed_ratio=0.3,
            )
            .set_opacity(0.7)
            .add_updater(
                lambda m: m.put_start_and_end_on(
                    epsilon_dots[0].get_center(),
                    epsilon_dots[0].get_center() + 8 * RIGHT,
                )
            ),
            DashedLine(
                epsilon_dots[1].get_center(),
                epsilon_dots[1].get_center() + 8 * RIGHT,
                color=Colors.epsilon,
                dashed_ratio=0.3,
            )
            .set_opacity(0.7)
            .add_updater(
                lambda m: m.put_start_and_end_on(
                    epsilon_dots[1].get_center(),
                    epsilon_dots[1].get_center() + 8 * RIGHT,
                )
            ),
        )
        epsilon_strip = Rectangle(
            width=8,
            height=4 * epsilon.get_value(),
            color=Colors.epsilon,
            fill_opacity=0.1,
            stroke_width=0,
        ).move_to(
            axes.coords_to_point(0, smooth_func(a.get_value())), aligned_edge=LEFT
        )

        self.play(
            Create(epsilon_lines[0]), Create(epsilon_lines[1]), FadeIn(epsilon_strip)
        )

        self.wait()

        # Delta
        self.next_section("Delta", skip_animations=SkipSectionAnims.delta)

        # Highlight delta
        self.play(
            self.highlight_and_recolor(expression[1], (1, 2), Colors.delta),
            self.highlight_and_recolor(expression[2], (6, 7), Colors.delta),
        )

        # Show delta interval
        delta_dot = Dot(
            axes.coords_to_point(a.get_value() - delta.get_value(), 0),
            radius=0.08,
            color=Colors.delta,
        ).add_updater(
            lambda m: m.move_to(
                axes.coords_to_point(a.get_value() - delta.get_value(), 0)
            )
        )
        delta_interval = Line(
            delta_dot.get_center(),
            axes.coords_to_point(a.get_value(), 0),
            color=Colors.delta,
            stroke_width=6,
        ).add_updater(
            lambda m: m.put_start_and_end_on(
                delta_dot.get_center(), axes.coords_to_point(a.get_value(), 0)
            )
        )

        delta_line = DashedLine(
            axes.coords_to_point(
                a.get_value() - delta.get_value(),
                smooth_func(a.get_value() - delta.get_value()),
            ),
            delta_dot.get_center(),
            color=Colors.delta,
            dashed_ratio=0.4,
        ).add_updater(
            lambda m: m.put_start_and_end_on(
                axes.coords_to_point(
                    a.get_value() - delta.get_value(),
                    smooth_func(a.get_value() - delta.get_value()),
                ),
                delta_dot.get_center(),
            )
        )

        self.play(Create(delta_line))

        a_dot = Dot(
            axes.coords_to_point(a.get_value(), 0),
            radius=0.08,
            color=Colors.point,
            z_index=10,
        ).add_updater(lambda m: m.move_to(axes.coords_to_point(a.get_value(), 0)))
        delta_line.suspend_updating()
        self.play(
            Create(delta_dot),
            Create(delta_interval),
            Create(a_dot),
            Unwrite(point_label),
        )
        delta_line.resume_updating()

        delta_label = (
            MathTex(r"a - \delta", color=Colors.delta, font_size=36)
            .next_to(delta_dot, DOWN, buff=0.2)
            .add_updater(lambda m: m.next_to(delta_dot, DOWN, buff=0.1))
        )
        self.play(Write(delta_label))

        self.wait()

        # Moving epsilon
        self.next_section(
            "Moving epsilon", skip_animations=SkipSectionAnims.moving_epsilon
        )

        new_epsilon = abs(smooth_func(a.get_value()) - smooth_func(a.get_value() - 0.2))
        epsilon_strip.generate_target()
        epsilon_strip.target = Rectangle(
            width=8,
            height=4 * new_epsilon,
            color=Colors.epsilon,
            fill_opacity=0.1,
            stroke_width=0,
        ).move_to(
            axes.coords_to_point(0, smooth_func(a.get_value())), aligned_edge=LEFT
        )
        self.play(
            epsilon.animate.set_value(new_epsilon),
            *[dot.animate.update() for dot in epsilon_dots],
            MoveToTarget(epsilon_strip),
            delta.animate.set_value(0.2),
            delta_line.animate.update(),
            run_time=3,
        )

        new_epsilon = abs(smooth_func(a.get_value()) - smooth_func(a.get_value() - 0.5))
        epsilon_strip.generate_target()
        epsilon_strip.target = Rectangle(
            width=8,
            height=4 * new_epsilon,
            color=Colors.epsilon,
            fill_opacity=0.1,
            stroke_width=0,
        ).move_to(
            axes.coords_to_point(0, smooth_func(a.get_value())), aligned_edge=LEFT
        )
        self.play(
            epsilon.animate.set_value(new_epsilon),
            *[dot.animate.update() for dot in epsilon_dots],
            MoveToTarget(epsilon_strip),
            delta.animate.set_value(0.5),
            delta_line.animate.update(),
            run_time=3,
        )

        new_epsilon = abs(smooth_func(a.get_value()) - smooth_func(a.get_value() - 0.3))
        epsilon_strip.generate_target()
        epsilon_strip.target = Rectangle(
            width=8,
            height=4 * new_epsilon,
            color=Colors.epsilon,
            fill_opacity=0.1,
            stroke_width=0,
        ).move_to(
            axes.coords_to_point(0, smooth_func(a.get_value())), aligned_edge=LEFT
        )
        self.play(
            epsilon.animate.set_value(new_epsilon),
            *[dot.animate.update() for dot in epsilon_dots],
            MoveToTarget(epsilon_strip),
            delta.animate.set_value(0.3),
            delta_line.animate.update(),
            run_time=3,
        )

        self.wait()

        # Moving a
        self.next_section("Moving a", skip_animations=SkipSectionAnims.moving_a)

        epsilon_strip.add_updater(
            lambda m: m.move_to(
                axes.coords_to_point(0, smooth_func(a.get_value())), aligned_edge=LEFT
            )
        )
        # Epsilon intersection calculation

        delta_dot.clear_updaters()
        delta_line.clear_updaters()

        delta_dot.add_updater(
            lambda m: m.move_to(
                axes.coords_to_point(
                    self.epsilon_intersection(1.5, L.get_value() - epsilon.get_value()),
                    0,
                )
            )
        )
        delta_line.add_updater(
            lambda m: m.put_start_and_end_on(
                axes.coords_to_point(
                    self.epsilon_intersection(1.5, L.get_value() - epsilon.get_value()),
                    smooth_func(
                        self.epsilon_intersection(
                            1.5, L.get_value() - epsilon.get_value()
                        )
                    ),
                ),
                delta_dot.get_center(),
            )
        )

        # Move a
        self.play(
            a.animate.set_value(2.3),
            L.animate.update(),
            delta_dot.animate.update(),
            delta_line.animate.update(),
            run_time=3,
        )

        self.play(
            a.animate.set_value(2.6),
            L.animate.update(),
            delta_dot.animate.update(),
            delta_line.animate.update(),
            run_time=3,
        )

        self.play(
            a.animate.set_value(1.7),
            L.animate.update(),
            delta_dot.animate.update(),
            delta_line.animate.update(),
            run_time=3,
        )

        self.play(
            a.animate.set_value(2),
            L.animate.update(),
            delta_dot.animate.update(),
            delta_line.animate.update(),
            run_time=3,
        )

        self.wait()

        # Right limit
        self.next_section("Right limit", skip_animations=SkipSectionAnims.right_limit)

        right_limit = self.limit_expression(LimitDirection.RIGHT).to_edge(UP)
        right_limit[2][1].set_color(Colors.time)
        right_limit[4][1].set_color(Colors.graph)
        right_limit[2][4].set_color(Colors.point)
        right_limit[2][8].set_color(Colors.point)
        right_limit[4][3].set_color(Colors.limit)
        right_limit[0][1].set_color(Colors.epsilon)
        right_limit[-1][6].set_color(Colors.epsilon)
        right_limit[1][1].set_color(Colors.delta)
        right_limit[2][6].set_color(Colors.delta)

        self.play(Transform(expression, right_limit))

        delta_dot.clear_updaters()
        delta_line.clear_updaters()

        new_point = axes.coords_to_point(
            self.epsilon_intersection(3, L.get_value() - epsilon.get_value()),
            0,
        )

        delta_dot.add_updater(
            lambda m: m.move_to(
                axes.coords_to_point(
                    self.epsilon_intersection(3, L.get_value() - epsilon.get_value()),
                    0,
                )
            )
        )
        new_delta_line = delta_line.copy().add_updater(
            lambda m: m.put_start_and_end_on(
                axes.coords_to_point(
                    self.epsilon_intersection(3, L.get_value() - epsilon.get_value()),
                    smooth_func(
                        self.epsilon_intersection(
                            3, L.get_value() - epsilon.get_value()
                        )
                    ),
                ),
                delta_dot.get_center(),
            )
        )

        new_delta_line.update()
        delta_dot.suspend_updating()

        self.play(Uncreate(delta_line))
        self.play(
            delta_dot.animate.move_to(new_point),
            Create(new_delta_line),
            run_time=2,
        )
        delta_label.suspend_updating()
        self.play(
            Transform(
                delta_label,
                MathTex(r"a + \delta", color=Colors.delta, font_size=36).next_to(
                    delta_dot, DOWN, buff=0.1
                ),
            )
        )
        delta_label.resume_updating()

        self.wait()

        # Both limits
        self.next_section("Both limits", skip_animations=SkipSectionAnims.both_limits)

        both_limit = self.limit_expression(LimitDirection.BOTH).to_edge(UP)
        both_limit[2][4].set_color(Colors.time)
        both_limit[4][1].set_color(Colors.graph)
        both_limit[2][6].set_color(Colors.point)
        both_limit[4][3].set_color(Colors.limit)
        both_limit[0][1].set_color(Colors.epsilon)
        both_limit[-1][6].set_color(Colors.epsilon)
        both_limit[1][1].set_color(Colors.delta)
        both_limit[2][-1].set_color(Colors.delta)

        self.play(Transform(expression, both_limit))

        left_delta_dot = delta_dot.copy().clear_updaters()
        left_delta_line = new_delta_line.copy().clear_updaters()

        left_delta_dot.add_updater(
            lambda m: m.move_to(
                axes.coords_to_point(
                    self.epsilon_intersection(1.5, L.get_value() - epsilon.get_value()),
                    0,
                )
            )
        )
        left_delta_line.add_updater(
            lambda m: m.put_start_and_end_on(
                axes.coords_to_point(
                    self.epsilon_intersection(1.5, L.get_value() - epsilon.get_value()),
                    smooth_func(
                        self.epsilon_intersection(
                            1.5, L.get_value() - epsilon.get_value()
                        )
                    ),
                ),
                left_delta_dot.get_center(),
            )
        )
        left_delta_label = (
            MathTex(r"a - \delta", color=Colors.delta, font_size=36)
            .next_to(left_delta_dot, DOWN, buff=0.1)
            .add_updater(lambda m: m.next_to(left_delta_dot, DOWN, buff=0.1))
        )
        left_delta_interval = Line(
            left_delta_dot.get_center(),
            axes.coords_to_point(a.get_value(), 0),
            color=Colors.delta,
            stroke_width=6,
        ).add_updater(
            lambda m: m.put_start_and_end_on(
                left_delta_dot.get_center(), axes.coords_to_point(a.get_value(), 0)
            )
        )

        self.play(
            Create(left_delta_dot),
            Create(left_delta_line),
        )
        self.play(Write(left_delta_label), Create(left_delta_interval))

        delta_dot.clear_updaters()
        delta = a.get_value() - self.epsilon_intersection(
            1.5, L.get_value() - epsilon.get_value()
        )
        new_delta_line.clear_updaters()

        self.play(
            delta_dot.animate.move_to(axes.coords_to_point(a.get_value() + delta, 0)),
            Uncreate(new_delta_line),
            Create(
                DashedLine(
                    axes.coords_to_point(
                        a.get_value() + delta,
                        smooth_func(a.get_value() + delta),
                    ),
                    axes.coords_to_point(a.get_value() + delta, 0),
                    color=Colors.delta,
                    dashed_ratio=0.4,
                )
            ),
        )

        self.wait()

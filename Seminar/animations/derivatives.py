import numpy as np
from manim import *


class Derivatives(MovingCameraScene):
    def construct(self):
        def f(x):
            return x * np.sin(x**2) + 1

        self.next_section("f", skip_animations=False)

        axes = Axes(
            x_range=[-1, 3],
            y_range=[-1, 3],
            axis_config={"color": BLUE},
        )
        self.play(Create(axes))

        graph = axes.plot(f, color=WHITE)
        graph_label = axes.get_graph_label(graph, label="f(x)", direction=DOWN)
        self.play(Create(graph), Write(graph_label), run_time=1.5)

        self.wait()

        self.next_section("f growth", skip_animations=False)

        a = ValueTracker(1)
        h = ValueTracker(0.4)

        a_dot = Dot(radius=0.12, color=ORANGE, z_index=2).move_to(
            axes.c2p(a.get_value(), 0)
        )
        a_label = MathTex("a", color=ORANGE).next_to(a_dot, DOWN)

        self.play(Create(a_dot), Write(a_label))

        a_dot.add_updater(lambda x: x.move_to(axes.c2p(a.get_value(), 0)))
        a_label.add_updater(lambda x: x.next_to(a_dot, DOWN))

        fa_dot = Dot(radius=0.12, color=ORANGE).move_to(
            axes.c2p(a.get_value(), f(a.get_value()))
        )
        a_fa = DashedLine(a_dot.get_center(), fa_dot.get_center(), color=ORANGE)

        self.play(
            AnimationGroup(
                Create(a_fa),
                Create(fa_dot),
                lag_ratio=0.5,
            )
        )

        fa_dot.add_updater(
            lambda x: x.move_to(axes.c2p(a.get_value(), f(a.get_value())))
        )
        a_fa.add_updater(
            lambda x: x.put_start_and_end_on(a_dot.get_center(), fa_dot.get_center())
        )

        a_h = Line(
            axes.c2p(a.get_value(), 0),
            axes.c2p(a.get_value() + h.get_value(), 0),
            color=TEAL,
            z_index=0,
            stroke_width=6,
        )
        h_dot = Dot(radius=0.12, color=TEAL).move_to(
            axes.c2p(a.get_value() + h.get_value(), 0)
        )
        h_label = MathTex("h", color=TEAL).next_to(a_h.get_center(), UP, buff=0.1)

        self.play(
            AnimationGroup(
                Create(a_h),
                AnimationGroup(Create(h_dot), Write(h_label), lag_ratio=0),
                lag_ratio=0.5,
            )
        )

        a_h.add_updater(
            lambda x: x.put_start_and_end_on(
                axes.c2p(a.get_value(), 0), axes.c2p(a.get_value() + h.get_value(), 0)
            )
        )
        h_dot.add_updater(
            lambda x: x.move_to(axes.c2p(a.get_value() + h.get_value(), 0))
        )
        h_label.add_updater(lambda x: x.next_to(a_h.get_center(), UP, buff=0.1))

        fh_dot = Dot(radius=0.12, color=TEAL).move_to(
            axes.c2p(a.get_value() + h.get_value(), f(a.get_value() + h.get_value()))
        )
        h_fh = DashedLine(h_dot.get_center(), fh_dot.get_center(), color=TEAL)

        self.play(
            AnimationGroup(
                Create(h_fh),
                Create(fh_dot),
                lag_ratio=0.5,
            )
        )

        ya_dot = Dot(radius=0.12, color=ORANGE, z_index=1).move_to(
            axes.c2p(0, f(a.get_value()))
        )
        yh_dot = Dot(radius=0.12, color=TEAL, z_index=1).move_to(
            axes.c2p(0, f(a.get_value() + h.get_value()))
        )

        ya_line = DashedLine(fa_dot.get_center(), ya_dot.get_center(), color=ORANGE)
        yh_line = DashedLine(fh_dot.get_center(), yh_dot.get_center(), color=TEAL)

        self.play(
            AnimationGroup(
                Create(ya_line),
                Create(yh_line),
                lag_ratio=0,
            ),
            AnimationGroup(
                Create(ya_dot),
                Create(yh_dot),
                lag_ratio=0,
            ),
            lag_ratio=0.5,
        )

        ya_dot.add_updater(lambda x: x.move_to(axes.c2p(0, f(a.get_value()))))
        yh_dot.add_updater(
            lambda x: x.move_to(axes.c2p(0, f(a.get_value() + h.get_value())))
        )
        ya_line.add_updater(
            lambda x: x.put_start_and_end_on(fa_dot.get_center(), ya_dot.get_center())
        )
        yh_line.add_updater(
            lambda x: x.put_start_and_end_on(fh_dot.get_center(), yh_dot.get_center())
        )

        ya_label = MathTex("f(a)", color=ORANGE).next_to(ya_dot, LEFT)
        yh_label = MathTex("f(a+h)", color=TEAL).next_to(yh_dot, LEFT)

        y_labels = VGroup(ya_label, yh_label)

        self.play(Write(ya_label), Write(yh_label))

        self.wait()

        ya_yh = Line(
            ya_dot.get_center(),
            yh_dot.get_center(),
            color=PINK,
            z_index=0,
            stroke_width=6,
        )
        brace = Brace(ya_yh, direction=LEFT, color=PINK)
        ya_yh_label = MathTex("f(a+h) - f(a)", color=PINK).next_to(brace, LEFT)

        self.play(
            Create(ya_yh),
        )
        self.play(
            Write(brace),
            ReplacementTransform(y_labels, ya_yh_label),
        )

        self.wait()

        self.next_section("g", skip_animations=False)

        g_text = MathTex(
            "g_a(h) = \\text{nárůst } f \\text{ od bodu } a \\text{ za čas } h",
            color=YELLOW,
        )
        g_text.to_edge(UP)

        self.play(Write(g_text))

        self.wait()

        g_text.generate_target()
        g_text.target = MathTex(
            r"g_a(h)",
            r"=",
            r"\frac{ f(a+h) - f(a) }{ h }",
            color=YELLOW,
        ).to_edge(UP)

        g_text.target[2][0:11].set_color(PINK)
        g_text.target[2][12:17].set_color(TEAL)

        self.play(MoveToTarget(g_text))

        self.wait()

        def g(a, h):
            return (f(a + h) - f(a)) / h

        g_graph_right = axes.plot(
            lambda x: g(a.get_value(), x), color=YELLOW, x_range=[0.01, 3]
        )
        g_graph_left = axes.plot(
            lambda x: g(a.get_value(), x), color=YELLOW, x_range=[-3, -0.01]
        )
        g_not_def = Circle(
            radius=0.15, color=RED, fill_opacity=1, fill_color=BLACK
        ).move_to(axes.c2p(0, np.sin(1) + 2 * np.cos(1)))
        g_label = axes.get_graph_label(g_graph_right, label="g_a(h)", direction=DOWN)

        self.play(
            Create(g_graph_left),
            Create(g_graph_right),
            DrawBorderThenFill(g_not_def),
            Write(g_label),
            FadeOut(
                a,
                a_dot,
                a_label,
                a_fa,
                fa_dot,
                a_h,
                h_dot,
                h_label,
                h_fh,
                fh_dot,
                ya_dot,
                yh_dot,
                ya_line,
                yh_line,
                ya_label,
                yh_label,
                ya_yh,
                brace,
                ya_yh_label,
            ),
        )

        lim_text = (
            MathTex(
                r"\lim_{h \to 0}",
                color=RED,
            )
            .next_to(g_text[2], LEFT, buff=0.1)
            .shift(0.18 * DOWN)
        )
        lim_text_2 = (
            lim_text.copy().next_to(g_text[0], LEFT).shift(0.8 * LEFT + 0.18 * DOWN)
        )

        self.play(
            Write(lim_text),
            Write(lim_text_2),
            g_text[0].animate.shift(0.8 * LEFT),
            g_text[1].animate.shift(0.8 * LEFT),
        )

        derivative_text = (
            MathTex(
                r"f'(a) = ",
                color=RED,
            )
            .next_to(lim_text_2, LEFT, buff=0.1)
            .shift(0.18 * UP)
        )

        self.play(Write(derivative_text))

        self.wait()

        def fx(x):
            return 2 * x**2 * np.cos(x**2) + np.sin(x**2)

        x = ValueTracker(0)
        w = DecimalNumber(fx(x.get_value()), color=RED).next_to(
            derivative_text, RIGHT, buff=0.1
        )
        w.add_updater(lambda m: m.set_value(x.get_value()))

        x_dot = (
            Dot(radius=0.12, color=RED)
            .move_to(axes.c2p(x.get_value(), f(x.get_value())))
            .add_updater(lambda m: m.move_to(axes.c2p(x.get_value(), f(x.get_value()))))
        )
        tangent = axes.plot(
            lambda a: f(x.get_value()) + fx(x.get_value()) * (a - x.get_value()),
            color=RED,
            x_range=[x.get_value() - 0.5, x.get_value() + 0.5],
            stroke_width=6,
        ).add_updater(
            lambda m: m.become(
                axes.plot(
                    lambda a: f(x.get_value())
                    + fx(x.get_value()) * (a - x.get_value()),
                    color=RED,
                    x_range=[x.get_value() - 0.5, x.get_value() + 0.5],
                    stroke_width=6,
                )
            )
        )
        self.play(
            FadeOut(
                g_graph_left,
                g_graph_right,
                g_not_def,
                lim_text,
                lim_text_2,
                g_text,
                g_label,
            ),
            Write(w),
            DrawBorderThenFill(x_dot),
            Create(tangent),
        )

        self.wait()

        self.play(
            x.animate.set_value(1),
            run_time=3,
        )

        self.wait()

        self.play(
            x.animate.set_value(2),
            run_time=3,
        )

        self.wait()

        self.play(
            x.animate.set_value(2.5),
            run_time=3,
        )

        self.wait()

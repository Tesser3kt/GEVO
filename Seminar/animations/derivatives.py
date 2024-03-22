import numpy as np
from manim import *


class Derivatives(MovingCameraScene):
    def construct(self):
        def f(x):
            return x * np.sin(x**2) + 1

        self.next_section("f", skip_animations=True)

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

        self.next_section("f growth", skip_animations=True)

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

        g_graph = axes.plot(
            lambda x: g(a.get_value(), x), color=YELLOW, x_range=[0.01, 2]
        )
        g_label = axes.get_graph_label(g_graph, label="g_a(h)", direction=DOWN)

        self.play(self.camera.)

        self.play(Create(g_graph), Write(g_label))

        self.wait()

        g_equals = MathTex("=", color=YELLOW).next_to(g_text, RIGHT).shift(0.05 * DOWN)
        g_value = DecimalNumber(
            g(a.get_value(), h.get_value()), num_decimal_places=2, color=YELLOW
        ).next_to(g_equals, RIGHT)

        self.play(
            Write(g_equals),
            Write(g_value),
        )

        g_value.add_updater(lambda x: x.set_value(g(a.get_value(), h.get_value())))
        self.wait()

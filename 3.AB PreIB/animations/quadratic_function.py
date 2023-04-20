from manim import *


class QuadraticFunction(Scene):
    def construct(self):
        axes = Axes(
            x_range=[-4, 4, 1],
            y_range=[-4, 4, 1],
            x_length=8,
            y_length=8
        ).add_coordinates()
        axes_labels = axes.get_axis_labels(x_label="x", y_label="y")
        self.play(Create(axes), Write(axes_labels))

        # linear function
        a_tracker = ValueTracker(1)
        b_tracker = ValueTracker(0)

        def update_graph(mob):
            a = a_tracker.get_value()
            b = b_tracker.get_value()
            mob.become(axes.plot(lambda x: a * x + b, x_range=[-5, 5],
                                 color=BLUE))
        linear = VMobject()

        update_graph(linear)
        linear.add_updater(update_graph)

        f_label = MathTex("f(x) = ", "a", "x", " + ", "b", color=BLUE,
                          substrings_to_isolate=["a", "b"],
                          tex_to_color_map={
                                "a": RED,
                                "b": GREEN
                          }).to_corner(UP + LEFT)
        a_label = MathTex("a = ", color=RED).next_to(f_label, DOWN,
                                                     aligned_edge=LEFT)
        b_label = MathTex("b = ", color=GREEN).next_to(a_label, DOWN,
                                                       aligned_edge=LEFT)
        a_value = DecimalNumber(a_tracker.get_value(), num_decimal_places=2,
                                color=RED).next_to(a_label, RIGHT)
        b_value = DecimalNumber(b_tracker.get_value(), num_decimal_places=2,
                                color=GREEN).next_to(b_label, RIGHT)

        self.play(Write(f_label))
        self.play(Write(a_label), Write(b_label),
                  Write(a_value), Write(b_value))
        self.play(Create(linear))

        # triangle
        x_tracker = ValueTracker(0.5)
        x = x_tracker.get_value()
        a = a_tracker.get_value()
        b = b_tracker.get_value()

        line1 = Line(axes.c2p(x, a*x + b), axes.c2p(x + 1, a*x + b),
                     color=WHITE)
        line2 = Line(axes.c2p(x + 1, a*x + b),
                     axes.c2p(x + 1, a*(x + 1) + b),
                     color=RED)

        line1_label = MathTex("1", color=WHITE).next_to(line1, DOWN)
        line1_label.add_updater(lambda m: m.next_to(line1, DOWN))

        line2_label = DecimalNumber(a, num_decimal_places=2,
                                    color=RED).next_to(line2, RIGHT)

        triangle = VGroup(line1, line2)

        def update_line2(mob):
            a = a_tracker.get_value()
            b = b_tracker.get_value()
            x = x_tracker.get_value()
            mob.become(Line(axes.c2p(x + 1, a*x + b),
                            axes.c2p(x + 1, a*(x + 1) + b),
                            color=RED))
        def update_line1(mob):
            a = a_tracker.get_value()
            b = b_tracker.get_value()
            x = x_tracker.get_value()
            mob.become(Line(axes.c2p(x, a*x + b), axes.c2p(x + 1, a*x + b)))

        def update_label2(mob):
            a = a_tracker.get_value()
            mob.become(DecimalNumber(a, num_decimal_places=2,
                                     color=RED).next_to(line2, RIGHT))

        line1.add_updater(update_line1)
        line2.add_updater(update_line2)
        line2_label.add_updater(update_label2)

        self.play(Create(triangle))
        self.play(Write(line1_label), Write(line2_label))

        self.wait()
        self.play(x_tracker.animate.set_value(1), run_time=2)
        self.play(x_tracker.animate.set_value(-1.5), run_time=2)
        self.play(x_tracker.animate.set_value(0.5), run_time=2)

        self.wait()
        self.play(a_tracker.animate.set_value(2),
                  b_tracker.animate.set_value(1),
                  ChangeDecimalToValue(a_value, 2),
                  ChangeDecimalToValue(b_value, 1),
                  x_tracker.animate.set_value(0),
                  run_time=2)

        self.wait()
        self.play(x_tracker.animate.set_value(-1.5), run_time=2)
        self.play(x_tracker.animate.set_value(0.5), run_time=2)

        self.wait()
        line1_label.clear_updaters()
        line2_label.clear_updaters()
        line1.clear_updaters()
        line2.clear_updaters()
        linear.clear_updaters()
        self.play(FadeOut(line1_label), FadeOut(line2_label))
        self.play(FadeOut(triangle), FadeOut(linear))

        # quadratic function
        c_tracker = ValueTracker(0)
        self.play(
            a_tracker.animate.set_value(1),
            b_tracker.animate.set_value(0),
            x_tracker.animate.set_value(0.2),
            ChangeDecimalToValue(a_value, 1),
            ChangeDecimalToValue(b_value, 0)
        )

        g_label = MathTex("g(x) = ", "f(x)", "x", " + ", "c", color=PURPLE_A,
                          substrings_to_isolate=["f(x)", "c"],
                          tex_to_color_map={
                                "f(x)": BLUE,
                                "c": YELLOW
                          }).to_corner(DOWN + LEFT).shift(2 * UP)


        a = a_tracker.get_value()
        b = b_tracker.get_value()
        c = c_tracker.get_value()
        x = x_tracker.get_value()

        ff_label = MathTex("f(x) = ", color=BLUE).next_to(g_label, DOWN,
                                                          aligned_edge=LEFT)
        ff_value = DecimalNumber(a*(x + 1) + b, num_decimal_places=2,
                                 color=BLUE).next_to(ff_label, RIGHT)
        c_label = MathTex("c = ", color=YELLOW).next_to(ff_label, DOWN,
                                                        aligned_edge=LEFT)
        c_value = DecimalNumber(c, num_decimal_places=2,
                                color=YELLOW).next_to(c_label, RIGHT)

        self.play(Write(g_label))
        self.play(Write(ff_label), Write(ff_value),
                  Write(c_label), Write(c_value))

        self.wait()
        line1 = Line(axes.c2p(x, (a*x + b) * x + c),
                     axes.c2p(x + 1, (a*x + b) * x + c),
                     color=WHITE)
        line2 = Line(axes.c2p(x + 1, (a*x + b) * x + c),
                     axes.c2p(x + 1, (a*(x + 1) + b) * (x + 1) + c),
                     color=BLUE)

        def update_line12(mob):
            a = a_tracker.get_value()
            b = b_tracker.get_value()
            c = c_tracker.get_value()
            x = x_tracker.get_value()
            mob.become(Line(axes.c2p(x, (a*x + b) * x + c),
                            axes.c2p(x + 1, (a*x + b) * x + c),
                            color=WHITE))

        def update_line22(mob):
            a = a_tracker.get_value()
            b = b_tracker.get_value()
            c = c_tracker.get_value()
            x = x_tracker.get_value()
            mob.become(Line(axes.c2p(x + 1, (a*x + b) * x + c),
                            axes.c2p(x + 1, (a*(x + 1) + b) * (x + 1) + c),
                            color=BLUE))

        line1_label = MathTex("1", color=WHITE).next_to(line1, DOWN)
        line1_label.add_updater(lambda m: m.next_to(line1, DOWN))

        line2_label = DecimalNumber(a * (x + 1) + b, num_decimal_places=2,
                                    color=BLUE).next_to(line2, RIGHT)

        def update_label22(mob):
            a = a_tracker.get_value()
            b = b_tracker.get_value()
            x = x_tracker.get_value()
            mob.become(DecimalNumber(a*(x + 1) + b, num_decimal_places=2,
                                     color=BLUE).next_to(line2, RIGHT))

        line1.add_updater(update_line12)
        line2.add_updater(update_line22)
        line2_label.add_updater(update_label22)

        triangle = VGroup(line1, line2)
        self.play(Create(triangle))
        self.play(Write(line1_label), Write(line2_label))

        dot = Dot(line2.get_end(), color=BLUE)
        trace = TracedPath(dot.get_center, stroke_width=4,
                           stroke_color=PURPLE_A)
        dot.add_updater(lambda m: m.move_to(line2.get_end()))

        self.play(
            x_tracker.animate.set_value(0),
            ChangeDecimalToValue(ff_value, a*(0 + 1) + b)
        )

        self.play(Create(dot))
        self.add(trace)

        self.play(x_tracker.animate.set_value(1),
                  ChangeDecimalToValue(ff_value, a*(1 + 1) + b),
                  run_time=2)

        self.play(x_tracker.animate.set_value(-2),
                  ChangeDecimalToValue(ff_value, a*(-2 + 1) + b),
                  run_time=2)

        # quadratic = axes.plot(lambda x: x**2, x_range=[-5, 5], color=BLUE)
        # quadratic_label = axes.get_graph_label(quadratic, label="x^2",
        #                                        x_val=-4, direction=UP/2)
        # self.add(quadratic, quadratic_label)

        self.wait(2)

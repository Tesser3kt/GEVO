from manim import *
import numpy as np


class Taylor(Scene):
    def get_axes(self):
        return Axes(
            x_range=[-1, 1],
            y_range=[-5, 5],
            axis_config={"color": WHITE},
        )

    def construct(self):
        # Create axes
        axes = self.get_axes()
        self.play(Create(axes))

        # Create a function
        func = lambda x: np.log(1 + x)
        taylor_1 = lambda x: x
        taylor_2 = lambda x: x - x**2 / 2
        taylor_3 = lambda x: x - x**2 / 2 + x**3 / 3
        taylor_4 = lambda x: x - x**2 / 2 + x**3 / 3 - x**4 / 4
        remainder_1 = lambda x: abs(func(x) - taylor_1(x))
        remainder_2 = lambda x: abs(func(x) - taylor_2(x))
        remainder_3 = lambda x: abs(func(x) - taylor_3(x))
        remainder_4 = lambda x: abs(func(x) - taylor_4(x))

        graph = FunctionGraph(func, color=BLUE, x_range=[-0.99, 4])
        graph_label = MathTex("f(x) = \\log(1 + x)", font_size=36, color=BLUE).next_to(
            graph, UR
        )

        # Display the graph
        self.play(Create(graph), Write(graph_label))
        self.wait()

        # Taylor 1
        taylor_graph_1 = FunctionGraph(taylor_1, color=RED, x_range=[-4, 4])
        taylor_label_1 = axes.get_graph_label(
            taylor_graph_1,
            label=MathTex("T_1(x) = x", font_size=36, color=RED),
            x_val=2 / 3,
        )
        self.play(Create(taylor_graph_1), Write(taylor_label_1))
        self.wait()

        # Remainder 1
        remainder_graph_1 = FunctionGraph(remainder_1, color=YELLOW, x_range=[-0.99, 4])
        remainder_label_1 = axes.get_graph_label(
            remainder_graph_1,
            label=MathTex("R_1(x) = |f(x) - T_1(x)|", font_size=36, color=YELLOW),
            x_val=2 / 3,
        ).shift(0.3 * UP)
        self.play(Create(remainder_graph_1), Write(remainder_label_1))
        self.wait(2)

        # Taylor 2
        taylor_graph_2 = FunctionGraph(taylor_2, color=GREEN, x_range=[-4, 4])
        taylor_label_2 = axes.get_graph_label(
            taylor_graph_2,
            label=MathTex("T_2(x) = x - \\frac{x^2}{2}", font_size=36, color=GREEN),
            x_val=2 / 3,
        )
        remainder_2_graph = FunctionGraph(remainder_2, color=YELLOW, x_range=[-0.99, 4])
        remainder_2_label = axes.get_graph_label(
            remainder_2_graph,
            label=MathTex("R_2(x) = |f(x) - T_2(x)|", font_size=36, color=YELLOW),
            x_val=2 / 3,
        ).shift(0.3 * RIGHT)

        self.play(
            Transform(taylor_graph_1, taylor_graph_2),
            Transform(taylor_label_1, taylor_label_2),
            Transform(remainder_graph_1, remainder_2_graph),
            Transform(remainder_label_1, remainder_2_label),
        )
        self.wait(2)

        # Taylor 3
        taylor_graph_3 = FunctionGraph(taylor_3, color=PURPLE, x_range=[-4, 4])
        taylor_label_3 = axes.get_graph_label(
            taylor_graph_3,
            label=MathTex(
                "T_3(x) = x - \\frac{x^2}{2} + \\frac{x^3}{3}",
                font_size=36,
                color=PURPLE,
            ),
            x_val=2 / 3,
        )
        remainder_3_graph = FunctionGraph(remainder_3, color=YELLOW, x_range=[-0.99, 4])
        remainder_3_label = axes.get_graph_label(
            remainder_3_graph,
            label=MathTex("R_3(x) = |f(x) - T_3(x)|", font_size=36, color=YELLOW),
            x_val=2 / 3,
        ).shift(0.5 * UP)

        self.play(
            Transform(taylor_graph_1, taylor_graph_3),
            Transform(taylor_label_1, taylor_label_3),
            Transform(remainder_graph_1, remainder_3_graph),
            Transform(remainder_label_1, remainder_3_label),
        )
        self.wait(2)

        # Taylor 4
        taylor_graph_4 = FunctionGraph(taylor_4, color=ORANGE, x_range=[-4, 4])
        taylor_label_4 = axes.get_graph_label(
            taylor_graph_4,
            label=MathTex(
                "T_4(x) = x - \\frac{x^2}{2} + \\frac{x^3}{3} - \\frac{x^4}{4}",
                font_size=36,
                color=ORANGE,
            ),
            x_val=2 / 3,
        ).shift(0.2 * RIGHT)
        remainder_4_graph = FunctionGraph(remainder_4, color=YELLOW, x_range=[-0.99, 4])
        remainder_4_label = axes.get_graph_label(
            remainder_4_graph,
            label=MathTex("R_4(x) = |f(x) - T_4(x)|", font_size=36, color=YELLOW),
            x_val=2 / 3,
        ).shift(0.5 * LEFT)

        self.play(
            Transform(taylor_graph_1, taylor_graph_4),
            Transform(taylor_label_1, taylor_label_4),
            Transform(remainder_graph_1, remainder_4_graph),
            Transform(remainder_label_1, remainder_4_label),
        )
        self.wait(2)

import numpy as np
from manim import *


class DrawSimpleCircuit(Scene):
    def draw_and_gate(self, color=WHITE, scale=1, position=ORIGIN):
        points = [
            np.array([0.75, 0, 0]) * scale,
            np.array([0, 0, 0]) * scale,
            np.array([0, 1, 0]) * scale,
            np.array([0.75, 1, 0]) * scale,
        ]

        # Draw Open rectangle
        rect = VMobject()
        rect.set_points_as_corners(points)
        rect.set_z_index(5)

        # Draw arc.
        arc = ArcBetweenPoints(
            start=points[-1], end=points[0], color=color, angle=-PI, z_index=5
        )

        gate = VGroup(rect, arc).move_to(position)

        # Rect animation.
        rect_anim = Create(rect)

        # Arc animation.
        arc_anim = Create(arc)
        self.play(AnimationGroup(rect_anim, arc_anim, lag_ratio=0.4))

        return gate

    def construct(self):
        # Draw AND gate
        and_gate = self.draw_and_gate(scale=2)

        # Draw inputs
        input1_pos = (
            and_gate.get_edge_center(LEFT) + and_gate.get_corner(UP + LEFT)
        ) / 2 + 3 * LEFT
        input2_pos = (
            and_gate.get_edge_center(LEFT) + and_gate.get_corner(DOWN + LEFT)
        ) / 2 + 3 * LEFT
        input1 = Dot(point=input1_pos, radius=0.15, color=WHITE, z_index=10)
        input2 = Dot(point=input2_pos, radius=0.15, color=WHITE, z_index=10)

        # Draw output
        output_pos = and_gate.get_edge_center(RIGHT) + 3 * RIGHT
        output = Dot(point=output_pos, radius=0.15, color=WHITE, z_index=10)

        # Draw wires
        input1_to_gate = Line(
            start=input1.get_center(), end=input1.get_center() + 3 * RIGHT
        )
        input2_to_gate = Line(
            start=input2.get_center(), end=input2.get_center() + 3 * RIGHT
        )
        output_to_gate = Line(
            start=output.get_center(), end=output.get_center() + 3 * LEFT
        )

        wires = VGroup(
            input1, input2, output, input1_to_gate, input2_to_gate, output_to_gate
        )

        # Play Inputs/Output anim.
        inputs_anim = AnimationGroup(
            AnimationGroup(GrowFromCenter(input1), GrowFromCenter(input2), lag_ratio=0),
            AnimationGroup(Create(input1_to_gate), Create(input2_to_gate), lag_ratio=0),
            lag_ratio=0.4,
        )
        output_anim = AnimationGroup(
            GrowFromCenter(output), Create(output_to_gate), lag_ratio=0.4
        )
        self.play(AnimationGroup(inputs_anim, output_anim, lag_ratio=0.4))

        # Draw 0 and 1.
        zero = MathTex(r"\mathbf{0}", color=TEAL).move_to(
            input1.get_center() + 0.5 * LEFT
        )
        one = MathTex(r"\mathbf{1}", color=PINK).move_to(
            input2.get_center() + 0.5 * LEFT
        )

        # Animate 0 and 1.
        self.play(Write(one), Write(zero))

        # Change inputs color.
        self.play(input1.animate().set_color(TEAL), input2.animate().set_color(PINK))

        # Create targets of zero and one.
        zero.generate_target()
        one.generate_target()

        zero.target = input1.copy()
        one.target = input2.copy()

        # Create input1 and input2 copies.
        input1_copy = input1.copy()
        input2_copy = input2.copy()
        self.add(input1_copy, input2_copy)

        # Transform 0 and 1 into dots.
        transform_anim = AnimationGroup(
            MoveToTarget(zero),
            MoveToTarget(one),
            lag_ratio=0,
        )
        moving_anim = AnimationGroup(
            MoveAlongPath(
                input1_copy,
                input1_to_gate,
                run_time=2,
                rate_func=rate_functions.ease_in_out_cubic,
            ),
            MoveAlongPath(
                input2_copy,
                input2_to_gate,
                run_time=2,
                rate_func=rate_functions.ease_in_out_cubic,
            ),
            lag_ratio=0,
        )

        # Lines following the inputs.
        zero_tracking_line = always_redraw(
            lambda: Line(input1.get_center(), input1_copy.get_center(), color=TEAL)
        )
        one_tracking_line = always_redraw(
            lambda: Line(input2.get_center(), input2_copy.get_center(), color=PINK)
        )
        self.add(zero_tracking_line, one_tracking_line)

        # Transform dots back to 0 and 1.
        wedge = MathTex(r"\wedge", color=WHITE)
        gate_zero = MathTex(r"\mathbf{0}", color=TEAL)
        gate_one = MathTex(r"\mathbf{1}", color=PINK)

        # Prepare targets for input1_copy and input2_copy.
        gate_exp = (
            VGroup(gate_zero, wedge, gate_one).arrange().move_to(ORIGIN + 0.1 * LEFT)
        )

        # Animate input1 and input2 copies along line to AND gate.
        self.play(AnimationGroup(transform_anim, moving_anim, lag_ratio=0.5))
        one_tracking_line.clear_updaters()
        zero_tracking_line.clear_updaters()
        self.play(
            AnimationGroup(
                AnimationGroup(
                    Transform(input1_copy, gate_exp[0]),
                    Transform(input2_copy, gate_exp[-1]),
                    lag_ratio=0,
                ),
                Write(wedge),
                lag_ratio=0.4,
            )
        )

        self.remove(input1_copy, input2_copy)

        # Compute the expression in the gate.
        gate_result = MathTex(r"\mathbf{0}", color=TEAL).move_to(ORIGIN + 0.1 * LEFT)
        self.play(
            Transform(gate_exp, gate_result, replace_mobject_with_target_in_scene=True)
        )
        self.wait()

        # Transform the result into dot and move to output line.
        gate_result.generate_target()
        gate_result.target = Dot(
            point=output_to_gate.get_left(), radius=0.15, color=TEAL
        )
        gate_result.set_z_index(20)

        self.play(MoveToTarget(gate_result))

        # Move result to output dot.
        output_tracking_line = always_redraw(
            lambda: Line(
                and_gate.get_edge_center(RIGHT),
                gate_result.get_center(),
                color=TEAL,
            )
        )
        self.add(output_tracking_line)
        gate_to_output = Line(and_gate.get_edge_center(RIGHT), output.get_center())
        self.play(
            MoveAlongPath(
                gate_result,
                gate_to_output,
                run_time=2,
                rate_func=rate_functions.ease_in_out_cubic,
            )
        )

        # Change output to zero again.
        output_tracking_line.clear_updaters()
        output.set_color(TEAL)
        gate_result.generate_target()
        gate_result.target = MathTex(r"\mathbf{0}", color=TEAL).move_to(
            output.get_center() + 0.5 * RIGHT
        )

        self.play(MoveToTarget(gate_result))

        self.wait(5)

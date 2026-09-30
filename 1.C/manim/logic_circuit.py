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


class DrawAdderCircuit(Scene):
    def draw_and_gate(self, color=WHITE, scale=1, position=ORIGIN):
        # Draw and gate
        points = [
            np.array([0.75, 0, 0]) * scale,
            np.array([0, 0, 0]) * scale,
            np.array([0, 1, 0]) * scale,
            np.array([0.75, 1, 0]) * scale,
        ]

        # Draw Open rectangle
        rect = VMobject(color=color)
        rect.set_points_as_corners(points)
        rect.set_z_index(5)

        # Draw arc.
        arc = ArcBetweenPoints(
            start=points[-1], end=points[0], color=color, angle=-PI, z_index=5
        )

        # Draw input lines.
        midpoint_input = (points[1] + points[2]) / 2
        input1 = (midpoint_input + points[2]) / 2
        input2 = (midpoint_input + points[1]) / 2
        input_line1 = Line(start=input1 + 0.75 * scale * LEFT, end=input1, color=color)
        input_line2 = Line(start=input2 + 0.75 * scale * LEFT, end=input2, color=color)

        # Draw output line.
        output = arc.get_edge_center(RIGHT)
        end = ORIGIN + 2 * scale * RIGHT + np.array([0, output[1], 0])
        output_line = Line(
            start=output,
            end=end,
            color=color,
        )

        gate = VGroup(rect, arc, input_line1, input_line2, output_line).move_to(
            position + scale * DOWN + 0.5 * scale * RIGHT
        )

        # Rect animation.
        rect_anim = Create(rect)

        # Arc animation.
        arc_anim = Create(arc)

        # Lines animation
        lines_anim = [Create(input_line1), Create(input_line2), Create(output_line)]
        return (
            gate,
            AnimationGroup(
                rect_anim,
                arc_anim,
                AnimationGroup(*lines_anim, lag_ratio=0),
                lag_ratio=0.4,
            ),
        )

    def draw_xor_gate(self, color=WHITE, scale=1, position=ORIGIN):
        # Draw and gate
        points = [
            np.array([0.25, 0, 0]) * scale,
            np.array([0, 0, 0]) * scale,
            np.array([0, 1, 0]) * scale,
            np.array([0.25, 1, 0]) * scale,
        ]
        tip = np.array([1.25, 0.5, 0]) * scale

        # Draw lines
        lines = [
            Line(
                start=points[1],
                end=points[0] + 0.01 * scale * RIGHT,
                color=color,
                z_index=5,
            ),
            Line(
                start=points[2],
                end=points[3] + 0.01 * scale * RIGHT,
                color=color,
                z_index=5,
            ),
        ]

        # Draw top arc.
        top_arc = ArcBetweenPoints(
            start=points[-1],
            end=tip,
            color=color,
            angle=-15 * PI / 48,
            z_index=5,
        )
        # Draw bottom arc.
        bot_arc = ArcBetweenPoints(
            start=points[0],
            end=tip,
            color=color,
            angle=15 * PI / 48,
            z_index=5,
        )
        # Draw back arcs.
        back_arc = ArcBetweenPoints(
            start=points[1], end=points[2], color=color, angle=PI / 2, z_index=5
        ).shift(0.01 * scale * RIGHT)
        back_arc_2 = back_arc.copy().shift(scale * 0.15 * LEFT)

        # Draw input lines.
        midpoint_input = (points[1] + points[2]) / 2
        input1 = (midpoint_input + points[2]) / 2
        input2 = (midpoint_input + points[1]) / 2
        input_line1 = Line(
            start=input1 + 1.5 * scale * LEFT,
            end=input1 + 0.18 * scale * RIGHT,
            color=color,
        )
        input_line2 = Line(
            start=input2 + 1.5 * scale * LEFT,
            end=input2 + 0.18 * scale * RIGHT,
            color=color,
        )

        # Draw output line.
        output = tip
        end = ORIGIN + 2 * scale * RIGHT + np.array([0, output[1], 0])
        output_line = Line(
            start=output,
            end=end,
            color=color,
        )

        gate = VGroup(
            *lines,
            top_arc,
            bot_arc,
            back_arc,
            back_arc_2,
            input_line1,
            input_line2,
            output_line,
        ).move_to(position + scale * UP)

        # Rect animation.
        lines_anim = [Create(line) for line in lines]

        # Arc animation.
        top_arc_anim = Create(top_arc)
        bot_arc_anim = Create(bot_arc)
        back_arc_anim = Create(back_arc)
        back_arc_2_anim = Create(back_arc_2)

        # Input/output animation.
        io_anim = [Create(input_line1), Create(input_line2), Create(output_line)]

        return (
            gate,
            AnimationGroup(
                AnimationGroup(*lines_anim, lag_ratio=0),
                AnimationGroup(top_arc_anim, bot_arc_anim, lag_ratio=0),
                AnimationGroup(back_arc_anim, back_arc_2_anim, lag_ratio=0),
                AnimationGroup(*io_anim, lag_ratio=0),
                lag_ratio=0.4,
            ),
        )

    def draw_or_gate(self, color=WHITE, scale=1, position=ORIGIN):
        # Draw or gate
        points = [
            np.array([0.25, 0, 0]) * scale,
            np.array([0, 0, 0]) * scale,
            np.array([0, 1, 0]) * scale,
            np.array([0.25, 1, 0]) * scale,
        ]
        tip = np.array([1.25, 0.5, 0]) * scale

        # Draw lines
        lines = [
            Line(
                start=points[1],
                end=points[0] + 0.01 * scale * RIGHT,
                color=color,
                z_index=5,
            ),
            Line(
                start=points[2],
                end=points[3] + 0.01 * scale * RIGHT,
                color=color,
                z_index=5,
            ),
        ]

        # Draw top arc.
        top_arc = ArcBetweenPoints(
            start=points[-1],
            end=tip,
            color=color,
            angle=-15 * PI / 48,
            z_index=5,
        )
        # Draw bottom arc.
        bot_arc = ArcBetweenPoints(
            start=points[0],
            end=tip,
            color=color,
            angle=15 * PI / 48,
            z_index=5,
        )
        # Draw back arcs.
        back_arc = ArcBetweenPoints(
            start=points[1], end=points[2], color=color, angle=PI / 2, z_index=5
        ).shift(0.01 * scale * RIGHT)

        # Draw input lines.
        midpoint_input = (points[1] + points[2]) / 2
        input1 = (midpoint_input + points[2]) / 2
        input2 = (midpoint_input + points[1]) / 2
        input_line1 = Line(
            start=input1 + 0.75 * scale * LEFT,
            end=input1 + 0.18 * scale * RIGHT,
            color=color,
        )
        input_line2 = Line(
            start=input2 + 0.75 * scale * LEFT,
            end=input2 + 0.18 * scale * RIGHT,
            color=color,
        )

        # Draw output line.
        output = tip
        end = ORIGIN + 2 * scale * RIGHT + np.array([0, output[1], 0])
        output_line = Line(
            start=output,
            end=end,
            color=color,
        )

        gate = VGroup(
            *lines,
            top_arc,
            bot_arc,
            back_arc,
            input_line1,
            input_line2,
            output_line,
        ).move_to(position + scale * UP)

        # Rect animation.
        lines_anim = [Create(line) for line in lines]

        # Arc animation.
        top_arc_anim = Create(top_arc)
        bot_arc_anim = Create(bot_arc)
        back_arc_anim = Create(back_arc)

        # Input/output animation.
        io_anim = [Create(input_line1), Create(input_line2), Create(output_line)]

        return (
            gate,
            AnimationGroup(
                AnimationGroup(*lines_anim, lag_ratio=0),
                AnimationGroup(top_arc_anim, bot_arc_anim, lag_ratio=0),
                AnimationGroup(back_arc_anim, lag_ratio=0),
                AnimationGroup(*io_anim, lag_ratio=0),
                lag_ratio=0.4,
            ),
        )

    def draw_adder(self, color=WHITE, scale=1, position=ORIGIN):
        (and_gate, and_gate_anim) = self.draw_and_gate(color, scale, position)
        (xor_gate, xor_gate_anim) = self.draw_xor_gate(color, scale, position)

        # Align gate outputs
        distance = and_gate.get_right() - xor_gate.get_right()
        xor_gate = xor_gate.shift(distance[0] * RIGHT)

        # Connect xor input to and inputs
        and_input1 = and_gate[2].get_left()
        xor_input1 = xor_gate[6].get_left()

        and_input2 = and_gate[3].get_left()
        xor_input2 = xor_gate[7].get_left()

        connecting_line1 = Line(
            start=np.array([and_input1[0], xor_input1[1], 0]),
            end=and_input1 + 0.02 * scale * DOWN,
            color=color,
        )
        connecting_line2 = Line(
            start=np.array([and_input2[0], xor_input2[1], 0]),
            end=and_input2 + 0.02 * scale * DOWN,
            color=color,
        ).shift(0.4 * scale * LEFT)
        connecting_line3 = Line(
            start=connecting_line2.get_bottom() + 0.02 * scale * UP,
            end=and_input2,
            color=color,
        )
        connect_anim = AnimationGroup(
            Create(connecting_line1), Create(connecting_line2), Create(connecting_line3)
        )

        connecting_lines = VGroup(connecting_line1, connecting_line2, connecting_line3)

        return (
            (and_gate, and_gate_anim),
            (xor_gate, xor_gate_anim),
            (connecting_lines, connect_anim),
        )

    def animate_adder(self, i1, i2, shift=ORIGIN):
        (
            (and_gate, and_gate_anim),
            (xor_gate, xor_gate_anim),
            (connect_lines, connect_anim),
        ) = self.draw_adder()

        and_gate.shift(shift)
        xor_gate.shift(shift)
        connect_lines.shift(shift)

        self.play(
            AnimationGroup(
                AnimationGroup(and_gate_anim, xor_gate_anim, lag_ratio=0),
                connect_anim,
                lag_ratio=0.5,
            )
        )

        adder = VGroup(and_gate, xor_gate, connect_lines)

        # Mark inputs.
        input1_dot = Dot(
            point=xor_gate[6].get_left(),
            radius=0.1,
            color=PINK if i1 else TEAL,
            z_index=10,
        )
        input2_dot = Dot(
            point=xor_gate[7].get_left(),
            radius=0.1,
            color=PINK if i2 else TEAL,
            z_index=10,
        )
        input1_text = MathTex(
            r"\mathbf{1}" if i1 else r"\mathbf{0}", color=PINK if i1 else TEAL
        ).next_to(input1_dot, LEFT)
        input2_text = MathTex(
            r"\mathbf{1}" if i2 else r"\mathbf{0}", color=PINK if i2 else TEAL
        ).next_to(input2_dot, LEFT)

        adder.add(input1_dot, input2_dot, input1_text, input2_text)

        self.play(
            GrowFromCenter(input1_dot),
            GrowFromCenter(input2_dot),
            Write(input1_text),
            Write(input2_text),
        )

        # Send current through the XOR gate.
        xor_input1_line = Line(
            start=input1_dot.get_center(),
            end=xor_gate[6].get_right(),
            color=PINK if i1 else TEAL,
            z_index=10,
        )
        xor_input2_line = Line(
            start=input2_dot.get_center(),
            end=xor_gate[7].get_right(),
            color=PINK if i2 else TEAL,
            z_index=10,
        )

        adder.add(xor_input1_line, xor_input2_line)

        xor_input1_anim = Create(xor_input1_line)
        xor_input2_anim = Create(xor_input2_line)

        for mobj in xor_gate[:-3]:
            mobj.set_z_index(20)

        # Fill XOR gate.
        xor_gate_inside = VGroup(*[mobj.copy() for mobj in xor_gate[:-3]])
        for mobj in xor_gate_inside:
            mobj.set_color(PINK if (i1 ^ i2) else TEAL).set_z_index(20)

        adder.add(xor_gate_inside)

        xor_fill_anim = AnimationGroup(
            *[Create(mobj) for mobj in xor_gate_inside], lag_ratio=0
        )

        # Send current through AND gate.
        for mobj in and_gate[:2]:
            mobj.set_z_index(20)

        and_connecting_line1 = connect_lines[0].copy()
        and_connecting_line1.set_color(PINK if i1 else TEAL).set_z_index(10)

        and_input_line1 = and_gate[2].copy()
        and_input_line1.set_color(PINK if i1 else TEAL).set_z_index(10)

        and_connecting_line2 = connect_lines[1].copy()
        and_connecting_line2.set_color(PINK if i2 else TEAL).set_z_index(10)

        and_input_line2 = Line(
            start=connect_lines[2].get_left(),
            end=and_gate[3].get_end(),
            color=PINK if i2 else TEAL,
        )
        and_input_line2.set_color(PINK if i2 else TEAL).set_z_index(10)

        adder.add(
            and_connecting_line1, and_connecting_line2, and_input_line1, and_input_line2
        )

        # Fill AND gate.
        and_gate_inside = VGroup(*[mobj.copy() for mobj in and_gate[:2]])
        for mobj in and_gate_inside:
            mobj.set_color(PINK if (i1 and i2) else TEAL).set_z_index(20)
        and_fill_anim = AnimationGroup(
            *[Create(mobj) for mobj in and_gate_inside], lag_ratio=0
        )

        fill_anim = AnimationGroup(
            AnimationGroup(
                Create(
                    and_connecting_line1,
                    run_time=1,
                    rate_func=rate_functions.ease_out_cubic,
                ),
                Create(
                    and_connecting_line2,
                    run_time=1,
                    rate_func=rate_functions.ease_out_cubic,
                ),
                lag_ratio=0,
            ),
            AnimationGroup(
                Create(
                    and_input_line1,
                    run_time=1,
                    rate_func=rate_functions.ease_in_cubic,
                ),
                Create(
                    and_input_line2,
                    run_time=1,
                    rate_func=rate_functions.ease_in_cubic,
                ),
                lag_ratio=0,
            ),
            lag_ratio=0.7,
        )

        adder.add(and_gate_inside)

        # Get XOR output
        xor_output = xor_gate[-1].copy()
        xor_output.set_color(PINK if (i1 ^ i2) else TEAL).set_z_index(10)

        adder.add(xor_output)

        xor_output_dot = Dot(
            point=xor_output.get_end(),
            radius=0.1,
            color=PINK if (i1 ^ i2) else TEAL,
        )
        xor_output_text = MathTex(
            r"\mathbf{1}" if (i1 ^ i2) else r"\mathbf{0}",
            color=PINK if (i1 ^ i2) else TEAL,
        ).next_to(xor_output_dot, RIGHT)

        adder.add(xor_output_dot, xor_output_text)

        xor_output_anim = AnimationGroup(
            Create(xor_output),
            AnimationGroup(
                GrowFromCenter(xor_output_dot),
                Write(xor_output_text),
                lag_ratio=0.4,
            ),
            lag_ratio=0.8,
        )

        # Get AND output.
        and_output = and_gate[-1].copy()
        and_output.set_color(PINK if (i1 and i2) else TEAL).set_z_index(10)
        and_output_dot = Dot(
            point=and_output.get_end(),
            radius=0.1,
            color=PINK if (i1 and i2) else TEAL,
        )
        and_output_text = MathTex(
            r"\mathbf{1}" if (i1 and i2) else r"\mathbf{0}",
            color=PINK if (i1 and i2) else TEAL,
        ).next_to(and_output_dot, RIGHT)

        adder.add(and_output, and_output_dot, and_output_text)

        and_output_anim = AnimationGroup(
            Create(and_output),
            AnimationGroup(
                GrowFromCenter(and_output_dot),
                Write(and_output_text),
                lag_ratio=0.4,
            ),
            lag_ratio=0.8,
        )

        self.play(
            AnimationGroup(
                AnimationGroup(
                    AnimationGroup(xor_input1_anim, xor_input2_anim, lag_ratio=0),
                    fill_anim,
                    lag_ratio=0.5,
                ),
                AnimationGroup(
                    AnimationGroup(xor_fill_anim, xor_output_anim, lag_ratio=0.4),
                    AnimationGroup(and_fill_anim, and_output_anim, lag_ratio=0.4),
                    lag_ratio=0.5,
                ),
                lag_ratio=0.3,
            )
        )

        return adder

    def construct(self):
        # Create adder
        adder1 = self.animate_adder(0, 1)
        self.play(adder1.animate.shift(2 * UP))
        adder2 = self.animate_adder(1, 1, 1.5 * DOWN)

        self.play(adder1.animate.shift(4 * LEFT), adder2.animate.shift(4 * LEFT))

        # Draw XOR gate
        (xor_gate, xor_gate_anim) = self.draw_xor_gate(position=0.75 * DOWN + RIGHT)
        self.play(xor_gate_anim)

        # Connect 1st gate carry + 2nd gate output to xor gate
        midpoint = adder1[0][-1].get_right() + RIGHT
        xor_connector1 = VMobject(color=WHITE).set_points_as_corners(
            [
                adder1[0][-1].get_right(),
                midpoint,
                np.array([midpoint[0], xor_gate[6].get_left()[1], 0]),
                xor_gate[6].get_left(),
            ]
        )

        midpoint = adder2[1][-1].get_right() + RIGHT
        xor_connector2 = VMobject(color=WHITE).set_points_as_corners(
            [
                adder2[1][-1].get_right(),
                midpoint,
                np.array([midpoint[0], xor_gate[7].get_left()[1], 0]),
                xor_gate[7].get_left(),
            ]
        )

        self.play(
            AnimationGroup(
                Uncreate(adder1[19]),
                Unwrite(adder1[20]),
                Create(xor_connector1),
                lag_ratio=0.1,
            ),
            AnimationGroup(
                Uncreate(adder2[16]),
                Unwrite(adder2[17]),
                Create(xor_connector2),
                lag_ratio=0.1,
            ),
        )

        # Draw and gate.
        (and_gate, and_gate_anim) = self.draw_and_gate(
            position=0.5 * DOWN + 0.875 * RIGHT
        )
        self.play(and_gate_anim)

        # Duplicate XOR gate inputs to AND gate.
        and_connector1 = VMobject().set_points_as_corners(
            [
                xor_gate[6].get_left() + 0.4 * RIGHT,
                np.array(
                    [
                        (xor_gate[6].get_left() + 0.4 * RIGHT)[0],
                        and_gate[2].get_left()[1],
                        0,
                    ]
                ),
                and_gate[2].get_left(),
            ]
        )
        and_connector2 = VMobject().set_points_as_corners(
            [
                xor_gate[7].get_left(),
                np.array(
                    [
                        (xor_gate[7].get_left())[0],
                        and_gate[3].get_left()[1],
                        0,
                    ]
                ),
                and_gate[3].get_left(),
            ]
        )

        self.play(Create(and_connector1), Create(and_connector2))

        (or_gate, or_gate_anim) = self.draw_or_gate(
            color=WHITE, position=4.5 * RIGHT + 3.25 * DOWN
        )
        or_gate.set_z_index(20)
        self.play(or_gate_anim)

        # Connect 2nd carry to or gate.
        carry_connector = Line(
            adder2[18].get_right(), or_gate[6].get_left() + 0.01 * RIGHT, color=WHITE
        )
        # Connect final carry to or gate.
        carry_connector2 = VMobject(color=WHITE).set_points_as_corners(
            [
                and_gate[-1].get_right() + 0.02 * UP,
                np.array([and_gate[-1].get_right()[0], or_gate[5].get_left()[1], 0]),
                or_gate[5].get_left() + 0.01 * RIGHT,
            ]
        )

        self.play(
            AnimationGroup(
                Uncreate(adder2[19]),
                Unwrite(adder2[20]),
                Create(carry_connector),
                lag_ratio=0.1,
            ),
            Create(carry_connector2),
        )

        # Send current.
        xor_connector1_copy = xor_connector1.copy().set_color(TEAL).set_z_index(15)
        xor_connector2_copy = xor_connector2.copy().set_color(TEAL).set_z_index(15)

        and_connector1_copy = and_connector1.copy().set_color(TEAL).set_z_index(15)
        and_connector2_copy = and_connector2.copy().set_color(TEAL).set_z_index(15)

        xor_input1_copy = xor_gate[6].copy().set_color(TEAL).set_z_index(15)
        xor_input2_copy = xor_gate[7].copy().set_color(TEAL).set_z_index(15)

        and_input1_copy = and_gate[2].copy().set_color(TEAL).set_z_index(15)
        and_input2_copy = and_gate[3].copy().set_color(TEAL).set_z_index(15)

        self.play(
            AnimationGroup(
                AnimationGroup(
                    AnimationGroup(
                        Create(xor_connector1_copy),
                        Create(xor_connector2_copy),
                        lag_ratio=0,
                    ),
                    AnimationGroup(
                        Create(xor_input1_copy), Create(xor_input2_copy), lag_ratio=0
                    ),
                    lag_ratio=0.6,
                ),
                AnimationGroup(
                    AnimationGroup(
                        Create(and_connector1_copy),
                        Create(and_connector2_copy),
                        lag_ratio=0.2,
                    ),
                    AnimationGroup(
                        Create(and_input1_copy),
                        Create(and_input2_copy),
                        lag_ratio=0,
                    ),
                    lag_ratio=0.5,
                ),
                lag_ratio=0.5,
            )
        )

        # Animate XOR and AND gate fill.
        xor_gate_inside = VGroup(*[mobj.copy() for mobj in xor_gate[:-3]])
        for mobj in xor_gate_inside:
            mobj.set_color(TEAL).set_z_index(20)

        and_gate_inside = VGroup(*[mobj.copy() for mobj in and_gate[:2]])
        for mobj in and_gate_inside:
            mobj.set_color(TEAL).set_z_index(20)

        self.play(
            *[Create(mobj) for mobj in xor_gate_inside],
            *[Create(mobj) for mobj in and_gate_inside],
        )

        xor_output_copy = xor_gate[-1].copy().set_color(TEAL).set_z_index(15)
        xor_output_dot = Dot(point=xor_gate[-1].get_right(), radius=0.1, color=TEAL)
        xor_output_text = MathTex(r"\mathbf{0}", color=TEAL).next_to(
            xor_output_dot, RIGHT
        )

        # XOR output anim
        xor_output_anim = AnimationGroup(
            Create(xor_output_copy),
            AnimationGroup(
                GrowFromCenter(xor_output_dot), Write(xor_output_text), lag_ratio=0.2
            ),
            lag_ratio=0.6,
        )

        # AND to OR connect anim
        and_to_or_connector = VMobject(color=TEAL, z_index=25).set_points_as_corners(
            [
                and_gate[-1].get_left(),
                and_gate[-1].get_right(),
                np.array([and_gate[-1].get_right()[0], or_gate[5].get_left()[1], 0]),
                or_gate[5].get_right(),
            ]
        )
        carry_to_or_connector = Line(
            adder2[18].get_left(), or_gate[6].get_right(), color=PINK, z_index=25
        )

        and_to_or_connect_anim = Create(and_to_or_connector)
        carry_to_or_connect_anim = Create(carry_to_or_connector)

        # OR gate output anim.
        or_gate_inside = VGroup(*[mobj.copy() for mobj in or_gate[:-3]])
        for mobj in or_gate_inside:
            mobj.set_color(PINK).set_z_index(30)

        or_gate_fill_anim = AnimationGroup(*[Create(mobj) for mobj in or_gate_inside])

        # OR gate output anim.
        or_gate_output_copy = or_gate[-1].copy().set_color(PINK).set_z_index(30)
        or_gate_output_dot = Dot(point=or_gate[-1].get_right(), radius=0.1, color=PINK)
        or_gate_output_text = MathTex(r"\mathbf{1}", color=PINK).next_to(
            or_gate_output_dot, RIGHT
        )

        or_output_anim = AnimationGroup(
            Create(or_gate_output_copy),
            AnimationGroup(
                GrowFromCenter(or_gate_output_dot),
                Write(or_gate_output_text),
                lag_ratio=0.2,
            ),
            lag_ratio=0.6,
        )

        self.play(
            xor_output_anim,
            AnimationGroup(
                AnimationGroup(
                    and_to_or_connect_anim, carry_to_or_connect_anim, lag_ratio=0
                ),
                AnimationGroup(or_gate_fill_anim, or_output_anim, lag_ratio=0.4),
                lag_ratio=0.7,
            ),
        )

        self.wait(5)

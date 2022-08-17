import numpy as np
from manim import *
from math import sin, cos

# config
CPU_ORIGIN = 2 * UP + 2 * LEFT
CPU_SIDE_LENGTH = 1.5
CPU_STROKE_WIDTH = 4
CPU_COLOR = TEAL
CPU_LINE_LENGTH = 0.4

RAM_ORIGIN = DOWN + 3 * LEFT
RAM_WIDTH = 4
RAM_BLOCK_WIDTH = RAM_WIDTH / 8
RAM_HEIGHT = 0.8
RAM_STROKE_WIDTH = 4
RAM_COLOR = LIGHT_PINK
RAM_INNER_FONT_SIZE = 45

PROG_COLOR = YELLOW
PROG_OFFSET_VECTOR = 2 * RIGHT
PROG_WIDTH = 4
PROG_HEIGHT = 5
PROG_STROKE_WIDTH = 4
PROG_INSTRUCTIONS = 4
PROG_BLOCK_HEIGHT = 0.8
PROG_DOT_OFFSET = 0.2
PROG_DOT_RADIUS = 0.03
PROG_FONT_SIZE = 30

HEAD_LINE_LENGTH = 0.3

INDICATOR_RECT_OPACITY = 0.2

CABLE_TOP_OFFSET = 1

TEXT_FONT = 'Fira Sans'
TEXT_FONT_SIZE = 30
TEXT_FADE_SHIFT_COEF = 0.2
CAPTION_OFFSET_COEF = 1.4


class CPU_addition(Scene):
    def construct(self):
        def write_to_ram_anim(mem_block: int, value: int) -> Mobject:
            # create value text
            value_text = Tex(
                str(value), font_size=RAM_INNER_FONT_SIZE).set_z_index(2)
            value_text.move_to(CPU_ORIGIN)

            # connect cpu to ram block
            start = CPU_ORIGIN + LEFT * (CPU_SIDE_LENGTH / 2)
            end = np.array([
                ram_left + (mem_block + 0.5) * RAM_BLOCK_WIDTH,
                ram_top,
                0
            ])
            midpoint = np.array([end[0], start[1], 0])

            # create cpu-ram connection
            cable = VMobject(
                stroke_color=CPU_COLOR,
                stroke_opacity=1,
                stroke_width=CPU_STROKE_WIDTH
            )
            cable.set_points_as_corners([start, midpoint, end])

            # create transfer dot
            cable_dot = Dot(start).set_z_index(2)

            # create text in block
            block_text = Tex(
                str(value), font_size=RAM_INNER_FONT_SIZE).set_z_index(2)
            block_text.move_to(end + (RAM_HEIGHT / 2) * DOWN)

            # play animation
            self.play(Write(value_text, run_time=1))
            self.play(Create(cable))
            self.play(FadeTransform(value_text, cable_dot, run_time=0.4,
                                    rate_func=rate_functions.ease_in_cubic))
            self.play(MoveAlongPath(cable_dot, cable, run_time=1,
                                    rate_func=rate_functions.linear))
            self.play(FadeTransform(cable_dot, block_text, run_time=0.4,
                                    rate_func=rate_functions.ease_out_cubic))
            cable.set_points_as_corners([end, midpoint, start])
            self.play(Uncreate(cable))

            return block_text

        def access_in_ram(mem_blocks: list[int], values: list[int],
                          mobjs: list[Mobject],
                          dirs: list[np.ndarray]) -> list[Mobject]:

            # create cpu-ram cables
            cables = []
            value_texts = []
            dots = []
            for i, mem_block in enumerate(mem_blocks):
                start = CPU_ORIGIN + LEFT * \
                    (CPU_SIDE_LENGTH / 2) + \
                    dirs[i] * (CPU_SIDE_LENGTH * 1.08 / 4)
                end = np.array([
                    ram_left + (mem_block + 0.5) * RAM_BLOCK_WIDTH,
                    ram_top,
                    0
                ])
                midpoint = np.array([end[0], start[1], 0])
                cable = VMobject(
                    stroke_color=CPU_COLOR,
                    stroke_opacity=1,
                    stroke_width=CPU_STROKE_WIDTH
                )
                cable.set_points_as_corners([start, midpoint, end])
                cables.append(cable)

                # copy ram values
                ram_value_copies = [mobj.copy().set_opacity(0)
                                    for mobj in mobjs]
                self.add(*ram_value_copies)

                # create value text in cpu
                value_text = Tex(
                    str(values[i]),
                    font_size=RAM_INNER_FONT_SIZE).set_z_index(2)
                value_text.move_to(
                    CPU_ORIGIN + dirs[i] * (CPU_SIDE_LENGTH * 1.08 / 4))
                value_texts.append(value_text)

                # create transfer dot
                cable_dot = Dot(end).set_z_index(2)
                dots.append(cable_dot)

            cables = VGroup(*cables)
            value_texts = VGroup(*value_texts)
            dots = VGroup(*dots)

            # play animation
            self.play(*[Create(cbl) for cbl in cables])

            # reverse cables
            for cbl in cables:
                pts = cbl.get_all_points()
                cbl = cbl.set_points(list(reversed(pts)))

            self.play(*[FadeTransform(
                mobj,
                dot,
                run_time=0.6,
                rate_func=rate_functions.ease_in_cubic
            ) for i, mobj in enumerate(mobjs) for j, dot in enumerate(dots)
                if i == j], *[mobj.animate(run_time=0.25).set_opacity(1)
                              for mobj in ram_value_copies])
            self.play(*[MoveAlongPath(
                dot,
                cbl,
                run_time=0.8,
                rate_func=rate_functions.linear
            ) for i, dot in enumerate(dots) for j, cbl in enumerate(cables)
                if i == j])
            self.play(*[FadeTransform(
                dot,
                val_text,
                run_time=0.4,
                rate_func=rate_functions.ease_out_cubic
            ) for i, dot in enumerate(dots)
                for j, val_text in enumerate(value_texts) if i == j])

            # reverse cables again
            for cbl in cables:
                pts = cbl.get_all_points()
                cbl = cbl.set_points(list(reversed(pts)))

            self.play(*[Uncreate(cbl) for cbl in cables])

            return value_texts

        def sum_in_cpu(mobjs: VGroup, result: int) -> Mobject:
            # create plus sign object
            plus_sign = Tex(
                r'$+$', font_size=RAM_INNER_FONT_SIZE, color=CPU_COLOR)
            plus_sign.move_to(CPU_ORIGIN)

            result_text = Tex(str(result), font_size=RAM_INNER_FONT_SIZE)
            result_text.move_to(CPU_ORIGIN)

            mobjs.add(plus_sign)
            self.play(Write(plus_sign, run_time=0.5))
            self.play(Transform(
                mobjs,
                result_text,
                run_time=1,
                replace_mobject_with_target_in_scene=True
            ))

            return result_text

        def write_to_ram_south(mem_block: int, mobj: Mobject) -> Mobject:
            # create cable
            start = CPU_ORIGIN + (CPU_SIDE_LENGTH / 2) * DOWN
            end = np.array([
                ram_left + (mem_block + 0.5) * RAM_BLOCK_WIDTH,
                ram_top,
                0
            ])
            midpoint1 = start + CABLE_TOP_OFFSET * DOWN
            midpoint2 = np.array([
                end[0],
                midpoint1[1],
                0
            ])
            corners = [start, midpoint1, midpoint2, end]

            cable = VMobject(
                stroke_color=CPU_COLOR,
                stroke_opacity=1,
                stroke_width=CPU_STROKE_WIDTH
            )
            cable.set_points_as_corners(corners)

            # create dot
            dot = Dot(start)

            # create mobj copy in mem_block
            ram_mobj = mobj.copy()
            ram_mobj.move_to(end + (RAM_HEIGHT / 2) * DOWN)

            # play animation
            self.play(Create(cable))
            self.play(FadeTransform(
                mobj,
                dot,
                run_time=0.6,
                rate_func=rate_functions.ease_in_cubic
            ))
            self.play(MoveAlongPath(
                dot,
                cable,
                run_time=1,
                rate_func=rate_functions.linear
            ))
            self.play(FadeTransform(
                dot,
                ram_mobj,
                run_time=0.4,
                rate_func=rate_functions.ease_out_cubic
            ))

            # reverse cable
            cable.set_points_as_corners(list(reversed(corners)))
            self.play(Uncreate(cable))

            return ram_mobj

        plane = NumberPlane(background_line_style={
            'stroke_color': YELLOW,
            'stroke_width': 1,
            'stroke_opacity': 0.4
        })

        # creating cpu frame
        cpu_square = Square(
            side_length=CPU_SIDE_LENGTH,
            color=CPU_COLOR,
            stroke_width=CPU_STROKE_WIDTH
        ).shift(CPU_ORIGIN)
        cpu_vertical_line_endpoints = [
            (np.array([x, y1, 0]), np.array([x, y2, 0]))
            for x in
            [-CPU_LINE_LENGTH, 0, CPU_LINE_LENGTH]
            for y1, y2 in
            [(CPU_SIDE_LENGTH / 2, CPU_SIDE_LENGTH / 2 + CPU_LINE_LENGTH),
             (-CPU_SIDE_LENGTH / 2, -CPU_SIDE_LENGTH / 2 - CPU_LINE_LENGTH)]
        ]
        cpu_horizontal_line_endpoints = [
            (np.array([x1, y, 0]), np.array([x2, y, 0]))
            for y in
            [-CPU_LINE_LENGTH, 0, CPU_LINE_LENGTH]
            for x1, x2 in
            [(CPU_SIDE_LENGTH / 2, CPU_SIDE_LENGTH / 2 + CPU_LINE_LENGTH),
             (-CPU_SIDE_LENGTH / 2, -CPU_SIDE_LENGTH / 2 - CPU_LINE_LENGTH)]
        ]
        cpu_line_endpoints = cpu_horizontal_line_endpoints + cpu_vertical_line_endpoints
        cpu_lines = [
            Line(
                start=x,
                end=y,
                color=CPU_COLOR,
                stroke_width=CPU_STROKE_WIDTH,
                stroke_opacity=1
            ).shift(CPU_ORIGIN) for x, y in cpu_line_endpoints
        ]
        cpu_frame = [cpu_square] + cpu_lines
        cpu_animation = [Create(mobj) for mobj in cpu_frame]

        # adding cpu caption animation
        cpu_caption = Text('CPU', font=TEXT_FONT, font_size=TEXT_FONT_SIZE,
                           color=CPU_COLOR).next_to(
            cpu_square, (1 + CAPTION_OFFSET_COEF) * UP)
        cpu_animation.append(
            FadeIn(cpu_caption, shift=TEXT_FADE_SHIFT_COEF * UP))

        # creating ram frame
        ram_rect = Rectangle(
            width=RAM_WIDTH,
            height=RAM_HEIGHT,
            color=RAM_COLOR,
            stroke_width=RAM_STROKE_WIDTH
        ).shift(RAM_ORIGIN)

        # creating ram dividing lines
        ram_top = RAM_ORIGIN[1] + RAM_HEIGHT / 2
        ram_bottom = RAM_ORIGIN[1] - RAM_HEIGHT / 2
        ram_left = RAM_ORIGIN[0] - RAM_WIDTH / 2
        ram_right = RAM_ORIGIN[0] + RAM_WIDTH / 2
        ram_div_lines = [
            Line(
                start=np.array([x, ram_top, 0]),
                end=np.array([x, ram_bottom, 0]),
                color=RAM_COLOR,
                stroke_width=RAM_STROKE_WIDTH,
                stroke_opacity=1
            ) for x in np.arange(ram_left + RAM_BLOCK_WIDTH, ram_right, 0.5)
        ]
        ram_frame = [ram_rect] + ram_div_lines
        ram_animation = [Create(mobj) for mobj in ram_frame]

        # adding ram caption
        ram_caption = Text('PAMĚŤ', font=TEXT_FONT, font_size=TEXT_FONT_SIZE,
                           color=RAM_COLOR).next_to(ram_rect,
                                                    CAPTION_OFFSET_COEF * LEFT)
        ram_caption.shift(0.05 * UP)
        ram_animation.append(
            FadeIn(ram_caption, shift=TEXT_FADE_SHIFT_COEF * LEFT))

        # numbering ram blocks
        ram_numbers = VGroup(*[
            Text(str(n), font=TEXT_FONT, font_size=TEXT_FONT_SIZE,
                 color=RAM_COLOR) for n in range(8)
        ])
        ram_numbers[0].next_to(ram_div_lines[0], DOWN)
        ram_numbers[0].shift(RAM_BLOCK_WIDTH * LEFT / 2)
        for k in range(1, 8):
            ram_numbers[k].align_to(ram_numbers[0], UP)
            ram_numbers[k].align_to(ram_numbers[0], LEFT)
            ram_numbers[k].shift(k * RAM_BLOCK_WIDTH * RIGHT)
        ram_numbers_animation = [Write(ram_numbers)]

        # creating program frame
        prog_frame_vertices = [
            np.array([0, -PROG_HEIGHT, 0]),
            ORIGIN,
            np.array([PROG_WIDTH, 0, 0]),
            np.array([PROG_WIDTH, -PROG_HEIGHT, 0])
        ]
        prog_frame = VMobject(
            stroke_color=PROG_COLOR,
            stroke_opacity=1,
            stroke_width=PROG_STROKE_WIDTH
        )
        prog_frame.set_points_as_corners(prog_frame_vertices)
        prog_frame.align_to(cpu_square, UP)
        prog_frame.shift(PROG_OFFSET_VECTOR)

        prog_animation = [Create(prog_frame)]

        # creating program caption
        prog_caption = Text('PROGRAM', font=TEXT_FONT,
                            font_size=TEXT_FONT_SIZE,
                            color=PROG_COLOR).next_to(
            prog_frame, (1 + CAPTION_OFFSET_COEF) * UP)
        prog_animation.append(
            FadeIn(prog_caption, shift=TEXT_FADE_SHIFT_COEF * UP))

        # creating program horizontal lines
        prog_hor_lines = VGroup(*[
            Line(
                start=np.array([0, y, 0]),
                end=np.array([PROG_WIDTH, y, 0]),
                color=PROG_COLOR,
                stroke_width=PROG_STROKE_WIDTH,
                stroke_opacity=1
            ) for y in np.arange(
                0, -PROG_INSTRUCTIONS * PROG_BLOCK_HEIGHT, -PROG_BLOCK_HEIGHT)
        ])
        prog_hor_lines.align_to(prog_frame, UP + LEFT)
        prog_hor_lines.shift(PROG_BLOCK_HEIGHT * DOWN)
        prog_animation += [Create(line) for line in prog_hor_lines]

        # creating vertical dots
        prog_dots = VGroup(*[
            Dot(
                point=np.array([0, y, 0]),
                radius=PROG_DOT_RADIUS,
                color=PROG_COLOR
            ) for y in [0, PROG_DOT_OFFSET, 2 * PROG_DOT_OFFSET]
        ])
        prog_dots.next_to(prog_hor_lines[-1], DOWN)
        dots_animation = FadeIn(prog_dots, shift=TEXT_FADE_SHIFT_COEF * DOWN)

        # writing instructions to program
        instructions = VGroup(*[
            Tex('Ulož ', r'$3$', ' do bloku ',
                r'$1$', '.', font_size=PROG_FONT_SIZE),
            Tex('Ulož ', r'$6$', ' do bloku ',
                r'$2$', '.', font_size=PROG_FONT_SIZE),
            Tex('Sečti obsah ', r'$1$', ' s obsahem ',
                r'$2$', '.', font_size=PROG_FONT_SIZE),
            Tex('Výsledek zapiš do ', r'$5$', '.', font_size=PROG_FONT_SIZE)
        ])
        instructions[0].set_color_by_tex('1', RAM_COLOR)
        instructions[1].set_color_by_tex('2', RAM_COLOR)
        instructions[2].set_color_by_tex('1', RAM_COLOR)
        instructions[2].set_color_by_tex('2', RAM_COLOR)
        instructions[3].set_color_by_tex('5', RAM_COLOR)
        instructions.next_to(prog_hor_lines[0], UP)
        for i in [0, 1, 3]:
            instructions[i].align_to(instructions[2], LEFT)
        for i in range(4):
            instructions[i].shift(i * PROG_BLOCK_HEIGHT * DOWN)

        instructions_animation = Write(instructions)

        # creating program block rects
        block_rects = VGroup(*[Rectangle(
            width=PROG_WIDTH,
            height=PROG_BLOCK_HEIGHT,
            stroke_color=None,
            stroke_opacity=0,
            fill_color=WHITE,
            fill_opacity=INDICATOR_RECT_OPACITY
        ) for _ in range(4)])
        block_rects.arrange(DOWN, 0)
        block_rects.align_to(prog_frame, UP)
        block_rects.align_to(prog_frame, LEFT)

        block_rect_anims = [
            [FadeIn(block_rect, run_time=0.2), FadeOut(block_rect, run_time=1)]
            for block_rect in block_rects
        ]

        # creating cpu head
        head_vertices = [
            ORIGIN,
            np.array([HEAD_LINE_LENGTH, 0, 0]),
            np.array([HEAD_LINE_LENGTH + cos(PI / 6) *
                     HEAD_LINE_LENGTH, sin(PI / 6) * HEAD_LINE_LENGTH, 0]),
            np.array([HEAD_LINE_LENGTH + cos(PI / 6) *
                     HEAD_LINE_LENGTH, -sin(PI / 6) * HEAD_LINE_LENGTH, 0]),
            np.array([HEAD_LINE_LENGTH, 0, 0])
        ]
        head = VMobject(
            stroke_color=CPU_COLOR,
            stroke_width=CPU_STROKE_WIDTH,
            stroke_opacity=1
        )
        head.set_points_as_corners(head_vertices)
        head.next_to(block_rects[0], LEFT)
        head_create_animation = [
            FadeIn(head, shift=TEXT_FADE_SHIFT_COEF * LEFT, run_time=0.5)]

        # number = Text('3', font=TEXT_FONT, font_size=TEXT_FONT_SIZE).next_to(
        #     ram_div_lines[2], 0.65 * LEFT)

        # playing scene
        # self.add(plane)
        self.play(*cpu_animation)
        self.wait()
        self.play(AnimationGroup(
            AnimationGroup(*ram_animation),
            AnimationGroup(*ram_numbers_animation),
            lag_ratio=0.5
        ))
        self.wait()
        self.play(*prog_animation)
        self.play(AnimationGroup(instructions_animation,
                  dots_animation, lag_ratio=0.6))
        self.wait()
        self.play(*head_create_animation)
        self.play(block_rect_anims[0][0])
        self.play(AnimationGroup(
            block_rect_anims[0][1],
            instructions[0].animate(run_time=1).set_opacity(0.4),
            lag_ratio=0.2))
        block_values = []
        block_values.append(write_to_ram_anim(1, 3))
        self.wait()
        self.play(head.animate(run_time=0.5).shift(PROG_BLOCK_HEIGHT * DOWN))
        self.play(block_rect_anims[1][0])
        self.play(AnimationGroup(
            block_rect_anims[1][1],
            instructions[1].animate(run_time=1).set_opacity(0.4),
            lag_ratio=0.2))
        block_values.append(write_to_ram_anim(2, 6))
        self.play(head.animate(run_time=0.5).shift(PROG_BLOCK_HEIGHT * DOWN))
        self.play(block_rect_anims[2][0])
        self.play(AnimationGroup(
            block_rect_anims[2][1],
            instructions[2].animate(run_time=1).set_opacity(0.4),
            lag_ratio=0.2))
        cpu_values = access_in_ram([1, 2], [3, 6], block_values, [UP, DOWN])
        result_value = sum_in_cpu(cpu_values, 9)
        self.play(head.animate(run_time=0.5).shift(PROG_BLOCK_HEIGHT * DOWN))
        self.play(block_rect_anims[3][0])
        self.play(AnimationGroup(
            block_rect_anims[3][1],
            instructions[3].animate(run_time=1).set_opacity(0.4),
            lag_ratio=0.2))
        write_to_ram_south(5, result_value)
        self.wait()

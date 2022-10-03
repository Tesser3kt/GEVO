from this import s
from typing import Tuple
import numpy as np
from manim import *


KW_COLOR = YELLOW
VAR_COLORS = [
    TEAL_C,
    LIGHT_PINK,
    ORANGE
]
WHILE_POS = np.array([-3.5, 1.5, 0])
WHILE_FONT_SIZE = 50
WHILE_SCALE_FACTOR = 0.5
TAB_SIZE = 0.5
LINE_HEIGHT = 0.31

LABEL_FONT_SIZE = 40
LABEL_LINE_WIDTH = 5

VAR_FONT_SIZE = 30
VAR_GRID_POS = np.array([-3.5, -2.5, 0])

ALGO_GUY_POS = np.array([3.5, 0, 0])
ALGO_GUY_COLOR = BLUE_D

CHECK_COLOR = GREEN_C
CROSS_COLOR = RED_C


class WhileCycle(Scene):
    def get_algo_tex(self) -> Tuple[VGroup, VGroup]:
        algo = MathTex(r'\mathtt{while} \:\: n > 1 \:\: \mathtt{do}',
                       r'\mathtt{while} \:\: p_i \text{ dělí } n \:\: \mathtt{do}',
                       r'n \leftarrow n / p_i',
                       r'm_i \leftarrow m_i + 1',
                       r'p_{i+1} \leftarrow \text{ nejbližší prvočíslo větší než } p_i',
                       r'm_{i+1} \leftarrow 0',
                       r'i \leftarrow i + 1',
                       r'\mathtt{return} \:\: \{(p_i, m_i)\}',
                       font_size=WHILE_FONT_SIZE
                       ).arrange(DOWN, aligned_edge=LEFT)

        algo[1].shift(TAB_SIZE * RIGHT)
        algo[2].shift(2 * TAB_SIZE * RIGHT)
        algo[3].shift(2 * TAB_SIZE * RIGHT)
        algo[4].shift(TAB_SIZE * RIGHT)
        algo[5].shift(TAB_SIZE * RIGHT)
        algo[6].shift(TAB_SIZE * RIGHT)

        # keyword and variable colors
        algo[0][:5].set_color(KW_COLOR)
        algo[0][5:6].set_color(VAR_COLORS[0])
        algo[0][8:].set_color(KW_COLOR)

        algo[1][:5].set_color(KW_COLOR)
        algo[1][5:7].set_color(VAR_COLORS[1])
        algo[1][13:14].set_color(VAR_COLORS[0])
        algo[1][14:].set_color(KW_COLOR)

        algo[2][:1].set_color(VAR_COLORS[0])
        algo[2][2:3].set_color(VAR_COLORS[0])
        algo[2][4:].set_color(VAR_COLORS[1])

        algo[3][:2].set_color(VAR_COLORS[2])
        algo[3][3:5].set_color(VAR_COLORS[2])

        algo[4][:4].set_color(VAR_COLORS[1])
        algo[4][-2:].set_color(VAR_COLORS[1])

        algo[5][:4].set_color(VAR_COLORS[2])

        algo[7][:6].set_color(KW_COLOR)
        algo[7][8:10].set_color(VAR_COLORS[1])
        algo[7][11:13].set_color(VAR_COLORS[2])

        algo_hooks = VGroup(*[
            VMobject(stroke_color=KW_COLOR, stroke_opacity=1,
                     stroke_width=2).set_points_as_corners([
                         algo[4].get_corner(LEFT) + 1.8 * UP + 0.2 * RIGHT,
                         algo[4].get_corner(LEFT) + 0.3 * UP + 0.2 * RIGHT,
                         algo[4].get_corner(LEFT) + 0.3 * UP + 0.45 * RIGHT
                     ]),
            VMobject(stroke_color=KW_COLOR, stroke_opacity=1,
                     stroke_width=2).set_points_as_corners([
                         algo[7].get_corner(LEFT) + 4.5 * UP + 0.2 * RIGHT,
                         algo[7].get_corner(LEFT) + 0.3 * UP + 0.2 * RIGHT,
                         algo[7].get_corner(LEFT) + 0.3 * UP + 0.45 * RIGHT
                     ])
        ])

        return algo, algo_hooks

    def show_section_label(self, mobj: VMobject, text: str) -> None:
        sec_label_tex = Tex(text, font_size=LABEL_FONT_SIZE)
        sec_label_line = Line(
            start=ORIGIN,
            end=LABEL_LINE_WIDTH * RIGHT,
            stroke_width=2
        ).next_to(sec_label_tex, DOWN, 0.2)

        algo_label = VGroup(sec_label_tex, sec_label_line)
        algo_label.next_to(mobj, UP, 0.2)

        self.play(AnimationGroup(
            Create(sec_label_line),
            FadeIn(sec_label_tex, shift=0.2 * UP),
            lag_ratio=0.3
        ))

    def get_var_grid(self) -> Tuple[VGroup, VGroup]:
        rows = [
            MathTex(x, font_size=VAR_FONT_SIZE, color=VAR_COLORS[0])
            for x in ['n', '504', '63', '7', '7', '1']
        ] + [
            MathTex(x, font_size=VAR_FONT_SIZE, color=VAR_COLORS[1])
            for x in ['p_i', '2', '3', '5', '7', '11']
        ] + [
            MathTex(x, font_size=VAR_FONT_SIZE, color=VAR_COLORS[2])
            for x in ['m_i', '0', '0', '0', '0', '0']
        ] + [
            MathTex(x, font_size=VAR_FONT_SIZE)
            for x in ['i', '0', '1', '2', '3', '4']
        ]

        rows = VGroup(
            *rows
        ).arrange_in_grid(4, 6, (0.1, 0.2), row_alignments='c' * 4,
                          col_alignments='c' * 6, row_heights=[0.4] * 4,
                          col_widths=[0.8] * 6)

        header_line = Line(
            ORIGIN,
            (rows.width + 0.2) * RIGHT,
            stroke_width=1
        )
        first_col_line = Line(
            ORIGIN,
            (rows.height + 0.2) * DOWN,
            stroke_width=1
        )

        return rows, VGroup(header_line, first_col_line)

    def get_algo_counter(self, algo_tex: MathTex) -> VGroup:
        lines = VGroup(*[
            Line(ORIGIN, 0.9 * RIGHT, color=ALGO_GUY_COLOR, stroke_width=2),
            Line(ORIGIN, 0.9 * LEFT, color=ALGO_GUY_COLOR, stroke_width=2)
        ]).next_to(algo_tex, UP, aligned_edge=LEFT).shift(0.5 * DOWN)

        return lines

    def construct(self):
        # self.add(NumberPlane(background_line_style={
        #     'stroke_opacity': 0.3
        # }))

        self.next_section()
        # algorithm frame
        algo, algo_hooks = self.get_algo_tex()
        self.play(AnimationGroup(
            Write(algo),
            Create(algo_hooks[0]),
            Create(algo_hooks[1]),
            lag_ratio=0.25))
        algo = VGroup(algo, algo_hooks)
        self.pause(2)
        self.play(
            algo.animate.scale(WHILE_SCALE_FACTOR).move_to(
                WHILE_POS)
        )
        self.show_section_label(algo, 'Algoritmus')

        # variable grid frame
        var_grid, grid_lines = self.get_var_grid()
        var_grid.move_to(VAR_GRID_POS)
        grid_lines[0].next_to(var_grid[0], DOWN, 0.2, aligned_edge=LEFT)
        grid_lines[0].shift(0.1 * LEFT)
        grid_lines[1].next_to(var_grid[0], RIGHT, 0.3, aligned_edge=UP)
        grid_lines[1].shift(0.1 * UP)
        self.play(*[Write(var_grid[i * 6])
                  for i in range(4)],
                  Create(grid_lines))
        self.play(AnimationGroup(
            *[Write(var_grid[i * 6 + 1]) for i in range(4)],
            lag_ratio=0.2
        ))
        self.show_section_label(var_grid, 'Proměnné')

        # algorithm guy frame
        algo_guy_frame = Rectangle(ALGO_GUY_COLOR, 2, 5).move_to(ALGO_GUY_POS)
        self.play(Create(algo_guy_frame))
        self.show_section_label(algo_guy_frame, 'Algoritmař')

        algo_counter = self.get_algo_counter(algo)
        self.play(Create(algo_counter[0]), Create(algo_counter[1]))

        # step 1
        tex = MathTex(r'504 > 1?', font_size=WHILE_FONT_SIZE)
        tex[0][:3].set_color(VAR_COLORS[0])
        tex.move_to(algo_guy_frame.get_center())
        self.play(Write(tex))
        self.pause(1)
        check = MathTex(r'\checkmark', color=CHECK_COLOR,
                        font_size=WHILE_FONT_SIZE)
        check.next_to(tex, RIGHT)
        self.play(Write(check))

        algo_first_while_counter = algo_counter.copy()

        # step 2
        algo_next_line_counter = algo_counter.copy()
        algo_next_line_counter.shift(
            (TAB_SIZE - 0.1) * RIGHT + LINE_HEIGHT * DOWN)
        algo_next_line_counter.width = 2.1

        self.play(
            FadeOut(tex, check, shift=0.1*UP),
            Transform(algo_counter, algo_next_line_counter)
        )
        algo_second_while_counter = algo_counter.copy()

        tex = MathTex(r'2 \text{ dělí } 504?', font_size=WHILE_FONT_SIZE)
        tex[0][0].set_color(VAR_COLORS[1])
        tex[0][-4:-1].set_color(VAR_COLORS[0])
        tex.move_to(algo_guy_frame.get_center())
        check.next_to(tex, RIGHT)

        self.play(Write(tex))
        self.pause(1)
        self.play(Write(check))

        # step 3
        algo_next_line_counter.shift(
            (LINE_HEIGHT + 0.04) * DOWN + 0.275 * LEFT)
        algo_next_line_counter.width = 1.05

        self.play(
            FadeOut(tex, check, shift=0.1*UP),
            Transform(algo_counter, algo_next_line_counter)
        )

        tex = MathTex(r'n \leftarrow 504 / 2', r'= 252',
                      font_size=WHILE_FONT_SIZE)
        tex[0][0].set_color(VAR_COLORS[0])
        tex[0][-5:-2].set_color(VAR_COLORS[0])
        tex[0][-1].set_color(VAR_COLORS[1])
        tex[1][-3:].set_color(VAR_COLORS[0])
        tex.move_to(algo_guy_frame.get_center())
        tex.shift(RIGHT)

        self.play(Write(tex[0]))
        self.play(
            tex[0].animate.shift(LEFT),
            FadeIn(tex[1], shift=0.2 * RIGHT),
            tex[1].animate.shift(LEFT)
        )

        n = MathTex(r'252', color=VAR_COLORS[0],
                    font_size=VAR_FONT_SIZE).move_to(var_grid[1])
        self.play(Transform(var_grid[1], n))
        self.pause(1)

        # step 4
        algo_next_line_counter.shift(
            (LINE_HEIGHT + 0.05) * DOWN + 0.2 * RIGHT)
        algo_next_line_counter.width = 1.45

        self.play(
            FadeOut(tex, shift=0.1*UP),
            Transform(algo_counter, algo_next_line_counter)
        )

        tex = MathTex(r'm_0 \leftarrow 0 + 1', r'= 1',
                      font_size=WHILE_FONT_SIZE)
        tex[0][:2].set_color(VAR_COLORS[2])
        tex[0][3:4].set_color(VAR_COLORS[2])
        tex[1][-1].set_color(VAR_COLORS[2])
        tex.move_to(algo_guy_frame.get_center())
        tex.shift(0.5 * RIGHT)
        self.play(Write(tex[0]))
        self.play(
            tex[0].animate.shift(0.5 * LEFT),
            FadeIn(tex[1], shift=0.2 * RIGHT),
            tex[1].animate.shift(0.5 * LEFT)
        )
        m_i = MathTex(r'1', color=VAR_COLORS[2],
                      font_size=VAR_FONT_SIZE).move_to(var_grid[13])
        self.play(Transform(var_grid[13], m_i))
        self.pause(1)

        # step 5
        self.play(
            FadeOut(tex, shift=0.1*UP),
            Transform(algo_counter, algo_second_while_counter)
        )

        tex = MathTex(r'2 \text{ dělí } 252?', font_size=WHILE_FONT_SIZE)
        tex[0][0].set_color(VAR_COLORS[1])
        tex[0][-4:-1].set_color(VAR_COLORS[0])
        tex.move_to(algo_guy_frame)
        check.next_to(tex, RIGHT)

        self.play(Write(tex))
        self.pause(1)
        self.play(Write(check))

        # step 6
        algo_next_line_counter = algo_counter.copy()
        algo_next_line_counter.shift(
            (LINE_HEIGHT + 0.04) * DOWN + 0.275 * LEFT)
        algo_next_line_counter.width = 1.05

        self.play(
            FadeOut(tex, check, shift=0.1*UP),
            Transform(algo_counter, algo_next_line_counter)
        )

        tex = MathTex(r'n \leftarrow 252 / 2', r'= 126',
                      font_size=WHILE_FONT_SIZE)
        tex[0][0].set_color(VAR_COLORS[0])
        tex[0][-5:-2].set_color(VAR_COLORS[0])
        tex[0][-1].set_color(VAR_COLORS[1])
        tex[1][-3:].set_color(VAR_COLORS[0])
        tex.move_to(algo_guy_frame.get_center())
        tex.shift(RIGHT)

        self.play(Write(tex[0]))
        self.play(
            tex[0].animate.shift(LEFT),
            FadeIn(tex[1], shift=0.2 * RIGHT),
            tex[1].animate.shift(LEFT)
        )

        n = MathTex(r'126', color=VAR_COLORS[0],
                    font_size=VAR_FONT_SIZE).move_to(var_grid[1])
        self.play(Transform(var_grid[1], n))
        self.pause(1)

        # step 7
        algo_next_line_counter.shift(
            (LINE_HEIGHT + 0.05) * DOWN + 0.2 * RIGHT)
        algo_next_line_counter.width = 1.45

        self.play(
            FadeOut(tex, shift=0.1*UP),
            Transform(algo_counter, algo_next_line_counter)
        )

        tex = MathTex(r'm_0 \leftarrow 1 + 1', r'= 2',
                      font_size=WHILE_FONT_SIZE)
        tex[0][:2].set_color(VAR_COLORS[2])
        tex[0][3:4].set_color(VAR_COLORS[2])
        tex[1][-1].set_color(VAR_COLORS[2])
        tex.move_to(algo_guy_frame.get_center())
        tex.shift(0.5 * RIGHT)
        self.play(Write(tex[0]))
        self.play(
            tex[0].animate.shift(0.5 * LEFT),
            FadeIn(tex[1], shift=0.2 * RIGHT),
            tex[1].animate.shift(0.5 * LEFT)
        )
        m_i = MathTex(r'2', color=VAR_COLORS[2],
                      font_size=VAR_FONT_SIZE).move_to(var_grid[13])
        self.play(Transform(var_grid[13], m_i))
        self.pause(1)

        # step 8
        self.play(
            FadeOut(tex, shift=0.1*UP),
            Transform(algo_counter, algo_second_while_counter)
        )

        tex = MathTex(r'2 \text{ dělí } 126?', font_size=WHILE_FONT_SIZE)
        tex[0][0].set_color(VAR_COLORS[1])
        tex[0][-4:-1].set_color(VAR_COLORS[0])
        tex.move_to(algo_guy_frame)
        check.next_to(tex, RIGHT)

        self.play(Write(tex))
        self.pause(1)
        self.play(Write(check))

        # step 9
        algo_next_line_counter = algo_counter.copy()
        algo_next_line_counter.shift(
            (LINE_HEIGHT + 0.04) * DOWN + 0.275 * LEFT)
        algo_next_line_counter.width = 1.05

        self.play(
            FadeOut(tex, check, shift=0.1*UP),
            Transform(algo_counter, algo_next_line_counter)
        )

        tex = MathTex(r'n \leftarrow 126 / 2', r'= 63',
                      font_size=WHILE_FONT_SIZE)
        tex[0][0].set_color(VAR_COLORS[0])
        tex[0][-5:-2].set_color(VAR_COLORS[0])
        tex[0][-1].set_color(VAR_COLORS[1])
        tex[1][-3:].set_color(VAR_COLORS[0])
        tex.move_to(algo_guy_frame.get_center())
        tex.shift(0.7 * RIGHT)

        self.play(Write(tex[0]))
        self.play(
            tex[0].animate.shift(0.7 * LEFT),
            FadeIn(tex[1], shift=0.2 * RIGHT),
            tex[1].animate.shift(0.7 * LEFT)
        )

        n = MathTex(r'63', color=VAR_COLORS[0],
                    font_size=VAR_FONT_SIZE).move_to(var_grid[1])
        self.play(Transform(var_grid[1], n))
        self.pause(1)

        # step 10
        algo_next_line_counter.shift(
            (LINE_HEIGHT + 0.05) * DOWN + 0.2 * RIGHT)
        algo_next_line_counter.width = 1.45

        self.play(
            FadeOut(tex, shift=0.1*UP),
            Transform(algo_counter, algo_next_line_counter)
        )

        tex = MathTex(r'm_0 \leftarrow 2 + 1', r'= 3',
                      font_size=WHILE_FONT_SIZE)
        tex[0][:2].set_color(VAR_COLORS[2])
        tex[0][3:4].set_color(VAR_COLORS[2])
        tex[1][-1].set_color(VAR_COLORS[2])
        tex.move_to(algo_guy_frame.get_center())
        tex.shift(0.5 * RIGHT)
        self.play(Write(tex[0]))
        self.play(
            tex[0].animate.shift(0.5 * LEFT),
            FadeIn(tex[1], shift=0.2 * RIGHT),
            tex[1].animate.shift(0.5 * LEFT)
        )
        m_i = MathTex(r'3', color=VAR_COLORS[2],
                      font_size=VAR_FONT_SIZE).move_to(var_grid[13])
        self.play(Transform(var_grid[13], m_i))
        self.pause(1)

        # step 11
        self.play(
            FadeOut(tex, shift=0.1*UP),
            Transform(algo_counter, algo_second_while_counter)
        )

        tex = MathTex(r'2 \text{ dělí } 63?', font_size=WHILE_FONT_SIZE)
        tex[0][0].set_color(VAR_COLORS[1])
        tex[0][-3:-1].set_color(VAR_COLORS[0])
        tex.move_to(algo_guy_frame)
        cross = MathTex(r'\times', color=CROSS_COLOR,
                        font_size=WHILE_FONT_SIZE)
        cross.next_to(tex, RIGHT)

        self.play(Write(tex))
        self.play(Write(cross))
        self.pause(1)

        self.next_section()

        # step 12
        algo_next_line_counter = algo_counter.copy()
        algo_next_line_counter.shift(
            3.48 * LINE_HEIGHT * DOWN + 1.12 * RIGHT)
        algo_next_line_counter.width = 4.34
        self.play(
            FadeOut(tex, cross, shift=0.1*UP),
            Transform(algo_counter, algo_next_line_counter)
        )
        tex = MathTex(r'p_1 \leftarrow 3', font_size=WHILE_FONT_SIZE)
        tex[0][:2].set_color(VAR_COLORS[1])
        tex[0][-1].set_color(VAR_COLORS[1])
        tex.move_to(algo_guy_frame)

        self.play(Write(tex), Write(var_grid[8]))
        self.pause(1)

        # step 13
        algo_next_line_counter.shift(
            (LINE_HEIGHT + 0.04) * DOWN + 1.62 * LEFT)
        algo_next_line_counter.width = 1.1
        self.play(
            FadeOut(tex, shift=0.1*UP),
            Transform(algo_counter, algo_next_line_counter)
        )

        tex = MathTex(r'm_1 \leftarrow 0', font_size=WHILE_FONT_SIZE)
        tex[0][:2].set_color(VAR_COLORS[2])
        tex[0][-1].set_color(VAR_COLORS[2])
        tex.move_to(algo_guy_frame)

        self.play(Write(tex), Write(var_grid[14]))
        self.pause(1)

        # step 13
        algo_next_line_counter.shift(
            (LINE_HEIGHT + 0.04) * DOWN + 0.05 * LEFT)
        algo_next_line_counter.width = 1
        self.play(
            FadeOut(tex, shift=0.1*UP),
            Transform(algo_counter, algo_next_line_counter)
        )
        tex = MathTex(r'i \leftarrow 0 + 1', r'= 1', font_size=WHILE_FONT_SIZE)
        tex.move_to(algo_guy_frame)
        tex.shift(0.5 * RIGHT)
        self.play(Write(tex[0]))
        self.play(
            tex[0].animate.shift(0.5 * LEFT),
            FadeIn(tex[1], shift=0.2 * RIGHT),
            tex[1].animate.shift(0.5 * LEFT),
            Write(var_grid[2]),
            Write(var_grid[20])
        )
        self.pause(1)

        # step 14
        self.play(
            FadeOut(tex, shift=0.1*UP),
            Transform(algo_counter, algo_first_while_counter)
        )

        tex = MathTex(r'63 > 1?', font_size=WHILE_FONT_SIZE)
        tex[0][:2].set_color(VAR_COLORS[0])
        tex.move_to(algo_guy_frame.get_center())
        check.next_to(tex, RIGHT)

        self.play(Write(tex))
        self.pause(1)
        self.play(Write(check))

        # step 15
        self.play(
            FadeOut(tex, check, shift=0.1*UP),
            Transform(algo_counter, algo_second_while_counter)
        )

        tex = MathTex(r'3 \text{ dělí } 63?', font_size=WHILE_FONT_SIZE)
        tex[0][0].set_color(VAR_COLORS[1])
        tex[0][-3:-1].set_color(VAR_COLORS[0])
        tex.move_to(algo_guy_frame)
        check.next_to(tex, RIGHT)

        self.play(Write(tex))
        self.pause(1)
        self.play(Write(check))

        # step 16
        algo_next_line_counter = algo_counter.copy()
        algo_next_line_counter.shift(
            (LINE_HEIGHT + 0.04) * DOWN + 0.275 * LEFT)
        algo_next_line_counter.width = 1.05

        self.play(
            FadeOut(tex, check, shift=0.1*UP),
            Transform(algo_counter, algo_next_line_counter)
        )

        tex = MathTex(r'n \leftarrow 63 / 3', r'= 21',
                      font_size=WHILE_FONT_SIZE)
        tex[0][0].set_color(VAR_COLORS[0])
        tex[0][-4:-2].set_color(VAR_COLORS[0])
        tex[0][-1].set_color(VAR_COLORS[1])
        tex[1][-2:].set_color(VAR_COLORS[0])
        tex.move_to(algo_guy_frame)
        tex.shift(0.7 * RIGHT)

        self.play(Write(tex[0]))
        self.play(
            tex[0].animate.shift(0.7 * LEFT),
            FadeIn(tex[1], shift=0.2 * RIGHT),
            tex[1].animate.shift(0.7 * LEFT)
        )

        n = MathTex(r'21', color=VAR_COLORS[0],
                    font_size=VAR_FONT_SIZE).move_to(var_grid[2])
        self.play(Transform(var_grid[2], n))
        self.pause(1)

        # step 17
        algo_next_line_counter.shift(
            (LINE_HEIGHT + 0.05) * DOWN + 0.2 * RIGHT)
        algo_next_line_counter.width = 1.45

        self.play(
            FadeOut(tex, shift=0.1*UP),
            Transform(algo_counter, algo_next_line_counter)
        )

        tex = MathTex(r'm_1 \leftarrow 0 + 1', r'= 1',
                      font_size=WHILE_FONT_SIZE)
        tex[0][:2].set_color(VAR_COLORS[2])
        tex[0][3:4].set_color(VAR_COLORS[2])
        tex[1][-1].set_color(VAR_COLORS[2])
        tex.move_to(algo_guy_frame.get_center())
        tex.shift(0.5 * RIGHT)
        self.play(Write(tex[0]))
        self.play(
            tex[0].animate.shift(0.5 * LEFT),
            FadeIn(tex[1], shift=0.2 * RIGHT),
            tex[1].animate.shift(0.5 * LEFT)
        )
        m_i = MathTex(r'1', color=VAR_COLORS[2],
                      font_size=VAR_FONT_SIZE).move_to(var_grid[14])
        self.play(Transform(var_grid[14], m_i))
        self.pause(1)

        # step 18
        self.play(
            FadeOut(tex, shift=0.1*UP),
            Transform(algo_counter, algo_second_while_counter)
        )

        tex = MathTex(r'3 \text{ dělí } 21?', font_size=WHILE_FONT_SIZE)
        tex[0][0].set_color(VAR_COLORS[1])
        tex[0][-3:-1].set_color(VAR_COLORS[0])
        tex.move_to(algo_guy_frame)
        check.next_to(tex, RIGHT)

        self.play(Write(tex))
        self.pause(1)
        self.play(Write(check))

        # step 19
        algo_next_line_counter = algo_counter.copy()
        algo_next_line_counter.shift(
            (LINE_HEIGHT + 0.04) * DOWN + 0.275 * LEFT)
        algo_next_line_counter.width = 1.05

        self.play(
            FadeOut(tex, check, shift=0.1*UP),
            Transform(algo_counter, algo_next_line_counter)
        )

        tex = MathTex(r'n \leftarrow 21 / 3', r'= 7',
                      font_size=WHILE_FONT_SIZE)
        tex[0][0].set_color(VAR_COLORS[0])
        tex[0][-4:-2].set_color(VAR_COLORS[0])
        tex[0][-1].set_color(VAR_COLORS[1])
        tex[1][-1].set_color(VAR_COLORS[0])
        tex.move_to(algo_guy_frame)
        tex.shift(0.4 * RIGHT)

        self.play(Write(tex[0]))
        self.play(
            tex[0].animate.shift(0.4 * LEFT),
            FadeIn(tex[1], shift=0.2 * RIGHT),
            tex[1].animate.shift(0.4 * LEFT)
        )

        n = MathTex(r'7', color=VAR_COLORS[0],
                    font_size=VAR_FONT_SIZE).move_to(var_grid[2])
        self.play(Transform(var_grid[2], n))
        self.pause(1)

        # step 20
        algo_next_line_counter.shift(
            (LINE_HEIGHT + 0.05) * DOWN + 0.2 * RIGHT)
        algo_next_line_counter.width = 1.45

        self.play(
            FadeOut(tex, shift=0.1*UP),
            Transform(algo_counter, algo_next_line_counter)
        )

        tex = MathTex(r'm_1 \leftarrow 1 + 1', r'= 2',
                      font_size=WHILE_FONT_SIZE)
        tex[0][:2].set_color(VAR_COLORS[2])
        tex[0][3:4].set_color(VAR_COLORS[2])
        tex[1][-1].set_color(VAR_COLORS[2])
        tex.move_to(algo_guy_frame.get_center())
        tex.shift(0.5 * RIGHT)
        self.play(Write(tex[0]))
        self.play(
            tex[0].animate.shift(0.5 * LEFT),
            FadeIn(tex[1], shift=0.2 * RIGHT),
            tex[1].animate.shift(0.5 * LEFT)
        )
        m_i = MathTex(r'2', color=VAR_COLORS[2],
                      font_size=VAR_FONT_SIZE).move_to(var_grid[14])
        self.play(Transform(var_grid[14], m_i))
        self.pause(1)

        # step 21
        self.play(
            FadeOut(tex, shift=0.1*UP),
            Transform(algo_counter, algo_second_while_counter)
        )

        tex = MathTex(r'3 \text{ dělí } 7?', font_size=WHILE_FONT_SIZE)
        tex[0][0].set_color(VAR_COLORS[1])
        tex[0][-2].set_color(VAR_COLORS[0])
        tex.move_to(algo_guy_frame)
        cross = MathTex(r'\times', color=CROSS_COLOR,
                        font_size=WHILE_FONT_SIZE)
        cross.next_to(tex, RIGHT)

        self.play(Write(tex))
        self.play(Write(cross))
        self.pause(1)

        self.next_section()

        # step 22
        algo_next_line_counter = algo_counter.copy()
        algo_next_line_counter.shift(
            3.48 * LINE_HEIGHT * DOWN + 1.12 * RIGHT)
        algo_next_line_counter.width = 4.34
        self.play(
            FadeOut(tex, cross, shift=0.1*UP),
            Transform(algo_counter, algo_next_line_counter)
        )
        tex = MathTex(r'p_2 \leftarrow 5', font_size=WHILE_FONT_SIZE)
        tex[0][:2].set_color(VAR_COLORS[1])
        tex[0][-1].set_color(VAR_COLORS[1])
        tex.move_to(algo_guy_frame)

        self.play(Write(tex), Write(var_grid[9]))
        self.pause(1)

        # step 23
        algo_next_line_counter.shift(
            (LINE_HEIGHT + 0.04) * DOWN + 1.62 * LEFT)
        algo_next_line_counter.width = 1.1
        self.play(
            FadeOut(tex, shift=0.1*UP),
            Transform(algo_counter, algo_next_line_counter)
        )

        tex = MathTex(r'm_2 \leftarrow 0', font_size=WHILE_FONT_SIZE)
        tex[0][:2].set_color(VAR_COLORS[2])
        tex[0][-1].set_color(VAR_COLORS[2])
        tex.move_to(algo_guy_frame)

        self.play(Write(tex), Write(var_grid[15]))
        self.pause(1)

        # step 24
        algo_next_line_counter.shift(
            (LINE_HEIGHT + 0.04) * DOWN + 0.05 * LEFT)
        algo_next_line_counter.width = 1
        self.play(
            FadeOut(tex, shift=0.1*UP),
            Transform(algo_counter, algo_next_line_counter)
        )
        tex = MathTex(r'i \leftarrow 1 + 1', r'= 2', font_size=WHILE_FONT_SIZE)
        tex.move_to(algo_guy_frame)
        tex.shift(0.5 * RIGHT)
        self.play(Write(tex[0]))
        self.play(
            tex[0].animate.shift(0.5 * LEFT),
            FadeIn(tex[1], shift=0.2 * RIGHT),
            tex[1].animate.shift(0.5 * LEFT),
            Write(var_grid[3]),
            Write(var_grid[21])
        )
        self.pause(1)

        # step 25
        self.play(
            FadeOut(tex, shift=0.1*UP),
            Transform(algo_counter, algo_second_while_counter)
        )

        tex = MathTex(r'5 \text{ dělí } 7?', font_size=WHILE_FONT_SIZE)
        tex[0][0].set_color(VAR_COLORS[1])
        tex[0][-2].set_color(VAR_COLORS[0])
        tex.move_to(algo_guy_frame)
        cross = MathTex(r'\times', color=CROSS_COLOR,
                        font_size=WHILE_FONT_SIZE)
        cross.next_to(tex, RIGHT)

        self.play(Write(tex))
        self.play(Write(cross))
        self.pause(1)

        self.next_section()

        # step 26
        algo_next_line_counter = algo_counter.copy()
        algo_next_line_counter.shift(
            3.48 * LINE_HEIGHT * DOWN + 1.12 * RIGHT)
        algo_next_line_counter.width = 4.34
        self.play(
            FadeOut(tex, cross, shift=0.1*UP),
            Transform(algo_counter, algo_next_line_counter)
        )
        tex = MathTex(r'p_3 \leftarrow 7', font_size=WHILE_FONT_SIZE)
        tex[0][:2].set_color(VAR_COLORS[1])
        tex[0][-1].set_color(VAR_COLORS[1])
        tex.move_to(algo_guy_frame)

        self.play(Write(tex), Write(var_grid[10]))
        self.pause(1)

        # step 27
        algo_next_line_counter.shift(
            (LINE_HEIGHT + 0.04) * DOWN + 1.62 * LEFT)
        algo_next_line_counter.width = 1.1
        self.play(
            FadeOut(tex, shift=0.1*UP),
            Transform(algo_counter, algo_next_line_counter)
        )

        tex = MathTex(r'm_3 \leftarrow 0', font_size=WHILE_FONT_SIZE)
        tex[0][:2].set_color(VAR_COLORS[2])
        tex[0][-1].set_color(VAR_COLORS[2])
        tex.move_to(algo_guy_frame)

        self.play(Write(tex), Write(var_grid[16]))
        self.pause(1)

        # step 28
        algo_next_line_counter.shift(
            (LINE_HEIGHT + 0.04) * DOWN + 0.05 * LEFT)
        algo_next_line_counter.width = 1
        self.play(
            FadeOut(tex, shift=0.1*UP),
            Transform(algo_counter, algo_next_line_counter)
        )
        tex = MathTex(r'i \leftarrow 2 + 1', r'= 3', font_size=WHILE_FONT_SIZE)
        tex.move_to(algo_guy_frame)
        tex.shift(0.5 * RIGHT)
        self.play(Write(tex[0]))
        self.play(
            tex[0].animate.shift(0.5 * LEFT),
            FadeIn(tex[1], shift=0.2 * RIGHT),
            tex[1].animate.shift(0.5 * LEFT),
            Write(var_grid[4]),
            Write(var_grid[22])
        )
        self.pause(1)

        self.next_section()

        # step 29
        self.play(
            FadeOut(tex, shift=0.1*UP),
            Transform(algo_counter, algo_second_while_counter)
        )

        tex = MathTex(r'7 \text{ dělí } 7?', font_size=WHILE_FONT_SIZE)
        tex[0][0].set_color(VAR_COLORS[1])
        tex[0][-2].set_color(VAR_COLORS[0])
        tex.move_to(algo_guy_frame)
        check.next_to(tex, RIGHT)

        self.play(Write(tex))
        self.pause(1)
        self.play(Write(check))

        # step 30
        algo_next_line_counter = algo_counter.copy()
        algo_next_line_counter.shift(
            (LINE_HEIGHT + 0.04) * DOWN + 0.275 * LEFT)
        algo_next_line_counter.width = 1.05

        self.play(
            FadeOut(tex, check, shift=0.1*UP),
            Transform(algo_counter, algo_next_line_counter)
        )

        tex = MathTex(r'n \leftarrow 7 / 7', r'= 1',
                      font_size=WHILE_FONT_SIZE)
        tex[0][0].set_color(VAR_COLORS[0])
        tex[0][-3].set_color(VAR_COLORS[0])
        tex[0][-1].set_color(VAR_COLORS[1])
        tex[1][-1].set_color(VAR_COLORS[0])
        tex.move_to(algo_guy_frame)
        tex.shift(0.4 * RIGHT)

        self.play(Write(tex[0]))
        self.play(
            tex[0].animate.shift(0.4 * LEFT),
            FadeIn(tex[1], shift=0.2 * RIGHT),
            tex[1].animate.shift(0.4 * LEFT)
        )

        n = MathTex(r'1', color=VAR_COLORS[0],
                    font_size=VAR_FONT_SIZE).move_to(var_grid[4])
        self.play(Transform(var_grid[4], n))
        self.pause(1)

        # step 31
        algo_next_line_counter.shift(
            (LINE_HEIGHT + 0.05) * DOWN + 0.2 * RIGHT)
        algo_next_line_counter.width = 1.45

        self.play(
            FadeOut(tex, shift=0.1*UP),
            Transform(algo_counter, algo_next_line_counter)
        )

        tex = MathTex(r'm_3 \leftarrow 0 + 1', r'= 1',
                      font_size=WHILE_FONT_SIZE)
        tex[0][:2].set_color(VAR_COLORS[2])
        tex[0][3:4].set_color(VAR_COLORS[2])
        tex[1][-1].set_color(VAR_COLORS[2])
        tex.move_to(algo_guy_frame.get_center())
        tex.shift(0.5 * RIGHT)
        self.play(Write(tex[0]))
        self.play(
            tex[0].animate.shift(0.5 * LEFT),
            FadeIn(tex[1], shift=0.2 * RIGHT),
            tex[1].animate.shift(0.5 * LEFT)
        )
        m_i = MathTex(r'1', color=VAR_COLORS[2],
                      font_size=VAR_FONT_SIZE).move_to(var_grid[16])
        self.play(Transform(var_grid[16], m_i))
        self.pause(1)

        self.next_section()

        # step 32
        self.play(
            FadeOut(tex, shift=0.1*UP),
            Transform(algo_counter, algo_second_while_counter)
        )

        tex = MathTex(r'7 \text{ dělí } 1?', font_size=WHILE_FONT_SIZE)
        tex[0][0].set_color(VAR_COLORS[1])
        tex[0][-2].set_color(VAR_COLORS[0])
        tex.move_to(algo_guy_frame)
        cross = MathTex(r'\times', color=CROSS_COLOR,
                        font_size=WHILE_FONT_SIZE)
        cross.next_to(tex, RIGHT)

        self.play(Write(tex))
        self.play(Write(cross))
        self.pause(1)

        # step 33
        algo_next_line_counter = algo_counter.copy()
        algo_next_line_counter.shift(
            3.48 * LINE_HEIGHT * DOWN + 1.12 * RIGHT)
        algo_next_line_counter.width = 4.34
        self.play(
            FadeOut(tex, cross, shift=0.1*UP),
            Transform(algo_counter, algo_next_line_counter)
        )
        tex = MathTex(r'p_4 \leftarrow 11', font_size=WHILE_FONT_SIZE)
        tex[0][:2].set_color(VAR_COLORS[1])
        tex[0][-2:].set_color(VAR_COLORS[1])
        tex.move_to(algo_guy_frame)

        self.play(Write(tex), Write(var_grid[11]))
        self.pause(1)

        # step 34
        algo_next_line_counter.shift(
            (LINE_HEIGHT + 0.04) * DOWN + 1.62 * LEFT)
        algo_next_line_counter.width = 1.1
        self.play(
            FadeOut(tex, shift=0.1*UP),
            Transform(algo_counter, algo_next_line_counter)
        )

        tex = MathTex(r'm_4 \leftarrow 0', font_size=WHILE_FONT_SIZE)
        tex[0][:2].set_color(VAR_COLORS[2])
        tex[0][-1].set_color(VAR_COLORS[2])
        tex.move_to(algo_guy_frame)

        self.play(Write(tex), Write(var_grid[17]))
        self.pause(1)

        # step 35
        algo_next_line_counter.shift(
            (LINE_HEIGHT + 0.04) * DOWN + 0.05 * LEFT)
        algo_next_line_counter.width = 1
        self.play(
            FadeOut(tex, shift=0.1*UP),
            Transform(algo_counter, algo_next_line_counter)
        )
        tex = MathTex(r'i \leftarrow 3 + 1', r'= 4', font_size=WHILE_FONT_SIZE)
        tex.move_to(algo_guy_frame)
        tex.shift(0.5 * RIGHT)
        self.play(Write(tex[0]))
        self.play(
            tex[0].animate.shift(0.5 * LEFT),
            FadeIn(tex[1], shift=0.2 * RIGHT),
            tex[1].animate.shift(0.5 * LEFT),
            Write(var_grid[5]),
            Write(var_grid[23])
        )
        self.pause(1)

        self.next_section()

        # step 36
        self.play(
            FadeOut(tex, shift=0.1*UP),
            Transform(algo_counter, algo_first_while_counter)
        )

        tex = MathTex(r'1 > 1?', font_size=WHILE_FONT_SIZE)
        tex[0][0].set_color(VAR_COLORS[0])
        tex.move_to(algo_guy_frame.get_center())
        cross.next_to(tex, RIGHT)

        self.play(Write(tex))
        self.pause(1)
        self.play(Write(cross))

        algo_next_line_counter = algo_counter.copy()
        algo_next_line_counter.shift(
            7.9 * LINE_HEIGHT * DOWN + 0.1 * RIGHT
        )
        algo_next_line_counter.width = 2
        self.play(
            FadeOut(tex, cross, shift=0.1*UP),
            Transform(algo_counter, algo_next_line_counter)
        )

        tex = MathTex(r'\{', r'(2, 3),', r'(3, 2),',
                      r'(5, 0),', r'(7, 1),', r'(11, 0)', r'\}',
                      font_size=WHILE_FONT_SIZE).scale(0.6)
        tex.move_to(algo_guy_frame)

        for i in range(1, 5):
            tex[i][1].set_color(VAR_COLORS[1])
            tex[i][-3].set_color(VAR_COLORS[2])

        tex[5][1:3].set_color(VAR_COLORS[1])
        tex[5][-2].set_color(VAR_COLORS[2])

        self.play(Write(tex))
        self.play(Uncreate(algo_counter[0]), Uncreate(algo_counter[1]))
        self.pause(2)

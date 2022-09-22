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

LABEL_FONT_SIZE = 40
LABEL_LINE_WIDTH = 5

VAR_FONT_SIZE = 30
VAR_GRID_POS = np.array([-3.5, -2.5, 0])


class WhileCycle(Scene):
    def get_algo_tex(self) -> Tuple[VGroup, VGroup]:
        algo = MathTex(r'&\mathtt{while} \:\: n > 1 \:\: \mathtt{do}\\' +
                       r'&\hspace*{12pt}\mathtt{while} \:\: p_i \text{ dělí } n \:\: \mathtt{do}\\' +
                       r'&\hspace*{24pt}n \leftarrow n / p_i\\' +
                       r'&\hspace*{24pt}m_i \leftarrow m_i + 1\\' +
                       r'&\hspace*{12pt}p_{i+1} \leftarrow \text{ nejbližší prvočíslo větší než } p_i\\' +
                       r'&\hspace*{12pt}m_{i+1} \leftarrow 0\\' +
                       r'&\hspace*{12pt}i \leftarrow i + 1\\' +
                       r'&\mathtt{return} \:\: \{(p_i, m_i)\}',
                       font_size=WHILE_FONT_SIZE)

        # while/do/return colors
        algo[0][:5].set_color(KW_COLOR)
        algo[0][8:10].set_color(KW_COLOR)
        algo[0][10:15].set_color(KW_COLOR)
        algo[0][24:26].set_color(KW_COLOR)
        algo[0][-15:-9].set_color(KW_COLOR)

        # n colors
        algo[0][5:6].set_color(VAR_COLORS[0])
        algo[0][23:24].set_color(VAR_COLORS[0])
        algo[0][26:27].set_color(VAR_COLORS[0])
        algo[0][28:29].set_color(VAR_COLORS[0])

        # p_i colors
        algo[0][15:17].set_color(VAR_COLORS[1])
        algo[0][30:32].set_color(VAR_COLORS[1])
        algo[0][39:43].set_color(VAR_COLORS[1])
        algo[0][79:81].set_color(VAR_COLORS[1])
        algo[0][-7:-5].set_color(VAR_COLORS[1])

        # m_i colors
        algo[0][32:34].set_color(VAR_COLORS[2])
        algo[0][35:37].set_color(VAR_COLORS[2])
        algo[0][81:85].set_color(VAR_COLORS[2])
        algo[0][-4:-2].set_color(VAR_COLORS[2])

        algo_hooks = VGroup(*[
            VMobject(stroke_color=KW_COLOR, stroke_opacity=1,
                     stroke_width=2).set_points_as_corners([
                         np.array([-3.7, 1.65, 0]), np.array([-3.7, 0, 0]),
                         np.array([-3.25, 0, 0])]),
            VMobject(stroke_color=KW_COLOR, stroke_opacity=1,
                     stroke_width=2).set_points_as_corners([
                         np.array([-4.35, 2.45, 0]
                                  ), np.array([-4.35, -2.3, 0]),
                         np.array([-3.9, -2.3, 0])])
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
        rows =\
            [MathTex(x, font_size=VAR_FONT_SIZE, color=VAR_COLORS[0])
             for x in ['n', '504', '63', '7', '7']] +\
            [MathTex(x, font_size=VAR_FONT_SIZE, color=VAR_COLORS[1])
             for x in ['p_i', '2', '3', '5', '7']] +\
            [MathTex(x, font_size=VAR_FONT_SIZE, color=VAR_COLORS[2])
             for x in ['m_i', '0', '0', '0', '0']] +\
            [MathTex(x, font_size=VAR_FONT_SIZE)
             for x in ['i', '0', '1', '2', '3']]

        rows = VGroup(
            *rows
        ).arrange_in_grid(4, 5, (0.1, 0.2), row_alignments='c' * 4,
                          col_alignments='c' * 5, row_heights=[0.4] * 4,
                          col_widths=[0.8] * 5)

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

    def construct(self):
        # self.add(NumberPlane(background_line_style={
        #     'stroke_opacity': 0.3
        # }))
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
        var_grid, grid_lines = self.get_var_grid()
        var_grid.move_to(VAR_GRID_POS)
        grid_lines[0].next_to(var_grid[0], DOWN, 0.2, aligned_edge=LEFT)
        grid_lines[0].shift(0.1 * LEFT)
        grid_lines[1].next_to(var_grid[0], RIGHT, 0.3, aligned_edge=UP)
        grid_lines[1].shift(0.1 * UP)
        self.show_section_label(var_grid, 'Proměnné')
        # self.play(*[Write(var_grid[i * 5])
        #           for i in range(4)], Create(grid_lines))
        self.add(var_grid)
        self.play(Create(grid_lines))
        self.pause(2)

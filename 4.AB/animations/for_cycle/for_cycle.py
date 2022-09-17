from typing import Tuple
import numpy as np
from manim import *

FOR_TEX_FONT_SIZE = 80
FOR_KW_COLOR = YELLOW
FOR_SET_COLORS = [
    TEAL_C,
    PINK
]
FOR_TEX_SHIFT = 4.5 * LEFT + 2.5 * UP
FOR_TEX_SCALE_FACTOR = 0.5

SET_ELEMENT_FONT_SIZE = 50
SET_WIDTH = 2.5
SET_LABEL_FONT_SIZE = 70


class ForCycle(Scene):
    def for_cycle_tex(self) -> MathTex:
        tex = MathTex(r'\mathtt{for} \; &x \in A \; \mathtt{do} \\' +
                      r'&B \leftarrow B \cup \{2 \cdot x\}',
                      font_size=FOR_TEX_FONT_SIZE)
        tex[0][0:3].set_color(FOR_KW_COLOR)
        tex[0][6:8].set_color(FOR_KW_COLOR)
        tex[0][5:6].set_color(FOR_SET_COLORS[0])
        tex[0][8:9].set_color(FOR_SET_COLORS[1])
        tex[0][10:11].set_color(FOR_SET_COLORS[1])
        return tex

    def set_values(self, values: list[int], color: str) -> VGroup:
        values_tex = VGroup(*[
            Tex(f'{value}', font_size=SET_ELEMENT_FONT_SIZE,
                color=color)
            for value in values]
        ).arrange_in_grid(
            rows=1,
            cols=len(values),
            row_alignments='u',
            col_alignments='c' * len(values),
            col_widths=[SET_WIDTH / len(values)] * len(values)
        )

        return values_tex

    def animate_set_elem(self, A_elems: VGroup, A_values: list[int],
                         B_elems: VGroup, B_values: list[int],
                         index: int) -> Tuple[VMobject, VMobject]:
        trans_A = MathTex(
            f'x = {A_values[index]}', font_size=SET_ELEMENT_FONT_SIZE)
        trans_A[0][2:3].set_color(FOR_SET_COLORS[0])
        trans_A.next_to(A_elems, DOWN, 0.83)

        trans_B = MathTex(
            f'2 \\cdot x = {B_values[index]}', font_size=SET_ELEMENT_FONT_SIZE)
        trans_B[0][4:].set_color(FOR_SET_COLORS[1])
        trans_B.next_to(trans_A, DOWN)

        if B_values[index] >= 10:
            trans_B.shift(0.18 * LEFT)
        else:
            trans_B.shift(0.3 * LEFT)

        A_elem_copy = A_elems[index].copy()
        A_elem_copy.remove()
        self.play(Transform(A_elem_copy, trans_A))
        self.play(Transform(trans_A, trans_B))
        self.play(Write(B_elems[index]))

        return A_elem_copy, trans_A

    def construct(self):
        # for cycle anim
        for_tex = self.for_cycle_tex()
        self.play(Write(for_tex))
        self.pause(2)
        self.play(
            for_tex.animate.shift(FOR_TEX_SHIFT).scale(FOR_TEX_SCALE_FACTOR)
        )

        A_numbers = [5, 3, 1, 9]
        B_numbers = [2 * a for a in A_numbers]
        # set A anim
        A_set_values = self.set_values(A_numbers, FOR_SET_COLORS[0])
        A_brace = Brace(A_set_values, UP, 0.5, 1)
        A_brace_text = MathTex(r'A', font_size=SET_LABEL_FONT_SIZE,
                               color=FOR_SET_COLORS[0])
        A_label = VGroup(A_brace, A_brace_text).arrange(UP)
        A_label.next_to(A_set_values, UP)
        A_set = VGroup(A_set_values, A_label)
        A_set.next_to(for_tex, RIGHT, 2.5, UP)
        self.play(
            FadeIn(A_label, shift=0.3 * UP),
            Write(A_set_values)
        )

        # set B anim
        B_set_values = self.set_values(B_numbers, FOR_SET_COLORS[1])
        B_brace = Brace(B_set_values, DOWN, 0.5, 1)
        B_brace_text = MathTex(
            r'B', font_size=SET_LABEL_FONT_SIZE, color=FOR_SET_COLORS[1])
        B_label = VGroup(B_brace, B_brace_text).arrange(DOWN)
        B_label.next_to(B_set_values, DOWN)
        B_set = VGroup(B_set_values, B_label)
        B_set.next_to(A_set, DOWN, 3.5, UP)
        self.play(
            FadeIn(B_label, shift=0.3*DOWN)
        )
        self.pause(2)

        # cycle anim
        frame_next = SurroundingRectangle(A_set_values[0], color=FOR_KW_COLOR)
        self.play(Create(frame_next))
        for index, _ in enumerate(A_numbers):
            tr_A, tr_B = self.animate_set_elem(A_set_values, A_numbers,
                                               B_set_values, B_numbers, index)
            self.pause(1)
            try:
                frame_prev = frame_next
                frame_next = SurroundingRectangle(A_set_values[index + 1],
                                                  color=FOR_KW_COLOR)
                self.play(Create(frame_next), Uncreate(
                    frame_prev), Unwrite(tr_A), Unwrite(tr_B))
            except IndexError:
                self.play(Uncreate(frame_prev), Unwrite(tr_A), Unwrite(tr_B))

        self.pause(1)

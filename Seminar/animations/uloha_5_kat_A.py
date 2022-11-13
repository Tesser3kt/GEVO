import numpy as np
from manim import *

from uloha_5_kat_A_config import *


def angle_bisector(p: Line, q: Line) -> Line:
    """ Return the angle bisector of two lines."""
    p = p.copy()
    q = q.copy()

    b = Line(p.get_start(), p.get_start() + 10 * RIGHT,
             color=BISECTOR_COLOR, stroke_width=BISECTOR_STROKE_WIDTH)
    b.rotate((p.get_angle() + q.get_angle()) / 2, about_point=b.get_start())

    return b


class Uloha5(Scene):
    def construct(self):
        # create ABC
        ABC = Polygon(
            np.array([-6, 0, 0]),
            np.array([-3, 6, 0]),
            np.array([6, 0, 0])
        ).set_stroke(ABC_COLOR, ABC_STROKE_WIDTH).set_z_index(ABC_Z_INDEX)
        ABC.move_to(ORIGIN)

        # label ABC
        A = MathTex("A", color=ABC_COLOR).next_to(
            ABC.get_vertices()[0], DOWN + LEFT, buff=0.1)
        B = MathTex("B", color=ABC_COLOR).next_to(
            ABC.get_vertices()[1], 0.2 * LEFT + UP, buff=0.1)
        C = MathTex("C", color=ABC_COLOR).next_to(
            ABC.get_vertices()[2], RIGHT + DOWN, buff=0.1)

        self.play(Create(ABC), Write(A), Write(B), Write(C))

        # get ABC sides
        AB = Line(ABC.get_vertices()[0], ABC.get_vertices()[1])
        BC = Line(ABC.get_vertices()[1], ABC.get_vertices()[2])
        AC = Line(ABC.get_vertices()[0], ABC.get_vertices()[2])

        b = angle_bisector(AB, AC)
        D = Intersection(ABC, b, color=GREEN, fill_opacity=1, z_index=10)

        self.play(Create(b), Create(D))

        self.pause(2)

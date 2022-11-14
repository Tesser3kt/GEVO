import numpy as np
from manim import *

from uloha_5_kat_A_config import *


def angle_bisector(p: Line, q: Line) -> Line:
<<<<<<< HEAD
    """ Returns the angle bisector of the angle between the two lines. """

    length = max(p.get_length(), q.get_length())
    angle = (p.get_angle() + q.get_angle()) / 2
    bisector = DashedLine(p.get_start(), p.get_start() +
                          length * RIGHT).rotate(angle,
                                                 about_point=p.get_start())

    return bisector


def line_intersection(p: Line, q: Line) -> np.ndarray:
    """ Returns the intersection point of the two lines. """

    p1 = p.get_start()
    p2 = p.get_end()
    p3 = q.get_start()
    p4 = q.get_end()

    x1, y1 = p1[0], p1[1]
    x2, y2 = p2[0], p2[1]
    x3, y3 = p3[0], p3[1]
    x4, y4 = p4[0], p4[1]

    x = ((x1 * y2 - y1 * x2) * (x3 - x4) - (x1 - x2) * (x3 * y4 - y3 * x4)) / \
        ((x1 - x2) * (y3 - y4) - (y1 - y2) * (x3 - x4))
    y = ((x1 * y2 - y1 * x2) * (y3 - y4) - (y1 - y2) * (x3 * y4 - y3 * x4)) / \
        ((x1 - x2) * (y3 - y4) - (y1 - y2) * (x3 - x4))

    return np.array([x, y, 0])
=======
    """ Return the angle bisector of two lines."""
    p = p.copy()
    q = q.copy()

    b = Line(p.get_start(), p.get_start() + 10 * RIGHT,
             color=BISECTOR_COLOR, stroke_width=BISECTOR_STROKE_WIDTH)
    b.rotate((p.get_angle() + q.get_angle()) / 2, about_point=b.get_start())

    return b
>>>>>>> d30123628076a7a21cb955a8c888b3a99b42b859


class Uloha5(Scene):
    def construct(self):
<<<<<<< HEAD

        self.next_section("Intro", skip_animations=False)

        ABC = Polygon(
            np.array([-6, 0, 0]),
            np.array([-3, 6, 0]),
            np.array([6, 0, 0]),
            stroke_color=ABC_COLOR,
            stroke_width=ABC_STROKE_WIDTH,
            z_index=ABC_Z_INDEX
        ).move_to(ORIGIN)

        A, B, C = tuple(ABC.get_vertices())
        A_label = MathTex("A", color=ABC_COLOR).next_to(
            A, DOWN + LEFT, buff=0.1)
        B_label = MathTex("B", color=ABC_COLOR).next_to(B, UP, buff=0.15)
        C_label = MathTex("C", color=ABC_COLOR).next_to(
            C, DOWN + RIGHT, buff=0.1)

        self.play(Create(ABC), Write(A_label), Write(B_label), Write(C_label))

        AB = Line(A, B, color=ABC_COLOR, stroke_width=ABC_STROKE_WIDTH)
        BC = Line(B, C, color=ABC_COLOR, stroke_width=ABC_STROKE_WIDTH)
        AC = Line(A, C, color=ABC_COLOR, stroke_width=ABC_STROKE_WIDTH)

        AD = angle_bisector(AB, AC)
        AD.set_stroke(color=AD_COLOR, width=AD_STROKE_WIDTH)
        AD.set_z_index(AD_Z_INDEX)

        # D = Dot(line_intersection(BC, AD), color=DOT_COLOR,
        #         radius=DOT_RADIUS, stroke_width=DOT_STROKE_WIDTH,
        #         stroke_opacity=DOT_STROKE_OPACITY,
        #         fill_opacity=DOT_FILL_OPACITY,
        #         z_index=DOT_Z_INDEX)
        # D_label = MathTex("D", color=DOT_COLOR).next_to(D, UP, buff=0.2)

        D = Dot(AC.get_center(), color=DOT_COLOR,
                radius=DOT_RADIUS, stroke_width=DOT_STROKE_WIDTH,
                stroke_opacity=DOT_STROKE_OPACITY,
                fill_opacity=DOT_FILL_OPACITY,
                z_index=DOT_Z_INDEX)
        E = Dot(AB.get_center(), color=DOT_COLOR,
                radius=DOT_RADIUS, stroke_width=DOT_STROKE_WIDTH,
                stroke_opacity=DOT_STROKE_OPACITY,
                fill_opacity=DOT_FILL_OPACITY,
                z_index=DOT_Z_INDEX)

        D_label = MathTex("D", color=DOT_COLOR).next_to(D, DOWN, buff=0.2)
        E_label = MathTex("E", color=DOT_COLOR).next_to(E, LEFT, buff=0.2)

        d = DashedLine(AC.get_start(), AC.get_end(),
                       color=AD_COLOR, stroke_width=AD_STROKE_WIDTH,
                       z_index=AD_Z_INDEX).rotate(PI / 2,
                                                  about_point=D.get_center())
        e = DashedLine(AB.get_start(), AB.get_end(),
                       color=AD_COLOR, stroke_width=AD_STROKE_WIDTH,
                       z_index=AD_Z_INDEX)
        e.set_angle(0).shift(3 * RIGHT)
        e.set_length(8)
        e.rotate(AB.get_angle(), about_point=AB.get_start())
        e.rotate(-PI / 2, about_point=E.get_center())
        alpha = Angle(AC, AB, radius=ANGLE_RADIUS, color=ANGLE_COLOR)
        alpha_label = MathTex("\\alpha", color=ANGLE_COLOR).next_to(
            alpha, buff=0.1).shift(0.7 * LEFT + 0.1 * DOWN)

        self.play(
            AnimationGroup(DrawBorderThenFill(D), Write(D_label),
                           lag_ratio=0.4),
            AnimationGroup(DrawBorderThenFill(E), Write(E_label),
                           lag_ratio=0.4),
            AnimationGroup(Create(alpha), Write(alpha_label),
                           lag_ratio=0.4)
        )

        self.play(Create(d), Create(e), Create(AD))

        self.next_section("Inner Triangle", skip_animations=False)
        self.pause(2)

        K = Dot(line_intersection(e, d), color=INNER_DOT_COLOR,
                radius=INNER_DOT_RADIUS, stroke_width=INNER_DOT_STROKE_WIDTH,
                stroke_opacity=INNER_DOT_STROKE_OPACITY,
                fill_opacity=INNER_DOT_FILL_OPACITY,
                z_index=INNER_DOT_Z_INDEX)
        L = Dot(line_intersection(AD, d), color=INNER_DOT_COLOR,
                radius=INNER_DOT_RADIUS, stroke_width=INNER_DOT_STROKE_WIDTH,
                stroke_opacity=INNER_DOT_STROKE_OPACITY,
                fill_opacity=INNER_DOT_FILL_OPACITY,
                z_index=INNER_DOT_Z_INDEX)
        M = Dot(line_intersection(AD, e), color=INNER_DOT_COLOR,
                radius=INNER_DOT_RADIUS, stroke_width=INNER_DOT_STROKE_WIDTH,
                stroke_opacity=INNER_DOT_STROKE_OPACITY,
                fill_opacity=INNER_DOT_FILL_OPACITY,
                z_index=INNER_DOT_Z_INDEX)

        K_label = MathTex("K", color=INNER_DOT_COLOR).next_to(
            K, DOWN + LEFT, buff=0.1)
        L_label = MathTex("L", color=INNER_DOT_COLOR).next_to(
            L, 3 * UP + RIGHT, buff=0.1)
        M_label = MathTex("M", color=INNER_DOT_COLOR).next_to(
            M, UP, buff=0.2)

        self.play(
            AnimationGroup(DrawBorderThenFill(
                K), Write(K_label), lag_ratio=0.4),
            AnimationGroup(DrawBorderThenFill(
                L), Write(L_label), lag_ratio=0.4),
            AnimationGroup(DrawBorderThenFill(
                M), Write(M_label), lag_ratio=0.4)
        )

        KLM = Polygon(K.get_center(), L.get_center(), M.get_center(
        ), color=INNER_DOT_COLOR, stroke_width=INNER_DOT_STROKE_WIDTH + 1,
            z_index=INNER_DOT_Z_INDEX)

        v1 = DashedLine(
            ORIGIN, 8 * RIGHT,
            color=HEIGHT_COLOR,
            stroke_width=HEIGHT_STROKE_WIDTH,
            z_index=HEIGHT_Z_INDEX
        ).move_to(K.get_center()).shift(RIGHT)
        v1.rotate(AD.get_angle() + PI / 2, about_point=K.get_center())

        v2 = DashedLine(
            ORIGIN, 8 * RIGHT,
            color=HEIGHT_COLOR,
            stroke_width=HEIGHT_STROKE_WIDTH,
            z_index=HEIGHT_Z_INDEX
        ).move_to(L.get_center()).shift(RIGHT)
        v2.rotate(e.get_angle() - PI / 2, about_point=L.get_center())

        v3 = DashedLine(
            ORIGIN, 8 * RIGHT,
            color=HEIGHT_COLOR,
            stroke_width=HEIGHT_STROKE_WIDTH,
            z_index=HEIGHT_Z_INDEX
        ).move_to(M.get_center()).shift(RIGHT)
        v3.rotate(d.get_angle() - PI / 2, about_point=M.get_center())

        self.play(Create(KLM))
        self.play(Create(v1), Create(v2), Create(v3))

        self.next_section("Orthocenter", skip_animations=False)
        self.pause(2)

        V = Dot(line_intersection(v1, v2), color=ORTH_DOT_COLOR,
                radius=ORTH_DOT_RADIUS, stroke_width=ORTH_DOT_STROKE_WIDTH,
                stroke_opacity=ORTH_DOT_STROKE_OPACITY,
                fill_opacity=ORTH_DOT_FILL_OPACITY,
                z_index=ORTH_DOT_Z_INDEX)
        V_label = MathTex("V", color=ORTH_DOT_COLOR).next_to(V, UP, buff=0.1)

        self.play(AnimationGroup(DrawBorderThenFill(
            V), Write(V_label), lag_ratio=0.4))

        T = Dot(BC.get_center(), color=T_COLOR,
                radius=ORTH_DOT_RADIUS, stroke_width=ORTH_DOT_STROKE_WIDTH,
                stroke_opacity=ORTH_DOT_STROKE_OPACITY,
                fill_opacity=0.5,
                z_index=ORTH_DOT_Z_INDEX)
        T_label = MathTex("T", color=T_COLOR).next_to(T, UP + RIGHT, buff=0.1)
        t = Line(A, T.get_center(), color=T_COLOR,
                 stroke_width=T_STROKE_WIDTH, z_index=T_Z_INDEX)

        self.play(AnimationGroup(
            DrawBorderThenFill(T), Write(T_label), Create(t), lag_ratio=0.4)
        )

        self.next_section("Parallelepiped")
        self.pause(2)

        ADTE = Polygon(A, D.get_center(), T.get_center(), E.get_center(),
                       color=PAR_COLOR, stroke_width=PAR_STROKE_WIDTH,
                       z_index=PAR_Z_INDEX)

        self.play(Create(ADTE), run_time=2)

        X = line_intersection(AB, v3)
        Y = line_intersection(AC, v2)

        AYVX = Polygon(A, Y, V.get_center(), X, color=PINK,
                       stroke_width=PAR_STROKE_WIDTH, z_index=PAR_Z_INDEX + 1)

        self.play(Create(AYVX), run_time=2)
=======
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
>>>>>>> d30123628076a7a21cb955a8c888b3a99b42b859

        self.pause(2)

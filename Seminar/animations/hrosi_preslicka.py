import numpy as np
from manim import *

from hrosi_preslicka_config import *


class Vertex:
    def __init__(self, position: np.ndarray) -> None:
        self.position = position
        self.object = self.make()

    def make(self) -> VMobject:
        return Dot(
            color=VERTEX_FILL_COLOR,
            radius=VERTEX_RADIUS,
            fill_opacity=VERTEX_FILL_OPACITY,
            stroke_width=VERTEX_STROKE_WIDTH,
            stroke_color=VERTEX_STROKE_COLOR
        ).move_to(self.position).set_z_index(2)

    def get_create_animation(self) -> Animation:
        return DrawBorderThenFill(self.object)


class Edge:
    def __init__(self, vertex1: Vertex, vertex2: Vertex) -> None:
        self.vertex1 = vertex1
        self.vertex2 = vertex2
        self.object = self.make()

    def make(self) -> VMobject:
        return Line(
            start=self.vertex1.position,
            end=self.vertex2.position,
            color=EDGE_COLOR,
            stroke_width=EDGE_STROKE_WIDTH
        ).set_z_index(0)

    def get_create_animation(self) -> Animation:
        return Create(self.object)


class HrosiPreslicka(Scene):
    def construct(self):
        vertices = [
            Vertex(np.array([0, 3, 0])),
            Vertex(np.array([-2, 1, 0])),
            Vertex(np.array([0, 1, 0])),
            Vertex(np.array([2, 1, 0])),
            Vertex(np.array([-3, -1, 0])),
            Vertex(np.array([-2, -1, 0])),
            Vertex(np.array([-1, -1, 0])),
            Vertex(np.array([0.5, -1, 0])),
            Vertex(np.array([1.5, -1, 0])),
            Vertex(np.array([2.5, -1, 0])),
            Vertex(np.array([3.5, -1, 0])),
            Vertex(np.array([-2.4, -3, 0])),
            Vertex(np.array([-1.6, -3, 0])),
            Vertex(np.array([-1, -3, 0])),
            Vertex(np.array([1.1, -3, 0])),
            Vertex(np.array([1.9, -3, 0])),
            Vertex(np.array([2.5, -3, 0]))
        ]
        edges = [
            Edge(vertices[0], vertices[1]),
            Edge(vertices[0], vertices[2]),
            Edge(vertices[0], vertices[3]),
            Edge(vertices[1], vertices[4]),
            Edge(vertices[1], vertices[5]),
            Edge(vertices[1], vertices[6]),
            Edge(vertices[3], vertices[7]),
            Edge(vertices[3], vertices[8]),
            Edge(vertices[3], vertices[9]),
            Edge(vertices[3], vertices[10]),
            Edge(vertices[5], vertices[11]),
            Edge(vertices[5], vertices[12]),
            Edge(vertices[6], vertices[13]),
            Edge(vertices[8], vertices[14]),
            Edge(vertices[8], vertices[15]),
            Edge(vertices[9], vertices[16])
        ]

        self.play(AnimationGroup(
            vertices[0].get_create_animation(),
            AnimationGroup(
                *[edges[i].get_create_animation() for i in range(3)]
            ),
            AnimationGroup(
                *[vertices[i].get_create_animation() for i in range(1, 4)]
            ),
            AnimationGroup(
                *[edges[i].get_create_animation() for i in range(3, 10)]
            ),
            AnimationGroup(
                *[vertices[i].get_create_animation() for i in range(4, 11)]
            ),
            AnimationGroup(
                *[edges[i].get_create_animation() for i in range(10, 16)]
            ),
            AnimationGroup(
                *[vertices[i].get_create_animation() for i in range(11, 17)]
            ),
            lag_ratio=0.2
        ))

        tree = VGroup(*vertices, *edges)
        self.play(tree.animate.shift(2 * RIGHT))
        self.pause(2)

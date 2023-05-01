from manim import *
import networkx as nx
from random import randint
from itertools import chain

VERTEX_COLOR = YELLOW_C
EDGE_COLOR = PURPLE_A
D_COLOR = BLUE_C
INF_COLOR = RED_C
TABLE_FONT_SIZE = 48

LOOP_INDEX_COLOR = TEAL
START_END_COLOR = RED_C
OLD_PATH_COLOR = GREEN_C


class FloydWarshall(Scene):

    def filter_duplicates(self, edges):
        new_edges = {}
        for edge, edge_obj in edges.items():
            if ((edge[0], edge[1]) not in new_edges
                    and (edge[1], edge[0]) not in new_edges):
                new_edges[(edge[0], edge[1])] = edge_obj

        return new_edges

    def construct(self):
        def show_paths(i, j, old_path, new_path):
            for x in (i, j):
                graph[f"v_{x}"].generate_target()
                graph[f"v_{x}"].target.become(
                    LabeledDot(
                        MathTex(f"v_{x}", color=WHITE), color=START_END_COLOR,
                        radius=0.3
                    ).move_to(graph[f"v_{x}"].get_center())
                )
            self.play(
                MoveToTarget(graph[f"v_{i}"]),
                MoveToTarget(graph[f"v_{j}"])
            )

            if old_path:
                for v in old_path[1:-1]:
                    graph[f"v_{v}"].generate_target()
                    graph[f"v_{v}"].target.become(
                        LabeledDot(
                            MathTex(f"v_{v}", color=WHITE),
                            color=OLD_PATH_COLOR,
                            radius=0.3
                        ).move_to(graph[f"v_{v}"].get_center())
                    )
                self.play(AnimationGroup(*[
                    MoveToTarget(graph[f"v_{v}"])
                    for v in old_path[1:-1]
                ]))

        # Create graph
        nx_graph = nx.graph_atlas(997)
        nx_vertices = [f"v_{i+1}" for i in range(len(nx_graph))]
        nx_graph = nx.relabel_nodes(nx_graph, dict(zip(nx_graph, nx_vertices)))

        graph = Graph.from_networkx(
            nx_graph,
            layout="spring",
            layout_scale=3.5,
            labels=True,
            vertex_config={
                "color": VERTEX_COLOR,
                "radius": 0.3,
            },
            edge_config={
                "color": EDGE_COLOR,
            }
        )

        self.play(Create(graph))
        self.play(graph.animate.shift(RIGHT * 3))

        # Edge weights
        edges = self.filter_duplicates(graph.edges)
        edge_weights = {
            edge: randint(1, 8)
            for edge in edges
        }
        edge_labels = VGroup(*[
            VGroup(
                circle := Circle(
                    radius=0.2, color=EDGE_COLOR,
                    fill_opacity=1
                ).move_to(edge_obj.get_center()),
                MathTex(
                    str(edge_weights[edge]),
                    color=BLACK
                ).move_to(circle.get_center())
            )
            for edge, edge_obj in edges.items()
        ])
        self.play(*[
            DrawBorderThenFill(edge_label[0])
            for edge_label in edge_labels
        ])
        self.play(*[
            Write(edge_label[1])
            for edge_label in edge_labels
        ])

        # Distance table
        D = [
            [99999 for _ in range(len(nx_graph))]
            for _ in range(len(nx_graph))
        ]
        paths = {}
        for i in range(len(nx_graph)):
            D[i][i] = 0
            paths[(i+1, i+1)] = [i+1]
        for edge, weight in edge_weights.items():
            D[nx_vertices.index(edge[0])][nx_vertices.index(edge[1])] = weight
            D[nx_vertices.index(edge[1])][nx_vertices.index(edge[0])] = weight
            paths[(nx_vertices.index(edge[0])+1,
                   nx_vertices.index(edge[1])+1)] = [
                nx_vertices.index(edge[0])+1, nx_vertices.index(edge[1])+1
            ]
            paths[(nx_vertices.index(edge[1])+1,
                   nx_vertices.index(edge[0])+1)] = [
                nx_vertices.index(edge[1])+1, nx_vertices.index(edge[0])+1
            ]

        first_row = [VMobject()] + [
            MathTex(f"v_{i+1}", color=VERTEX_COLOR, font_size=TABLE_FONT_SIZE)
            for i in range(len(nx_graph))
        ]
        other_rows = [
            [MathTex(f"v_{i+1}", color=VERTEX_COLOR,
                     font_size=TABLE_FONT_SIZE)] + [
                MathTex(D[i][j], color=D_COLOR, font_size=TABLE_FONT_SIZE)
                if D[i][j] != 99999 else MathTex(r"\infty", color=INF_COLOR,
                                                 font_size=TABLE_FONT_SIZE)
                for j in range(len(nx_graph))
            ]
            for i in range(len(nx_graph))
        ]

        distance_table = VGroup(
            *first_row,
            *chain.from_iterable(other_rows)
        ).arrange_in_grid(len(nx_graph) + 1, len(nx_graph) + 1, buff=0.25
                          ).to_corner(UL)

        self.play(Write(distance_table))

        # lines
        vertical_lines = VGroup(*[
            Line(distance_table[i % len(nx_graph) + 1].get_center() +
                 UP * 0.25 + LEFT * 0.35,
                 distance_table[-len(nx_graph) + i].get_center() + DOWN * 0.25 +
                 LEFT * 0.35,
                 color=VERTEX_COLOR,
                 stroke_width=1)
            for i in range(len(nx_graph))
        ])
        horizontal_lines = VGroup(*[
            Line(distance_table[(i + 1) * (len(nx_graph) + 1)].get_center() +
                 UP * 0.3 + LEFT * 0.25,
                 distance_table[(i + 1) * (len(nx_graph) + 1) +
                                len(nx_graph)].get_center() +
                 UP * 0.3 + RIGHT * 0.25,
                 color=VERTEX_COLOR,
                 stroke_width=1)
            for i in range(len(nx_graph))
        ])
        self.play(Create(vertical_lines), Create(horizontal_lines))

        # Nope
        self.wait()
        rect = Rectangle(
            width=4,
            height=2,
            color=RED,
            fill_color=YELLOW,
            fill_opacity=1
        ).move_to(ORIGIN)
        text = Text("NE!", color=RED).scale(2).move_to(ORIGIN)

        self.play(AnimationGroup(
            DrawBorderThenFill(rect),
            Write(text),
            lag_ratio=0.5
        ))
        self.wait()
        self.play(FadeOut(rect), FadeOut(text))

        self.play(*[
            Uncreate(vertical_lines[i])
            for i in range(1, len(nx_graph))
        ], *[
            Uncreate(horizontal_lines[i])
            for i in range(1, len(nx_graph))
        ])

        # Algorithm
        k_label = VGroup(
            MathTex("k =", color=LOOP_INDEX_COLOR),
            MathTex("1", color=LOOP_INDEX_COLOR)
        ).arrange(RIGHT)
        i_label = VGroup(
            MathTex("i =", color=LOOP_INDEX_COLOR),
            MathTex("1", color=LOOP_INDEX_COLOR)
        ).arrange(RIGHT)
        j_label = VGroup(
            MathTex("j =", color=LOOP_INDEX_COLOR),
            MathTex("1", color=LOOP_INDEX_COLOR)
        ).arrange(RIGHT)

        index_labels = VGroup(k_label, i_label, j_label).arrange(
            DOWN, buff=0.25).to_corner(DL)

        self.play(Write(index_labels))

        square = Square(0.5, color=LOOP_INDEX_COLOR).move_to(
            distance_table[len(nx_graph) + 2].get_center()
        )
        self.play(Create(square))

        for k in range(1, len(nx_graph) + 1):
            self.play(k_label[1].animate.become(
                MathTex(str(k), color=LOOP_INDEX_COLOR
                        ).next_to(k_label[0], RIGHT)
            ), i_label[1].animate.become(
                MathTex(str(1), color=LOOP_INDEX_COLOR
                        ).next_to(i_label[0], RIGHT)
            ))
            for i in range(1, 3):
                animation = [j_label[1].animate.become(
                    MathTex("1", color=LOOP_INDEX_COLOR).next_to(
                        j_label[0], RIGHT)
                )]
                if i != 1:
                    animation.append(i_label[1].animate.become(
                        MathTex(str(i), color=LOOP_INDEX_COLOR
                                ).next_to(i_label[0], RIGHT)
                    ))

                if (i, k) != (1, 1):
                    square2 = Square(0.5, color=LOOP_INDEX_COLOR).move_to(
                        distance_table[
                            i * (len(nx_graph) + 1) + 1
                        ].get_center()
                    )
                    animation += [
                        Create(square2),
                        Uncreate(square)
                    ]
                    square = square2

                self.play(*animation)

                for j in range(1, 3):
                    old_path = paths.get((i, j), [])
                    if D[i-1][j-1] > D[i-1][k-1] + D[k-1][j-1]:
                        D[i-1][j-1] = D[i-1][k-1] + D[k-1][j-1]
                        paths[(i, j)] = (paths.get((i, k), [])[:-1] +
                                         paths.get((k, j), []))
                    new_path = paths.get((i, j), [])
                    if j != 1:
                        square_animation = []
                        square_animation.append(
                            j_label[1].animate.become(
                                MathTex(str(j), color=LOOP_INDEX_COLOR
                                        ).next_to(j_label[0], RIGHT)
                            )
                        )
                        square2 = Square(0.5, color=LOOP_INDEX_COLOR).move_to(
                            distance_table[
                                i * (len(nx_graph) + 1) + j
                            ].get_center()
                        )
                        square_animation += [
                            Create(square2),
                            Uncreate(square)
                        ]
                        square = square2
                        self.play(*square_animation)

                    show_paths(i, j, old_path, new_path)
        self.wait()

from manim import *
import networkx as nx
from random import randint

from graphs_config import *


class UndirectedGraphExample(Scene):
    def construct(self):
        G = Graph.from_networkx(nx.petersen_graph(),
                                vertex_config={"color": VERTEX_COLOR,
                                               "radius": 0.1},
                                edge_config={"color": EDGE_COLOR},
                                layout="random")

        self.play(Create(G), run_time=2)
        self.wait(1)

        # peterson circular
        self.play(G.animate.change_layout("circular"), run_time=2)
        self.wait(1)

        # peterson hexagons
        small_triangle = RegularPolygon(3, radius=1.5)
        big_hexagon = RegularPolygon(6, radius=3)

        layout = {
            0: small_triangle.get_vertices()[0],
            1: big_hexagon.get_vertices()[0],
            2: big_hexagon.get_vertices()[5],
            3: big_hexagon.get_vertices()[4],
            4: big_hexagon.get_vertices()[3],
            5: ORIGIN,
            6: big_hexagon.get_vertices()[1],
            7: small_triangle.get_vertices()[1],
            8: small_triangle.get_vertices()[2],
            9: big_hexagon.get_vertices()[2]
        }
        self.play(G.animate.change_layout(layout), run_time=2)
        self.wait(1)

        # peterson nonagon
        nonagon = RegularPolygon(9, radius=3)
        layout = {
            0: nonagon.get_vertices()[0],
            1: nonagon.get_vertices()[8],
            2: nonagon.get_vertices()[4],
            3: nonagon.get_vertices()[5],
            4: nonagon.get_vertices()[1],
            5: ORIGIN,
            6: nonagon.get_vertices()[7],
            7: nonagon.get_vertices()[3],
            8: nonagon.get_vertices()[6],
            9: nonagon.get_vertices()[2]
        }
        self.play(G.animate.change_layout(layout), run_time=2)
        self.wait(1)

        # peterson normal
        small_pentagon = RegularPolygon(5, radius=1.5)
        big_pentagon = RegularPolygon(5, radius=3)

        G.generate_target()
        for v in range(5):
            G.target[v].move_to(big_pentagon.get_vertices()[v])
        for v in range(5, 10):
            G.target[v].move_to(small_pentagon.get_vertices()[v - 5])
        self.play(MoveToTarget(G), run_time=2)

        self.wait(1)

        # cubic graph
        self.play(FadeOut(G))

        G = Graph.from_networkx(nx.cubical_graph(),
                                vertex_config={"color": VERTEX_COLOR,
                                               "radius": 0.25},
                                edge_config={"color": EDGE_COLOR},
                                layout="random", layout_scale=4,
                                labels=True)

        self.play(Create(G), run_time=2)
        self.wait(1)

        # cubic graph hexagon
        hexagon = RegularPolygon(6, radius=3)
        layout = {
            0: [-1.5, 0, 0],
            1: [1.5, 0, 0],
            2: hexagon.get_vertices()[0],
            3: hexagon.get_vertices()[1],
            4: hexagon.get_vertices()[2],
            5: hexagon.get_vertices()[3],
            6: hexagon.get_vertices()[4],
            7: hexagon.get_vertices()[5]
        }
        self.play(G.animate.change_layout(layout), run_time=2)
        self.wait(1)

        # cubic graph circle
        self.play(G.animate.change_layout("circular"), run_time=2)
        self.wait(1)

        # cubic graph squares
        small_square = Square(1.5)
        big_square = Square(3)

        layout = {
            0: small_square.get_vertices()[0],
            1: small_square.get_vertices()[3],
            2: small_square.get_vertices()[2],
            3: small_square.get_vertices()[1],
            4: big_square.get_vertices()[0],
            5: big_square.get_vertices()[1],
            6: big_square.get_vertices()[2],
            7: big_square.get_vertices()[3]
        }
        self.play(G.animate.change_layout(layout), run_time=2)
        self.wait(1)

        # cubic graph original
        cube_layout = {
            0: [2, 2, 0],
            1: [2, 0, 0],
            2: [0, 0, 0],
            3: [0, 2, 0],
            4: [1, 1, 0],
            5: [-1, 1, 0],
            6: [-1, -1, 0],
            7: [1, -1, 0]
        }
        self.play(G.animate.change_layout(cube_layout), run_time=2)

        self.wait(2)

        self.play(
            G.animate.remove_edges((0, 4), (1, 7), (2, 6), (3, 5))
        )
        self.play(
            *[G[v].animate.shift(DOWN + RIGHT) for v in range(4)],
            *[G[v].animate.shift(2 * LEFT) for v in range(4, 8)]
        )

        self.wait(2)


class TreeExamples(Scene):
    def construct(self):
        # tree
        tree = nx.balanced_tree(2, 3)
        G = Graph.from_networkx(tree, layout="tree",
                                layout_scale=3,
                                root_vertex=0,
                                vertex_config={"color": VERTEX_COLOR,
                                               "radius": 0.1},
                                edge_config={"color": EDGE_COLOR})

        self.play(Create(G), run_time=2)
        self.wait(1)

        # tree random
        self.play(G.animate.change_layout(
            "random", layout_scale=3), run_time=2)
        self.wait(1)

        # tree circular
        self.play(G.animate.change_layout(
            "circular", layout_scale=3), run_time=2)
        self.wait(1)

        # tree kamada_kawai
        self.play(G.animate.change_layout(
            "kamada_kawai", layout_scale=3), run_time=2)
        self.wait(1)

        # tree normal
        self.play(G.animate.change_layout(
            "tree", root_vertex=13, layout_scale=3), run_time=2)
        self.wait(2)


class PathAndCycleExamples(Scene):
    def construct(self):
        G = Graph.from_networkx(nx.circular_ladder_graph(5),
                                vertex_config={"color": VERTEX_COLOR,
                                               "radius": 0.15},
                                edge_config={"color": EDGE_COLOR},
                                layout="circular", layout_scale=3.5,
                                labels=False)

        for v in G.vertices.values():
            v.set_z_index(10)
        for e in G.edges.values():
            e.set_z_index(5)

        self.play(Create(G), run_time=2)
        self.wait(2)

        # walk example
        walk_vertices = [0, 1, 6, 7, 2, 1, 0, 4]
        dot = Dot(radius=0.2, color=PATH_COLOR).set_z_index(12)
        dot.move_to(G[walk_vertices[0]].get_center())

        self.play(Create(dot))
        dot_trace_1 = TracedPath(dot.get_center, stroke_width=4,
                                 stroke_color=PATH_COLOR).set_z_index(7)
        dot_trace_2 = TracedPath(dot.get_center, stroke_width=4,
                                 stroke_color=PATH_COLOR_TWICE).set_z_index(8)
        dot_trace_3 = TracedPath(dot.get_center, stroke_width=4,
                                 stroke_color=PATH_COLOR).set_z_index(9)
        self.add(dot_trace_1)
        for i, v in enumerate(walk_vertices):
            self.play(dot.animate.move_to(G[v].get_center()))
            G[v].set_color(PATH_COLOR)
            if i in [5, 6]:
                G[v].set_color(PATH_COLOR_TWICE)
            if i == 5:
                self.add(dot_trace_2)
                self.play(dot.animate.set_color(PATH_COLOR_TWICE))
            if i == 6:
                self.add(dot_trace_3)
                self.play(dot.animate.set_color(PATH_COLOR))

        self.wait(2)

        # trail example
        self.play(
            FadeOut(dot_trace_1, dot_trace_2, dot_trace_3, dot),
            *[v.animate.set_color(VERTEX_COLOR)
              for v in G.vertices.values()]
        )

        trail_vertices = [2, 7, 6, 1, 2, 3, 4]
        dot.move_to(G[trail_vertices[0]].get_center())
        self.play(Create(dot))

        dot_trace = TracedPath(dot.get_center, stroke_width=4,
                               stroke_color=PATH_COLOR).set_z_index(7)
        self.add(dot_trace)

        for i, v in enumerate(trail_vertices):
            self.play(dot.animate.move_to(G[v].get_center()))
            G[v].set_color(PATH_COLOR)
            if i == 4:
                G[v].set_color(PATH_COLOR_TWICE)

        self.wait(2)

        # path example
        self.play(
            FadeOut(dot_trace, dot),
            *[v.animate.set_color(VERTEX_COLOR)
              for v in G.vertices.values()]
        )

        path_vertices = [0, 5, 6, 7, 2, 3, 4]

        dot.move_to(G[path_vertices[0]].get_center())
        self.play(Create(dot))

        dot_trace = TracedPath(dot.get_center, stroke_width=4,
                               stroke_color=PATH_COLOR).set_z_index(7)
        self.add(dot_trace)

        for v in path_vertices:
            self.play(dot.animate.move_to(G[v].get_center()))
            G[v].set_color(PATH_COLOR)

        self.wait(2)

        # cycle example
        self.play(dot.animate.move_to(G[0].get_center()))

        self.wait(2)


class SpanningTreeExample(Scene):
    def construct(self):
        grid_layout = {
            (0, 0): [-3, -3, 0],
            (0, 1): [-1, -3, 0],
            (0, 2): [1, -3, 0],
            (0, 3): [3, -3, 0],
            (1, 0): [-3, -1, 0],
            (1, 1): [-1, -1, 0],
            (1, 2): [1, -1, 0],
            (1, 3): [3, -1, 0],
            (2, 0): [-3, 1, 0],
            (2, 1): [-1, 1, 0],
            (2, 2): [1, 1, 0],
            (2, 3): [3, 1, 0],
            (3, 0): [-3, 3, 0],
            (3, 1): [-1, 3, 0],
            (3, 2): [1, 3, 0],
            (3, 3): [3, 3, 0]
        }

        nx_graph = nx.grid_2d_graph(4, 4)
        edge_weights = {
            edge: randint(1, 9)
            for edge in nx_graph.edges
        }
        for e in edge_weights:
            nx_graph[e[0]][e[1]]["weight"] = edge_weights[e]

        G = Graph.from_networkx(nx_graph,
                                vertex_config={"color": VERTEX_COLOR,
                                               "radius": 0.15},
                                edge_config={"color": EDGE_COLOR},
                                layout=grid_layout,
                                labels=False)
        print(G.edges)

        weight_labels = VGroup()
        weight_labels_dict = {}
        for edge, weight in edge_weights.items():
            label = MathTex(str(weight), color=WHITE).scale(0.8)
            if edge[0][0] == edge[1][0]:
                label.next_to(G.edges[edge], UP, buff=0.15)
            else:
                label.next_to(G.edges[edge], RIGHT, buff=0.15)
            weight_labels.add(label)
            weight_labels_dict[edge] = label

        for v in G.vertices.values():
            v.set_z_index(10)
        for e in G.edges.values():
            e.set_z_index(5)

        self.play(Create(G), run_time=2)
        self.wait(1)

        self.play(Write(weight_labels), run_time=2)
        self.wait(2)

        spanning_tree = nx.minimum_spanning_tree(nx_graph)
        for e in sorted(spanning_tree.edges, key=lambda x: edge_weights[x]):
            line = Line(G[e[0]].get_center(), G[e[1]].get_center(),
                        stroke_width=15, stroke_color=SPANNING_TREE_COLOR,
                        z_index=7)
            self.play(Create(line),weight_labels_dict[e].animate.
                      set_color(SPANNING_TREE_COLOR).scale(1.2))

        self.wait(2)

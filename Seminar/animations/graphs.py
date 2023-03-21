from manim import *
import networkx as nx

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
        self.wait(1)

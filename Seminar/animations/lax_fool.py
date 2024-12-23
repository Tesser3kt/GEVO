from lzma import FILTER_LZMA1
from pathlib import Path
from typing import Tuple
import numpy as np
from manim import *

# defaults
GRID_COLOR_MAIN = WHITE
GRID_COLOR_AUX = TEAL
GRID_OPACITY = 0.8

GRID_STEP = 0.4

ANGEL_COLOR = YELLOW
ANGEL_STROKE_WIDTH = 1.5
ANGEL_INITIAL_POS = 0, -8
ANGEL_SCALE_FACTOR = 0.07

DEVIL_COLOR = RED

LIMIT_COLORS = [
    ORANGE,
    PINK,
    GREEN,
    BLUE,
    PURPLE
]

GAME_SPEED = 0.5


class LaxFool(Scene):
    def create_grid(self) -> None:
        # create axes
        axes = {
            'x': Line(
                start=np.array([-10, 0, 0]),
                end=np.array([10, 0, 0]),
                color=GRID_COLOR_MAIN,
                stroke_width=1,
                stroke_opacity=1
            ),
            'y': Line(
                start=np.array([0, 10, 0]),
                end=np.array([0, -10, 0]),
                color=GRID_COLOR_MAIN,
                stroke_width=1,
                stroke_opacity=1
            )
        }

        # create grid lines
        aux_lines = {
            'ver': [
                Line(
                    start=np.array([x, 10, 0]),
                    end=np.array([x, -10, 0]),
                    color=GRID_COLOR_AUX,
                    stroke_width=1,
                    stroke_opacity=GRID_OPACITY
                ) for x in np.arange(-10, 10, GRID_STEP)
            ],
            'hor': [
                Line(
                    start=np.array([-10, y, 0]),
                    end=np.array([10, y, 0]),
                    color=GRID_COLOR_AUX,
                    stroke_width=1,
                    stroke_opacity=GRID_OPACITY
                ) for y in np.arange(10, -10, -GRID_STEP)
            ]
        }

        # play creation
        self.play(Create(axes['x']), Create(axes['y']))
        self.play(
            AnimationGroup(
                *[Create(line) for line in aux_lines['ver']],
                lag_ratio=0.03
            ),
            AnimationGroup(
                *[Create(line) for line in aux_lines['hor']],
                lag_ratio=0.03
            )
        )

    def create_angel(self) -> VGroup:
        # create head and body
        head = Circle(0.5, ANGEL_COLOR, stroke_width=ANGEL_STROKE_WIDTH,
                      fill_color=ANGEL_COLOR, fill_opacity=1)
        body = Polygon(*[
            np.array([0, 0.5, 0]),
            np.array([1, -2, 0]),
            np.array([-1, -2, 0])
        ], color=ANGEL_COLOR, stroke_width=ANGEL_STROKE_WIDTH,
            fill_color=ANGEL_COLOR, fill_opacity=1)
        body.next_to(head, 0.25 * DOWN)
        wings = [
            Polygon(*[
                np.array([0.5, 0, 0]),
                np.array([1.25, 0.75, 0]),
                np.array([2.5, 0, 0])
            ], color=ANGEL_COLOR, stroke_width=ANGEL_STROKE_WIDTH,
                fill_color=ANGEL_COLOR, fill_opacity=1),
            Polygon(*[
                np.array([-0.5, 0, 0]),
                np.array([-1.25, 0.75, 0]),
                np.array([-2.5, 0, 0])
            ], color=ANGEL_COLOR, stroke_width=ANGEL_STROKE_WIDTH,
                fill_color=ANGEL_COLOR, fill_opacity=1)
        ]
        wings[0].move_to(np.array([1.35, -1, 0]))
        wings[1].move_to(np.array([-1.35, -1, 0]))

        halo = Ellipse(1.2, 0.5, color=ANGEL_COLOR,
                       stroke_width=ANGEL_STROKE_WIDTH)
        halo.move_to(np.array([0, 0.6, 0]))

        return VGroup(head, body, *wings, halo)

    def devil_eat_field(self, *field: Tuple[int, int]) -> None:
        square = Square(GRID_STEP, color=DEVIL_COLOR,
                        stroke_width=1, fill_color=DEVIL_COLOR, fill_opacity=1,
                        z_index=-999)
        square.move_to(np.array([(field[0] - 0.5) * GRID_STEP,
                                 (field[1] - 0.5) * GRID_STEP, 0]))
        self.play(DrawBorderThenFill(square, run_time=GAME_SPEED))

    def angel_move_to(self, angel: VGroup, *field: Tuple[int, int]) -> None:
        self.play(angel.animate(run_time=GAME_SPEED).
                  move_to(np.array([(field[0] - 0.5) * GRID_STEP,
                          (field[1] - 0.5) *
                          GRID_STEP,
                          0])))

    def play_game(self, angel: VGroup, angel_moves: list,
                  devil_moves: list) -> None:
        for i, _ in enumerate(devil_moves):
            self.devil_eat_field(*devil_moves[i])
            self.angel_move_to(angel, *angel_moves[i])

    def show_limit(self, *angel_pos: Tuple[int, int], color: str) -> None:
        limits = [
            Line(
                np.array([(angel_pos[0] - 0.5) * GRID_STEP,
                         (angel_pos[1] - 1.5) * GRID_STEP, 0]),
                np.array([(angel_pos[0] - 101) * GRID_STEP,
                          (angel_pos[1] + 99) * GRID_STEP, 0]),
                stroke_width=2,
                stroke_opacity=1,
                color=color
            ),
            Line(
                np.array([(angel_pos[0] - 0.5) * GRID_STEP,
                         (angel_pos[1] - 1.5) * GRID_STEP, 0]),
                np.array([(angel_pos[0] + 100) * GRID_STEP,
                          (angel_pos[1] + 99) * GRID_STEP, 0]),
                stroke_width=2,
                stroke_opacity=1,
                color=color
            )
        ]
        self.play(Create(limits[0]), Create(limits[1]))

    def get_bouncing_path(self, ceil: np.ndarray,
                          floor: np.ndarray) -> VMobject:
        curve = CubicBezier(
            ceil,
            ceil + 1.5 * LEFT,
            floor + UP,
            floor
        )
        arc1 = ArcBetweenPoints(
            curve.get_end(),
            curve.get_end() + 1.5 * LEFT,
            0.7 * PI
        )
        arc2 = ArcBetweenPoints(
            arc1.get_end(),
            arc1.get_end() + 0.75 * LEFT,
            0.7 * PI
        )
        arc3 = ArcBetweenPoints(
            arc2.get_end(),
            arc2.get_end() + 0.33 * LEFT,
            0.7 * PI
        )

        curves = VGroup(curve, arc1, arc2, arc3)
        path = VMobject()
        path.points = curves.get_all_points()

        return path

    def construct(self) -> None:
        self.create_grid()
        angel = self.create_angel()
        self.play(DrawBorderThenFill(angel))
        self.play(angel.animate.move_to(np.array([
            (ANGEL_INITIAL_POS[0] - 0.5) * GRID_STEP,
            (ANGEL_INITIAL_POS[1] - 0.5) * GRID_STEP,
            0])).scale(ANGEL_SCALE_FACTOR))
        self.show_limit(*ANGEL_INITIAL_POS, color=LIMIT_COLORS[0])

        # first set of moves
        angel_moves = [
            (1, -7),
            (1, -6),
            (2, -5),
            (2, -4),
            (1, -3),
            (1, -2),
            (0, -1),
            (0, 0)
        ]
        devil_moves = [
            (17, 9),
            (12, 9),
            (7, 9),
            (2, 9),
            (-3, 9),
            (-8, 9),
            (-13, 9),
            (11, 9)
        ]
        self.play_game(angel, angel_moves, devil_moves)
        self.show_limit(0, 0, color=LIMIT_COLORS[1])
        self.pause(GAME_SPEED * 2)

        # second set of moves
        angel_moves = [
            (-1, 1),
            (-1, 2),
            (-2, 3),
            (-2, 4)
        ]

        devil_moves = [
            (6, 9),
            (1, 9),
            (-4, 9),
            (-9, 9)
        ]
        self.play_game(angel, angel_moves, devil_moves)
        self.show_limit(-2, 4, color=LIMIT_COLORS[2])
        self.pause(GAME_SPEED * 2)

        # third set of moves
        angel_moves = [
            (-1, 5),
            (-1, 6)
        ]

        devil_moves = [
            (0, 9),
            (-5, 9)
        ]
        self.play_game(angel, angel_moves, devil_moves)
        self.show_limit(-1, 6, color=LIMIT_COLORS[3])
        self.pause(GAME_SPEED * 2)

        angel_moves = [
            (-2, 7)
        ]
        devil_moves = [
            (-1, 9)
        ]
        self.play_game(angel, angel_moves, devil_moves)
        self.show_limit(-2, 7, color=LIMIT_COLORS[4])
        self.pause(GAME_SPEED * 2)

        angel_moves = [
            (-2, 8)
        ]
        devil_moves = [
            (-2, 9)
        ]
        self.play_game(angel, angel_moves, devil_moves)
        self.pause(GAME_SPEED * 2)

        angel.set_z_index(9999)
        self.play(angel.animate.move_to(ORIGIN).scale(1 / ANGEL_SCALE_FACTOR))
        head, body, wing1, wing2, halo = tuple(angel.submobjects)
        path = self.get_bouncing_path(
            head.get_center(), head.get_center() + 2.5 * DOWN + 2 * LEFT)
        # self.add(path)
        self.play(MoveAlongPath(head, path, run_time=2),
                  wing1.animate.rotate(
                      angle=-0.3*PI, about_point=wing1.get_left()),
                  wing2.animate.rotate(
                      angle=0.3*PI, about_point=wing2.get_right()),
                  FadeOut(halo))
        self.pause(1)

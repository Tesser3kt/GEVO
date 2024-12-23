from typing import Tuple
import numpy as np
from manim import *

# defaults
GRID_COLOR_MAIN = WHITE
GRID_COLOR_AUX = TEAL
GRID_OPACITY = 0.8

GRID_STEP = 1

ANGEL_COLOR = YELLOW
ANGEL_STROKE_WIDTH = 1.5
ANGEL_INITIAL_POS = -2, -2
ANGEL_SCALE_FACTOR = 0.17

DEVIL_COLOR = RED


class AngelsAndDevils(Scene):
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
        self.play(DrawBorderThenFill(square))

    def angel_move_to(self, angel: VGroup, *field: Tuple[int, int]) -> None:
        self.play(angel.animate.move_to(np.array([(field[0] - 0.5) * GRID_STEP,
                                                  (field[1] - 0.5) * GRID_STEP,
                                                  0])))

    def play_game(self, angel: VGroup, angel_moves: list,
                  devil_moves: list) -> None:
        for i, _ in enumerate(devil_moves):
            self.devil_eat_field(*devil_moves[i])
            self.angel_move_to(angel, *angel_moves[i])

    def construct(self) -> None:
        self.create_grid()
        angel = self.create_angel()
        self.play(DrawBorderThenFill(angel))
        self.play(angel.animate.move_to(np.array([
            ANGEL_INITIAL_POS[0] - 0.5 * GRID_STEP,
            ANGEL_INITIAL_POS[1] - 0.5 * GRID_STEP,
            0])).scale(ANGEL_SCALE_FACTOR))

        angel_moves = [
            (-2, -1),
            (-3, 0),
            (-3, 1),
            (-2, 1),
            (-1, 2)
        ]
        devil_moves = [
            (-2, -3),
            (-2, 0),
            (-4, 1),
            (-3, 2),
            (-1, 1)
        ]
        self.play_game(angel, angel_moves, devil_moves)
        self.pause(1)

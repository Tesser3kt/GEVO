from enum import Enum
from PIL import Image, ImageDraw
from random import randint

WIDTH = 60
HEIGHT = 50
BG = 0, 0, 0
PROB_DECREASE = 5


class Direction(Enum):
    """ Enum for directions."""
    UP = (0, -1)
    DOWN = (0, 1)
    LEFT = (-1, 0)
    RIGHT = (1, 0)


# create new 60x50 black canvas
level_img = Image.new('RGB', (WIDTH, HEIGHT), BG)

# create a draw object
draw = ImageDraw.Draw(level_img)

# create probability dict (actual numbers are irrelevant for now)
probs = {
    Direction.UP: 25,
    Direction.DOWN: 25,
    Direction.LEFT: 25,
    Direction.RIGHT: 25
}

# choose a random starting point on the rim
side = randint(0, 1)  # north/south or east/west
if side:
    x = randint(0, WIDTH - 1)
    y = 0 if randint(0, 1) else HEIGHT - 1
else:
    x = 0 if randint(0, 1) else WIDTH - 1
    y = randint(0, HEIGHT - 1)


# set probs to always go away from the rim
direction = -x // abs(x), -y // abs(y)

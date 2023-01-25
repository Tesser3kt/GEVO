from enum import Enum
from PIL import Image, ImageDraw
from random import randint, choice

WIDTH = 60
HEIGHT = 50
BG_COLOR = 0, 0, 0
DEFAULT_CHANCE = 10000
PROB_DECREASE = 100
POINT_COLOR = 255, 255, 0
STABLE_MOVES = 0


class Direction(Enum):
    """ Enum for directions."""
    UP = (0, -1)
    DOWN = (0, 1)
    LEFT = (-1, 0)
    RIGHT = (1, 0)


def draw_point(x: int, y: int, color: tuple[int]) -> None:
    """ Draw a single point on the canvas as a 1x1 rectangle. """
    draw.rectangle((x, y, x, y), fill=color)


def distance(x1: int, y1: int, x2: int, y2: int) -> float:
    """ Calculate the Manhattan distance between two points. """
    return abs(x1 - x2) + abs(y1 - y2)


def can_move(x: int, y: int, direction: Direction) -> bool:
    """ Check if it's possible to move in the given direction. """
    return (0 <= x + direction.value[0] < WIDTH and
            0 <= y + direction.value[1] < HEIGHT)


def random_direction(probs: dict) -> Direction:
    """ Choose a random direction. """
    return choice([
        *(Direction.UP for _ in range(probs[Direction.UP.value])),
        *(Direction.DOWN for _ in range(probs[Direction.DOWN.value])),
        *(Direction.LEFT for _ in range(probs[Direction.LEFT.value])),
        *(Direction.RIGHT for _ in range(probs[Direction.RIGHT.value]))
    ])


def reset_direction_probs(probs: dict, direction: Direction) -> None:
    """ Reset direction probabilities so that the given direction has 100 %.
    """
    probs[direction.value] = DEFAULT_CHANCE
    for other_direction in Direction:
        if other_direction != direction:
            probs[other_direction.value] = 0


def alter_probs(probs: dict, direction: Direction,
                pref_dirs: tuple[Direction]) -> None:
    """ Decrease probabilities of moving in the same direction and increase
    probabilities of moving in adjacent directions. """

    probs[direction.value] -= PROB_DECREASE

    if (direction.value[1], direction.value[0]) in pref_dirs:
        probs[(direction.value[1],
               direction.value[0])] += 3 * PROB_DECREASE // 4
        probs[(-direction.value[1],
               -direction.value[0])] += PROB_DECREASE // 4
    else:
        probs[(direction.value[1],
               direction.value[0])] += PROB_DECREASE // 4
        probs[(-direction.value[1],
               -direction.value[0])] += 3 * PROB_DECREASE // 4


# create new 60x50 black canvas
level_img = Image.new('RGB', (WIDTH, HEIGHT), BG_COLOR)

# create a draw object
draw = ImageDraw.Draw(level_img)

# create probability dict (actual numbers are irrelevant for now)
probs = {
    Direction.UP.value: 0,
    Direction.DOWN.value: 0,
    Direction.LEFT.value: 0,
    Direction.RIGHT.value: 0
}

# create a tuple of extremal points
extremal_points = (
    *((0, y) for y in range(HEIGHT)),
    *((WIDTH - 1, y) for y in range(HEIGHT)),
    *((x, 0) for x in range(WIDTH)),
    *((x, HEIGHT - 1) for x in range(WIDTH))
)

# choose a random starting point on the rim
x, y = choice(extremal_points)
starting_point = x, y

# determine directions to move away from the starting point
preferred_directions = []
if x >= WIDTH // 2:
    preferred_directions.append(Direction.LEFT.value)
else:
    preferred_directions.append(Direction.RIGHT.value)

if y >= HEIGHT // 2:
    preferred_directions.append(Direction.UP.value)
else:
    preferred_directions.append(Direction.DOWN.value)

# set probs to always go away from the rim
starting_dir = (Direction.DOWN if y == 0 else Direction.UP if y == HEIGHT - 1
                else Direction.RIGHT if x == 0 else Direction.LEFT)
reset_direction_probs(probs, starting_dir)

# always move to the opposite side so the level is not too short
if x == 0:
    final_points = [(WIDTH - 1, y) for y in range(HEIGHT)]
elif x == WIDTH - 1:
    final_points = [(0, y) for y in range(HEIGHT)]
elif y == 0:
    final_points = [(x, HEIGHT - 1) for x in range(WIDTH)]
else:
    final_points = [(x, 0) for x in range(WIDTH)]

# draw the first point
draw_point(x, y, POINT_COLOR)

# next point is definitely in direction 'starting_dir'
x, y = x + starting_dir.value[0], y + starting_dir.value[1]

# draw until the rim is reached again
last_direction = starting_dir
moves_in_direction = 0

while (x, y) not in final_points:
    # draw the point
    draw_point(x, y, POINT_COLOR)

    # decrease probability of moving in the same direction and increase
    # probability of moving in adjacent directions
    if moves_in_direction > STABLE_MOVES:
        alter_probs(probs, last_direction, preferred_directions)

    # move at least STABLE_MOVES in the same direction
    # then choose a random direction based on the probabilities
    # if not possible to move, keep choosing until it is

    direction = random_direction(probs)
    while not can_move(x, y, direction):
        if probs[direction.value] == DEFAULT_CHANCE:
            alter_probs(probs, direction, preferred_directions)
        direction = random_direction(probs)

    # move in the chosen direction
    x, y = x + direction.value[0], y + direction.value[1]

    # reset direction probabilities if direction changed
    if direction != last_direction:
        reset_direction_probs(probs, direction)
        last_direction = direction
        moves_in_direction = 0
    else:
        moves_in_direction += 1

# draw the last point
draw_point(x, y, POINT_COLOR)

# save the image
level_img.save('level.png')

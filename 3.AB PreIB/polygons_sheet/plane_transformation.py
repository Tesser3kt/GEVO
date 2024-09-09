import numpy as np
from PIL import Image, ImageDraw


def plane_transformation(x, y):
    x_ = (2 * x - y) / 3 + 200
    y_ = (x + 2 * y) / 2 - 100
    return x_, y_


X_LINE_PIXELS = [(x, y) for x in np.arange(0, 600, 0.1) for y in np.arange(20, 581, 40)]
Y_LINE_PIXELS = [(x, y) for y in np.arange(0, 600, 0.1) for x in np.arange(20, 581, 40)]
DOT_PIXELS = [(x, y) for x in np.arange(20, 581, 40) for y in np.arange(20, 581, 40)]
SQUARE_PIXELS = [(x, y) for x in np.arange(220, 381, 0.1) for y in (220, 380)] + [
    (x, y) for x in (220, 380) for y in np.arange(220, 381, 0.1)
]

image = Image.new("RGB", (600, 600), (255, 255, 255))
draw = ImageDraw.Draw(image)

for x, y in X_LINE_PIXELS:
    draw.point((x, y), fill=(100, 100, 100))

for x, y in Y_LINE_PIXELS:
    draw.point((x, y), fill=(100, 100, 100))

for x, y in DOT_PIXELS:
    draw.circle((x, y), radius=2, fill=(0, 0, 0))

for x, y in SQUARE_PIXELS:
    draw.rectangle([x - 2, y - 2, x + 2, y + 2], fill=(0, 107, 107))

image.save("grid.png")

transformed_image = Image.new("RGB", (600, 600), (255, 255, 255))
transformed_draw = ImageDraw.Draw(transformed_image)

for x, y in X_LINE_PIXELS:
    x_, y_ = plane_transformation(x, y)
    transformed_draw.point((x_, y_), fill=(100, 100, 100))

for x, y in Y_LINE_PIXELS:
    x_, y_ = plane_transformation(x, y)
    transformed_draw.point((x_, y_), fill=(100, 100, 100))

for x, y in DOT_PIXELS:
    x_, y_ = plane_transformation(x, y)
    transformed_draw.circle((x_, y_), radius=2, fill=(0, 0, 0))

for x, y in SQUARE_PIXELS:
    x_, y_ = plane_transformation(x, y)
    transformed_draw.rectangle([x_ - 2, y_ - 2, x_ + 2, y_ + 2], fill=(0, 107, 107))

transformed_image.save("transformed_grid.png")

class Config:
    SCREEN_WIDTH = 1000
    SCREEN_HEIGHT = 1000
    TILE_SIZE = 20
    FPS = 5
    GRID_COLOR = 128, 128, 128
    NEIGHBORS = [(1, 0), (1, 1), (0, 1), (-1, 1), (-1, 0), (-1, -1), (0, -1), (1, -1)]
    NEIGHBORS_TO_LIVE = [2, 3]
    NEIGHBORS_TO_SPAWN = 3

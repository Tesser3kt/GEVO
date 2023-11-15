import pygame as pg
from config import Config


class Tile(pg.sprite.Sprite):
    def __init__(self, x, y, width, height, color):
        super().__init__()
        self.image = pg.Surface((width, height))
        self.image.fill(color)
        self.image = self.image.convert()
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

    def change_color(self, color):
        self.image.fill(color)


def draw_grid(screen, color):
    for x in range(0, Config.SCREEN_WIDTH, Config.TILE_SIZE):
        pg.draw.line(screen, color, (x, 0), (x, Config.SCREEN_HEIGHT))
    for y in range(0, Config.SCREEN_HEIGHT, Config.TILE_SIZE):
        pg.draw.line(screen, color, (0, y), (Config.SCREEN_WIDTH, y))


def fill_grid(screen):
    tiles = pg.sprite.RenderUpdates()
    for x in range(0, Config.SCREEN_WIDTH, Config.TILE_SIZE):
        for y in range(0, Config.SCREEN_HEIGHT, Config.TILE_SIZE):
            tile = Tile(x, y, Config.TILE_SIZE, Config.TILE_SIZE, (0, 0, 0))
            tiles.add(tile)
            screen.blit(tile.image, tile.rect)
    return tiles


def run_game(screen, canvas, tiles, tiles_alive):
    done = False
    pause = False
    clock = pg.time.Clock()
    while not done:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                done = True
            elif event.type == pg.KEYDOWN:
                if event.key == pg.K_SPACE:
                    pause = not pause
                elif event.key == pg.K_ESCAPE:
                    done = True
        if pause:
            continue

        rects_to_update = []
        tiles_to_kill = []
        tiles_to_create = []
        for tile in tiles:
            neighbors = 0
            for neighbor in Config.NEIGHBORS:
                neighbor_x = tile.rect.x + neighbor[0] * Config.TILE_SIZE
                neighbor_y = tile.rect.y + neighbor[1] * Config.TILE_SIZE
                for tile2 in tiles_alive:
                    if tile2.rect.x == neighbor_x and tile2.rect.y == neighbor_y:
                        neighbors += 1
            if tile in tiles_alive:
                if neighbors not in Config.NEIGHBORS_TO_LIVE:
                    tiles_to_kill.append(tile)
            else:
                if neighbors == Config.NEIGHBORS_TO_PROCREATE:
                    tiles_to_create.append(tile)

        for tile in tiles_to_kill:
            tile.change_color((0, 0, 0))
            tiles_alive.remove(tile)
            canvas.blit(tile.image, tile.rect)
            rects_to_update.append(tile.rect)
        for tile in tiles_to_create:
            tile.change_color((255, 255, 255))
            tiles_alive.add(tile)
            canvas.blit(tile.image, tile.rect)
            rects_to_update.append(tile.rect)

        draw_grid(canvas, Config.GRID_COLOR)
        screen.blit(canvas, (0, 0))
        clock.tick(Config.FPS)
        pg.display.update(rects_to_update)


def main():
    pg.init()
    screen = pg.display.set_mode((Config.SCREEN_WIDTH, Config.SCREEN_HEIGHT))
    pg.display.set_caption("Game of Life")

    canvas = pg.Surface((Config.SCREEN_WIDTH, Config.SCREEN_HEIGHT))
    canvas = canvas.convert()
    tiles = fill_grid(canvas)
    tiles_alive = pg.sprite.RenderUpdates()
    draw_grid(canvas, Config.GRID_COLOR)
    screen.blit(canvas, (0, 0))
    pg.display.update()
    clock = pg.time.Clock()
    done = False

    while not done:
        rects_to_update = []
        for event in pg.event.get():
            if event.type == pg.QUIT:
                done = True
            elif event.type == pg.MOUSEBUTTONDOWN:
                if event.button == 1:
                    pos = pg.mouse.get_pos()
                    for tile in tiles:
                        if tile.rect.collidepoint(pos):
                            tile.change_color((255, 255, 255))
                            tiles_alive.add(tile)
                            screen.blit(tile.image, tile.rect)
                            rects_to_update.append(tile.rect)
            elif event.type == pg.KEYDOWN:
                if event.key == pg.K_SPACE:
                    done = True
        pg.display.update(rects_to_update)
        clock.tick(Config.FPS)

    run_game(screen, canvas, tiles, tiles_alive)


if __name__ == "__main__":
    main()

from pygame import image, Surface
from img import load_tiles, get_tiles_rect, SIZE
from maze import create_maze


def parse_grid(data):
    return data.strip().split('\n')


def draw_grid(data, tile_img, tiles):
    xs = len(data[0]) * SIZE
    ys = len(data) * SIZE
    img = Surface((xs, ys))
    for y, row in enumerate(data):
        for x, char in enumerate(row):
            rect = get_tiles_rect(x, y)
            img.blit(tile_img,  rect, tiles[char])
    return img


if __name__ == '__main__':
    tile_img, tiles = load_tiles()
    level = create_maze(12, 7)
    level = parse_grid(level)
    maze = draw_grid(level, tile_img, tiles)
    image.save(maze, 'dist/maze.png')

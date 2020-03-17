import pygame
import os
import sys

TILE_POSITIONS = [
    ('#',  0, 0),  # wall
    ('b',  1, 0),  # blue
    ('.',  2, 0),  # dot
    ('>',  3, 0),  # face right
    ('<',  4, 0),  # face left
    ('$',  5, 0),  # monster
    (' ',  0, 1),  # floor
    ('w',  1, 1),  # white
    ('v',  3, 1),  # face down
    ('^',  4, 1),  # face top
    ('o',  5, 1),  # face back
]

SIZE = 32


def get_tiles_rect(x, y):
    return x*SIZE, y*SIZE


def load_tiles():
    '''
    Load tiles from an image file into a dictionary
    Returns a tuple of (image, tile_dict)
    '''
    tiles = {}

    tile_img = pygame.image.load(os.path.join(sys.path[0], '../img/tiles.xpm'))
    for symbol, x, y in TILE_POSITIONS:
        tiles[symbol] = pygame.Rect(x*SIZE, y*SIZE, SIZE, SIZE)
    return tile_img, tiles


if __name__ == '__main__':
    tile_img, tiles = load_tiles()

    m = pygame.Surface(get_tiles_rect(4, 1))
    m.blit(tile_img,  get_tiles_rect(0, 0), tiles['#'])
    m.blit(tile_img,  get_tiles_rect(1, 0), tiles[' '])
    m.blit(tile_img,  get_tiles_rect(2, 0), tiles['>'])
    m.blit(tile_img,  get_tiles_rect(3, 0), tiles['.'])

    pygame.image.save(m, '../dist/tile_combo.png')

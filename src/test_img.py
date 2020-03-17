import pytest
import random
from img import *


def test_get_tiles_rect():
    size = 32
    for _ in range(20):
        x = random.randint(1, 1000)
        y = random.randint(1, 1000)
        assert ((x*size, y*size) == get_tiles_rect(x, y))


def test_load_tiles():
    _, tiles = load_tiles()
    assert (len(TILE_POSITIONS) == len(tiles))
    for s, x, y in TILE_POSITIONS:
        res = tiles.get(s, None)
        assert(res != None)


if __name__ == '__main__':
    pytest.main()

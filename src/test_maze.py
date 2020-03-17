import pytest
import random
import math
from maze import *


def test_create_grid_string():
    testcases = [
        {
            "x": 5,
            "y": 5,
            "dots": {
                (1, 1), (1, 2), (1, 3),
                (2, 2),
                (3, 1), (3, 2), (3, 3),
            },
            "want": "#####\n#.#.#\n#...#\n#.#.#\n#####\n",
        }
    ]
    for testcase in testcases:
        assert (testcase["want"] == create_grid_string(
                testcase["dots"], testcase["x"], testcase["y"]))


def test_get_all_dot_positions():
    testcases = [
        {
            "x": 1,
            "y": 1,
            "want": [],
        },
        {
            "x": 2,
            "y": 2,
            "want": [],
        },
        {
            "x": 3,
            "y": 3,
            "want": [(1, 1)],
        },
        {
            "x": 3,
            "y": 4,
            "want": [(1, 1), (1, 2)],
        }
    ]
    for testcase in testcases:
        assert (set(testcase["want"]) == set(get_all_dot_positions(
            testcase["x"], testcase["y"])))


def test_get_neighbors():
    testcases = [
        {
            "x": 1,
            "y": 1,
            "want": [
                (0, 0), (0, 1), (0, 2),
                (1, 0), (1, 2),
                (2, 0), (2, 1), (2, 2),
            ],
        },
        {
            "x": 5,
            "y": 5,
            "want": [
                (4, 4), (4, 5), (4, 6),
                (5, 4), (5, 6),
                (6, 4), (6, 5), (6, 6),
            ],
        },
    ]
    for testcase in testcases:
        assert (set(testcase["want"]) == set(get_neighbors(
            testcase["x"], testcase["y"])))
    for _ in range(50):
        x = random.randint(1, 1000)
        y = random.randint(1, 1000)
        neighbors = get_neighbors(x, y)
        assert(8 == len(neighbors))
        for xx, yy in neighbors:
            dx = math.fabs(x - xx)
            dy = math.fabs(y-yy)
            assert(dx != 0 or dy != 0)
            assert(dx <= 1 and dx >= 0)
            assert(dy <= 1 and dy >= 0)


def test_generate_dot_positions():
    X = 20
    Y = 20
    for _ in range(10):
        x = random.randint(3, X)
        y = random.randint(3, Y)
        dots = generate_dot_positions(x, y)

        total = 0
        for xx, yy in dots:
            count = 0
            for tx, ty in get_neighbors(xx, yy):
                count += 1 if (tx, ty) in dots else 0
            total += 1 if count > 5 else 0
        assert(total <= len(dots)/2)


def test_create_maze():
    X = 20
    Y = 20
    for _ in range(20):
        x = random.randint(3, X)
        y = random.randint(3, Y)
        m_str = create_maze(x, y)
        m = m_str.split('\n')
        print(m_str)
        vis = set()

        def dfs(tx, ty):
            vis.add((tx, ty))
            neighbors = get_neighbors(tx, ty)
            for xx, yy in neighbors:
                if (xx >= 0 and xx < x and
                    yy >= 0 and yy < y and
                        m[yy][xx] == '.' and (xx, yy) not in vis):
                    dfs(xx, yy)
        dfs(1, 1)
        assert((x-2) * (y-2) <= 2 * len(vis))


if __name__ == '__main__':
    pytest.main()

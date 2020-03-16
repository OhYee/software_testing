import pytest
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


if __name__ == '__main__':
    pytest.main()

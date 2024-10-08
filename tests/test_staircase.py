import pytest
from expects import equal, expect

from src.staircase import Staircase

"""
This problem was asked by Amazon.

There exists a staircase with N steps, and you can climb up either 1 or 2 steps at a time.

Given N, write a function that returns the number of unique ways you can climb the staircase.

The order of the steps matters.
"""


class TestStaircase:
    @pytest.mark.parametrize(
        "steps,expected",
        [
            (1, [[1]]),
            (2, [[1, 1], [2]]),
            (3, [[1, 1, 1], [1, 2], [2, 1]]),
            (4, [[1, 1, 1, 1], [1, 1, 2], [1, 2, 1], [2, 1, 1], [2, 2]]),
            (
                5,
                [
                    [1, 1, 1, 1, 1],
                    [1, 1, 1, 2],
                    [1, 1, 2, 1],
                    [1, 2, 1, 1],
                    [1, 2, 2],
                    [2, 1, 1, 1],
                    [2, 1, 2],
                    [2, 2, 1],
                ],
            ),
        ],
    )
    def test_solve(self, steps: int, expected: list[list[int]]) -> None:
        staircase = Staircase()

        stairs = staircase.solve(steps)

        expect(stairs).to(equal(expected))

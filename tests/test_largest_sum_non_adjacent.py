import pytest
from expects import equal, expect

from src.largest_sum_non_adjacent import largest_sum_non_adjacent

"""
This problem was asked by Airbnb.

Given a list of integers, write a function that returns the largest sum of non-adjacent numbers. Numbers can be 0 or negative.
"""


class TestLargestSumNonAdjacent:
    @pytest.mark.parametrize(
        "numbers, expected",
        [
            ([2, 4, 6, 2, 5], 13),
            ([5, 1, 1, 5], 10),
            ([3, 2, 5, 10, 7], 15),
        ],
    )
    def test_large_sum_non_adjacent(self, numbers: list[int], expected: int) -> None:
        larget_sum = largest_sum_non_adjacent(numbers)

        expect(larget_sum).to(equal(expected))

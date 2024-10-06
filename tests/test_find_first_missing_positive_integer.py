import pytest
from expects import equal, expect

from src.find_first_missing_positive_integer import find_first_missing_positive_integer

"""
This problem was asked by Stripe.

Given an array of integers, find the first missing positive integer in linear time and constant space. 

In other words, find the lowest positive integer that does not exist in the array. 

The array can contain duplicates and negative numbers as well.
"""


class TestFindFirstMissingPositiveInteger:
    @pytest.mark.parametrize(
        "array,solution",
        [
            ([1, 2, 3, 4, 5, 6], 7),
            ([-6, -5, -4, -3, -2, -1, 0, 1], 2),
            ([3, 4, -1, 1], 2),
            ([1, 2, 0], 3),
            ([1, 2, 0, 2], 3),
            ([1, 2, 2, 0], 3),
            ([3, 8], 1),
            ([-1, 19], 1),
        ],
    )
    def test_find_first_missing_positive_integer(
        self, array: list[int], solution: int
    ) -> None:
        missing = find_first_missing_positive_integer(array)

        expect(missing).to(equal(solution))

"""
This problem was asked by Airbnb.

Given a list of integers, write a function that returns the largest sum of non-adjacent numbers. Numbers can be 0 or negative.
"""


def largest_sum_non_adjacent(array: list[int]) -> int:
    if not array:
        return 0

    include = 0
    exclude = 0

    for item in array:
        new_exclude = max(include, exclude)
        include = exclude + item
        exclude = new_exclude

    return max(include, exclude)

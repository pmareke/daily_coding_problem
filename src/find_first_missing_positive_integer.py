"""
This problem was asked by Stripe.

Given an array of integers, find the first missing positive integer in linear time and constant space.

In other words, find the lowest positive integer that does not exist in the array.

The array can contain duplicates and negative numbers as well.
"""


def find_first_missing_positive_integer(array: list[int]) -> int:
    sorted_array = sorted(array)
    filtered_array = list(filter(lambda x: x > 0, sorted_array))
    last_element = filtered_array[-1]
    for item in range(len(filtered_array)):
        if filtered_array[item] != item + 1:
            return item + 1
    return last_element + 1

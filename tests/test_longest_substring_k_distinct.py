import pytest
from expects import equal, expect

from src.longest_substring_k_distinct import LongestSubstringKDistinct

"""
This problem was asked by Amazon.

Given an integer k and a string s, find the length of the longest substring that contains at most k distinct characters.
"""


class TestLongestSubstringKDistinct:
    @pytest.mark.parametrize(
        "k,string,expected",
        [
            (1, "aa", "aa"),
            (2, "abcba", "bcb"),
            (2, "abcde", "ab"),
            (2, "pqrst", "pq"),
            (3, "abcadcacacaca", "cadcacacaca"),
        ],
    )
    def test_longest_substring_k_distinct(
        self, k: int, string: str, expected: str
    ) -> None:
        longest_substring_k_distinct = LongestSubstringKDistinct(k)

        substring = longest_substring_k_distinct.find_longest_substring(string)

        expect(substring).to(equal(expected))

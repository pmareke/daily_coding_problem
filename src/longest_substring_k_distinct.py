"""
This problem was asked by Amazon.

Given an integer k and a string s, find the length of the longest substring that contains at most k distinct characters.
"""


class LongestSubstringKDistinct:
    def __init__(self, k: int) -> None:
        self.k = k

    def find_longest_substring(self, string: str) -> str:
        if self.k == 0 or not string:
            return ""

        char_count: dict[str, int] = {}
        left = 0
        max_length = 0
        start = 0

        for right in range(len(string)):
            char = string[right]
            char_count[char] = char_count.get(char, 0) + 1

            while len(char_count) > self.k:
                left_char = string[left]
                char_count[left_char] -= 1
                if char_count[left_char] == 0:
                    del char_count[left_char]
                left += 1

            if right - left + 1 > max_length:
                max_length = right - left + 1
                start = left

        return string[start : start + max_length]

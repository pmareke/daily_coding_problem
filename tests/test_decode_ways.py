import pytest
from expects import equal, expect

from src.decode_ways import decode_ways

"""
Good morning! Here's your coding interview problem for today.

This problem was asked by Facebook.

Given the mapping a = 1, b = 2, ... z = 26, and an encoded message, count the number of ways it can be decoded.

For example, the message '111' would give 3, since it could be decoded as 'aaa', 'ka', and 'ak'.

You can assume that the messages are decodable. For example, '001' is not allowed.
"""


class TestDecodeWays:
    @pytest.mark.parametrize(
        "message, times",
        [
            ("111", 3),
            ("1", 1),
            ("12", 2),
            ("226", 3),
            ("06", 0),
            ("10", 1),
            ("12345", 3),
        ],
    )
    def test_decode_ways(self, message: str, times: int) -> None:
        possible_decodes = decode_ways(message)

        expect(possible_decodes).to(equal(times))

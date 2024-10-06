"""
Good morning! Here's your coding interview problem for today.

This problem was asked by Facebook.

Given the mapping a = 1, b = 2, ... z = 26, and an encoded message, count the number of ways it can be decoded.

For example, the message '111' would give 3, since it could be decoded as 'aaa', 'ka', and 'ak'.

You can assume that the messages are decodable. For example, '001' is not allowed.
"""


def decode_ways(message: str) -> int:
    if not message:
        return 0

    if message[0] == "0":
        return 0

    dp = [0] * (len(message) + 1)

    dp[0] = 1  # Empty string
    dp[1] = 1  # First character (already checked that s[0] != '0')

    # Fill the dp array
    for idx in range(2, len(message) + 1):
        # Check single digit
        if 1 <= int(message[idx - 1 : idx]) <= 9:
            dp[idx] += dp[idx - 1]

        # Check two digits
        if 10 <= int(message[idx - 2 : idx]) <= 26:
            dp[idx] += dp[idx - 2]

    return dp[-1]

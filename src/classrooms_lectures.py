from collections import defaultdict

"""
This problem was asked by Snapchat.

Given an array of time intervals (start, end) for classroom lectures (possibly overlapping),
find the minimum number of rooms required.
"""


class ClassroomsLectures:
    def __init__(self, intervals: list[tuple[int, int]]) -> None:
        self.intervals = intervals

    def find_min(self) -> int:
        times: dict[int, int] = defaultdict(int)
        for interval in self.intervals:
            for time in range(interval[0], interval[1]):
                times[time] += 1
        return max(times.values())

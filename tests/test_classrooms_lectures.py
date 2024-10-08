import pytest
from expects import equal, expect

from src.classrooms_lectures import ClassroomsLectures

"""
This problem was asked by Snapchat.

Given an array of time intervals (start, end) for classroom lectures (possibly overlapping),
find the minimum number of rooms required.
"""


class TestClassroomsLectures:
    @pytest.mark.parametrize(
        "intervals,expected",
        [
            ([(30, 75), (0, 50), (60, 150)], 2),
            ([(0, 30), (5, 10), (15, 20)], 2),
            ([(10, 20), (20, 30), (30, 40)], 1),
            ([(0, 50), (25, 60), (35, 70), (55, 80)], 3),
            ([(10, 15), (12, 25), (20, 30), (5, 10), (25, 35)], 2),
            ([(100, 200), (150, 250), (120, 180), (170, 300)], 4),
        ],
    )
    def test_find_min(self, intervals: list[tuple[int, int]], expected: int) -> None:
        classrooms_lectures = ClassroomsLectures(intervals)

        min_rooms = classrooms_lectures.find_min()

        expect(min_rooms).to(equal(expected))

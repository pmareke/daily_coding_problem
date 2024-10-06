from typing import Callable

"""
This problem was asked by Apple.

Implement a job scheduler which takes in a function f and an integer n, and calls f after n milliseconds.
"""


class Scheduler:
    def __init__(self, sleep: Callable) -> None:
        self.sleep = sleep

    def schedule(self, func: Callable, milliseconds: int) -> None:
        self.sleep(milliseconds)
        func()

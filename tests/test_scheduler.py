from doublex import Spy
from doublex_expects import have_been_called, have_been_called_with
from expects import expect

from src.scheduler import Scheduler

"""
This problem was asked by Apple.

Implement a job scheduler which takes in a function f and an integer n, and calls f after n milliseconds.
"""


class TestScheduler:
    def test_scheduler(self) -> None:
        milliseconds = 1000
        spy = Spy()
        scheduler = Scheduler(spy.sleep)  # type: ignore

        scheduler.schedule(spy.func, milliseconds)

        expect(spy.sleep).to(have_been_called_with(milliseconds))
        expect(spy.func).to(have_been_called)

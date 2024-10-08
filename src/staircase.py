"""
This problem was asked by Amazon.

There exists a staircase with N steps, and you can climb up either 1 or 2 steps at a time.

Given N, write a function that returns the number of unique ways you can climb the staircase.

The order of the steps matters.
"""


class Staircase:
    def solve(self, steps: int) -> list[list[int]]:
        return self._find_paths(steps, 0, [])

    def _find_paths(self, steps: int, current_step: int, path: list) -> list[list[int]]:
        results: list[list[int]] = []

        if current_step > steps:
            return results

        if current_step == steps:
            results.append(path)
            return results

        return [
            *results,
            *self._find_paths(steps, current_step + 1, path + [1]),
            *self._find_paths(steps, current_step + 2, path + [2]),
        ]

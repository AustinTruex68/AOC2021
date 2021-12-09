from typing import Iterable
from aocfw import SolutionBase


class Solution(SolutionBase):
    def solve(self, data: Iterable[int]) -> int:
        raise NotImplementedError()


if __name__ == '__main__':
    Solution.run(source='input.txt')

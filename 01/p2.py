from typing import Iterable
from aocfw import SolutionBase


class Solution(SolutionBase):
    def solve(self, data: Iterable[int]) -> int:
        data = list(data)
        answer = 0
        for index, d in enumerate(list(data)):
            if index < 3:
                continue
            if self.sum_last_3(data, index) > self.sum_last_3(data, index - 1):
                answer = answer + 1
        return answer

    def sum_last_3(self, data, index):
        v1 = data[index]
        v2 = data[index - 1]
        v3 = data[index - 2]
        return v1 + v2 + v3


if __name__ == '__main__':
    Solution.run(source='input.txt')

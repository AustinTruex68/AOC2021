from typing import Iterable
from aocfw import SolutionBase, IParser, StringParser


class Solution(SolutionBase):
    # how to change data coming in
    # bindings = {IParser: StringParser}
    def solve(self, data: Iterable[int]) -> int:
        data = list(data)
        answer = 0
        for index, d in enumerate(list(data)):
            if index == 0:
                continue
            if d > data[index - 1]:
                answer = answer + 1
        return answer

if __name__ == '__main__':
    Solution.run(source='input.txt')

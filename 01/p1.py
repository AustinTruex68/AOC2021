from typing import Iterable
from aocfw import SolutionBase, IParser, StringParser


class Solution(SolutionBase):
    bindings = {IParser: StringParser}
    def solve(self, data: Iterable[str]) -> int:
        data = list(data)
        i = 0
        answer = 0
        for d in data:
            i = i + 1
            if i == 0:
                continue
        if int(data[i - 2]) < int(d):
            answer = answer + 1
        return answer


if __name__ == '__main__':
    Solution.run(source='input.txt')

from typing import Iterable
from aocfw import SolutionBase, IParser, StringParser


class Solution(SolutionBase):
    bindings = {IParser: StringParser}
    def solve(self, data: Iterable[str]) -> int:
        horz = 0
        vert = 0
        for d in data:
            cmd, val = d.split(" ")
            if cmd == "forward":
                horz = horz + int(val)
            elif cmd == "down":
                vert = vert + int(val)
            else:
                vert = vert - int(val)

        return vert*horz


if __name__ == '__main__':
    Solution.run(source='input.txt')

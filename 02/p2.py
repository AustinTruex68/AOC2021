from typing import Iterable
from aocfw import SolutionBase, IParser, StringParser


class Solution(SolutionBase):
    bindings = {IParser: StringParser}
    def solve(self, data: Iterable[str]) -> int:
        horz = 0
        depth = 0
        aim = 0
        for d in data:
            cmd, val = d.split(" ")
            if cmd == "forward":
                horz = horz + int(val)
                p = aim * val
                depth = depth + (aim * int(val))
            elif cmd == "down":
                aim = aim + int(val)
            else:
                aim = aim - int(val)

        return depth*horz


if __name__ == '__main__':
    Solution.run(source='input.txt')

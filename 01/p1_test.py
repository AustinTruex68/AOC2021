from unittest import TestCase, main
from aocfw import TestCaseMixin
from p1 import Solution


class SolutionTests(TestCase, TestCaseMixin):

    solution = Solution
    source = 'sample.txt'
    given = 7

    def test_foo(self):
        self.get_parsed_data()


if __name__ == '__main__':
    main()

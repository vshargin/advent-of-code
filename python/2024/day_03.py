import re

from utils import AOCSolution


class Solution(AOCSolution):
    def _parse_input(self, puzzle_input: str):
        self._instructions = "".join(puzzle_input)

    def _solve_common(self):
        pass

    def solve_part_1(self):
        print(self._instructions)
        return self._execute(self._instructions)

    def solve_part_2(self):
        return self._execute(self._process_conditionals(self._instructions))

    @staticmethod
    def _execute(instructions: str):
        return sum(
            [
                int(a) * int(b)
                for a, b in re.findall(r"mul\((\d+),(\d+)\)", instructions)
            ]
        )

    @staticmethod
    def _process_conditionals(instructions: str):
        return re.sub(r"don't\(\).*?(?:do\(\)|$)", "", instructions)

import re
from dataclasses import dataclass

from utils import AOCSolution


@dataclass
class Machine:
    x: int
    y: int
    a_x: int
    a_y: int
    b_x: int
    b_y: int


class Solution(AOCSolution):
    def _parse_input(self, puzzle_input: str):
        regex_increments = r"X\+([0-9]+), Y\+([0-9]+)"
        regex_coordinates = r"X=([0-9]+), Y=([0-9]+)"

        self._machines: list[Machine] = []

        for machine in "\n".join(puzzle_input).split("\n\n"):
            x, y = re.search(regex_coordinates, machine).groups()
            increments = re.findall(regex_increments, machine)
            a_x, a_y = increments[0]
            b_x, b_y = increments[1]
            self._machines.append(
                Machine(int(x), int(y), int(a_x), int(a_y), int(b_x), int(b_y))
            )

    def _solve_common(self):
        pass

    def solve_part_1(self) -> int:
        total_tokens = 0

        for machine in self._machines:
            tokens = self.solve_machine(machine)
            if tokens is not None:
                total_tokens += tokens

        return total_tokens

    def solve_part_2(self) -> int:
        total_tokens = 0

        for machine in self._machines:
            tokens = self.solve_machine(machine, offset=10000000000000)
            if tokens is not None:
                total_tokens += tokens

        return total_tokens

    @staticmethod
    def solve_machine(machine: Machine, offset: int = 0) -> int | None:
        b = (
            machine.a_y * (machine.x + offset) - machine.a_x * (machine.y + offset)
        ) // (machine.a_y * machine.b_x - machine.a_x * machine.b_y)
        mod_b = (
            machine.a_y * (machine.x + offset) - machine.a_x * (machine.y + offset)
        ) % (machine.a_y * machine.b_x - machine.a_x * machine.b_y)
        a = ((machine.x + offset) - machine.b_x * b) // machine.a_x
        mod_a = ((machine.x + offset) - machine.b_x * b) % machine.a_x

        if mod_b != 0 or mod_a != 0:
            return None
        else:
            return a * 3 + b

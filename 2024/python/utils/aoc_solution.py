from abc import ABC, abstractmethod


class AOCSolution(ABC):
    def __init__(self, input: str | list[str]):
        if isinstance(input, str):
            with open(input) as f:
                self._parse_input(f)
        else:
            self._parse_input(input)

    @abstractmethod
    def _parse_input(self, input):
        pass

    def solve(self, part: int):
        self._solve_common()

        if part == 1:
            return self.solve_part_1()
        elif part == 2:
            return self.solve_part_2()
        else:
            raise ValueError("Part must be 1 or 2")

    @abstractmethod
    def _solve_common(self):
        pass

    @abstractmethod
    def solve_part_1(self):
        pass

    @abstractmethod
    def solve_part_2(self):
        pass

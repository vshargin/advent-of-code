import re

from utils import AOCSolution


class Solution(AOCSolution):
    def _parse_input(self, puzzle_input: str):
        self._matrix = [list(row) for row in puzzle_input]

    def _solve_common(self):
        pass

    def solve_part_1(self):
        return self.count_xmas(self._matrix)

    def solve_part_2(self):
        return self.count_x_mas(self._matrix)

    @staticmethod
    def count_xmas(matrix: list[list[str]]) -> int:
        directions = [
            (1, 0),
            (0, 1),
            (1, 1),
            (1, -1),
            (-1, 1),
            (-1, -1),
            (-1, 0),
            (0, -1),
        ]
        max_i = len(matrix)
        max_j = len(matrix[0])

        count = 0
        for i in range(max_i):
            for j in range(max_j):
                for direction in directions:
                    word = ""
                    for k in range(4):
                        new_i = i + k * direction[0]
                        new_j = j + k * direction[1]
                        if 0 <= new_i <= max_i - 1 and 0 <= new_j <= max_j - 1:
                            word += matrix[new_i][new_j]
                    if word == "XMAS":
                        count += 1

        return count

    @staticmethod
    def count_x_mas(matrix: list[list[str]]) -> int:
        max_i = len(matrix) - 1
        max_j = len(matrix[0]) - 1

        count = 0
        for i in range(1, max_i):
            for j in range(1, max_j):
                center = matrix[i][j]
                if center != "A":
                    continue
                diag_1 = matrix[i - 1][j - 1] + matrix[i + 1][j + 1]
                diag_2 = matrix[i - 1][j + 1] + matrix[i + 1][j - 1]
                if "M" in diag_1 and "S" in diag_1 and "M" in diag_2 and "S" in diag_2:
                    count += 1
        return count

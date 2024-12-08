from itertools import combinations

from utils import AOCSolution


class Solution(AOCSolution):
    def _parse_input(self, puzzle_input: str):
        self._matrix = [list(row) for row in puzzle_input]

    def _solve_common(self):
        self._n = len(self._matrix) - 1
        self._m = len(self._matrix[0]) - 1

        self._antennas = {}

        for i, row in enumerate(self._matrix):
            for j, cell in enumerate(row):
                if cell != ".":
                    self._antennas[cell] = self._antennas.get(cell, []) + [(i, j)]

    def solve_part_1(self):
        antinodes = set()

        for same_frequency_antennas in self._antennas.values():
            for antenna_a, antenna_b in combinations(same_frequency_antennas, 2):
                antinodes.update(
                    Solution.get_antinodes(antenna_a, antenna_b, self._n, self._m)
                )

        return len(antinodes)

    def solve_part_2(self):
        antinodes = set()

        for same_frequency_antennas in self._antennas.values():
            for antenna_a, antenna_b in combinations(same_frequency_antennas, 2):
                antinodes.update(
                    Solution.get_antinodes(
                        antenna_a, antenna_b, self._n, self._m, part2=True
                    )
                )

        return len(antinodes)

    @staticmethod
    def get_antinodes(a, b, n, m, part2=False):
        a_i, a_j = a
        b_i, b_j = b
        di = a_i - b_i
        dj = a_j - b_j
        antinodes = []

        if a == b:
            return antinodes
        if part2:
            antinodes += [a, b]

        i = 1

        while True:
            if not part2 and i > 1:
                break

            antinode_candidates = [
                (a_i + i * di, a_j + i * dj),
                (b_i - i * di, b_j - i * dj),
            ]
            antinode_candidates = [
                antinode
                for antinode in antinode_candidates
                if 0 <= antinode[0] <= n and 0 <= antinode[1] <= m
            ]

            if not antinode_candidates:
                break

            antinodes += antinode_candidates

            i += 1

        return antinodes

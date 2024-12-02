from utils import AOCSolution


class Solution(AOCSolution):
    def _parse_input(self, input):
        self._left = []
        self._right = []
        for line in input:
            left_item, right_item = line.strip().split("   ")
            self._left.append(int(left_item))
            self._right.append(int(right_item))

    def _solve_common(self):
        self._left.sort()
        self._right.sort()

    def solve_part_1(self):
        distances = []
        for left_item, right_item in zip(self._left, self._right):
            distances.append(abs(left_item - right_item))
        total_distance = sum(distances)

        return total_distance

    def solve_part_2(self):
        right_frequencies = {}
        for item in self._right:
            right_frequencies[item] = right_frequencies.get(item, 0) + 1

        distances = []
        for item in self._left:
            distances.append(item * right_frequencies.get(item, 0))
        total_distance = sum(distances)

        return total_distance

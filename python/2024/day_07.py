from utils import AOCSolution


class Solution(AOCSolution):
    def _parse_input(self, puzzle_input: str):
        self._test_values = []
        self._sequences = []
        for row in puzzle_input:
            self._sequences.append([int(x) for x in row.split(": ")[1].split()])
            self._test_values.append(int(row.split(": ")[0]))

    def _solve_common(self):
        pass

    def solve_part_1(self):
        count = 0
        for test_value, sequence in zip(self._test_values, self._sequences):
            if Solution.test(test_value, sequence):
                count += test_value
        return count

    def solve_part_2(self):
        count = 0
        for test_value, sequence in zip(self._test_values, self._sequences):
            if Solution.test(test_value, sequence, with_concat=True):
                count += test_value
        return count

    @staticmethod
    def test(target_value, sequence, acc=0, with_concat=False):
        if not sequence:
            return acc == target_value
        if acc > target_value:
            return False
        return (
            Solution.test(
                target_value, sequence[1:], acc + sequence[0], with_concat=with_concat
            )
            or Solution.test(
                target_value, sequence[1:], acc * sequence[0], with_concat=with_concat
            )
            or (
                with_concat
                and Solution.test(
                    target_value,
                    sequence[1:],
                    int(str(acc) + str(sequence[0])),
                    with_concat=with_concat,
                )
            )
        )

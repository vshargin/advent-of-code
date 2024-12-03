from typing import Tuple

from utils import AOCSolution


class Solution(AOCSolution):
    def _parse_input(self, puzzle_input: list[str]):
        self._reports = []
        for line in puzzle_input:
            report = list(map(int, line.strip().split(" ")))
            self._reports.append(report)

    def _solve_common(self):
        pass

    def solve_part_1(self) -> int:
        safe_reports = 0
        for i, report in enumerate(self._reports):
            safe, _ = self.test_safety(report)
            if safe:
                safe_reports += 1

        return safe_reports

    def solve_part_2(self) -> int:
        safe_reports = 0
        for i, report in enumerate(self._reports):
            safe, removal_candidates = self.test_safety(report)
            if safe:
                safe_reports += 1
            else:
                for i in removal_candidates:
                    safe, _ = self.test_safety(report[:i] + report[i + 1:])
                    if safe:
                        safe_reports += 1
                        break

        return safe_reports

    @staticmethod
    def test_safety(report: list[int]) -> Tuple[bool, set[int]]:
        safe = True
        last_change = None
        last_value = None
        removal_candidates = set()
        for i, level in enumerate(report):
            if last_value is not None:
                if level < last_value:
                    change = "decreasing"
                elif level > last_value:
                    change = "increasing"
                else:
                    change = None
                if change and last_change and last_change != change:
                    safe = False
                    removal_candidates.update([i - 2, i - 1, i])
                last_change = change
                abs_diff = abs(level - last_value)
                if abs_diff > 3 or abs_diff == 0:
                    safe = False
                    removal_candidates.update([i - 1, i])
            last_value = level

        return safe, removal_candidates

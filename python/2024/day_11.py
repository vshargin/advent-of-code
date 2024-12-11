from utils import AOCSolution


class Solution(AOCSolution):
    def _parse_input(self, puzzle_input: str):
        self._stones = [int(x) for x in puzzle_input[0].split()]
        self._stones = {x: self._stones.count(x) for x in self._stones}

    def _solve_common(self):
        pass

    def solve_part_1(self) -> int:
        return Solution.blink(self._stones, 25)

    def solve_part_2(self) -> int:
        return Solution.blink(self._stones, 75)

    @staticmethod
    def blink(stones: dict[int, int], blinks: int) -> int:
        for _ in range(blinks):
            stones_after_blinking = {}
            for stone, count in stones.items():
                new_stones = Solution.blink_at_stone(stone)
                for new_stone in new_stones:
                    stones_after_blinking[new_stone] = (
                        stones_after_blinking.get(new_stone, 0) + count
                    )
            stones = stones_after_blinking

        stone_count = sum([count for count in stones.values()])

        return stone_count

    @staticmethod
    def blink_at_stone(stone: int) -> list[int]:
        if stone == 0:
            new_stones = [1]
        elif len(str(stone)) % 2 == 0:
            middle_index = len(str(stone)) // 2
            left = int(str(stone)[:middle_index])
            right = int(str(stone)[middle_index:])
            new_stones = [left, right]
        else:
            new_stones = [stone * 2024]
        return new_stones

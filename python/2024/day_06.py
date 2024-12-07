from utils import AOCSolution


class Solution(AOCSolution):
    def _parse_input(self, puzzle_input: str):
        self._matrix = [list(row) for row in puzzle_input]

    def _solve_common(self):
        self._obstacles = self.get_obstacles(self._matrix)
        self._starting_position = self.get_guard_location(self._matrix)
        self._size = len(self._matrix)
        self._states = self.walk(self._starting_position, self._obstacles, self._size)

    def solve_part_1(self):
        return len({position for position, _ in self._states})

    def solve_part_2(self):
        potential_obstacles = {position for position, _ in self._states}
        potential_obstacles.remove(self._starting_position[0])
        potential_obstacles.remove(
            self.get_next_position(
                self._starting_position[0], self._starting_position[1]
            )
        )

        loops = 0
        for candidate_obstacle in potential_obstacles:
            if (
                self.walk(
                    self._starting_position,
                    self._obstacles | {candidate_obstacle},
                    self._size,
                )
                is None
            ):
                loops += 1
        return loops

    @staticmethod
    def get_guard_location(puzzle_input):
        directions = {"^": 0, "v": 1, "<": 2, ">": 3}
        for i, row in enumerate(puzzle_input):
            for j, cell in enumerate(row):
                if cell in ["^", "v", "<", ">"]:
                    return (i, j), directions[cell]

    @staticmethod
    def get_next_position(position, direction):
        movement = {0: (-1, 0), 2: (1, 0), 1: (0, 1), 3: (0, -1)}
        i, j = position
        di, dj = movement[direction]
        next_position = i + di, j + dj
        return next_position

    @staticmethod
    def get_obstacles(matrix: list[list[str]]) -> set[tuple[int, int]]:
        obstacles = set()
        for i, row in enumerate(matrix):
            for j, cell in enumerate(row):
                if cell == "#":
                    obstacles.add((i, j))
        return obstacles

    @staticmethod
    def walk(
        start_position: tuple[int, int], obstacles: set[tuple[int, int]], size: int
    ) -> set[tuple[int, int]]:
        states = set()
        guard_position, direction = start_position
        while True:
            if (guard_position, direction) in states:
                return None
            states.add((guard_position, direction))
            next_position = Solution.get_next_position(guard_position, direction)
            if next_position in obstacles:
                direction = (direction + 1) % 4
            else:
                if min(next_position) >= 0 and max(next_position) < size:
                    guard_position = next_position
                else:
                    break
        return states

from collections import deque

from utils import AOCSolution


class Solution(AOCSolution):
    def _parse_input(self, puzzle_input: str):
        self._bytes = [map(int, row.split(",")) for row in puzzle_input]
        self._size_x = 71
        self._size_y = 71
        self._stop_at = 1024

    def _solve_common(self):
        pass

    def solve_part_1(self) -> int:
        matrix = [[0 for _ in range(self._size_x)] for _ in range(self._size_y)]
        for i, (y, x) in enumerate(self._bytes):
            if i == self._stop_at:
                break
            matrix[y][x] = 1

        return self.bfs(
            matrix,
            (0, 0),
            (self._size_y - 1, self._size_x - 1),
            self._size_x,
            self._size_y,
        )

    def solve_part_2(self) -> str:
        matrix = [[0 for _ in range(self._size_x)] for _ in range(self._size_y)]
        for i, (y, x) in enumerate(self._bytes):
            matrix[y][x] = 1

            if (
                self.bfs(
                    matrix,
                    (0, 0),
                    (self._size_y - 1, self._size_x - 1),
                    self._size_x,
                    self._size_y,
                )
                == -1
            ):
                return f"{y},{x}"

    @staticmethod
    def get_neighbours(x, y, size_x, size_y):
        neighbours = []
        if x > 0:
            neighbours.append((x - 1, y))
        if x < size_x - 1:
            neighbours.append((x + 1, y))
        if y > 0:
            neighbours.append((x, y - 1))
        if y < size_y - 1:
            neighbours.append((x, y + 1))
        return neighbours

    @staticmethod
    def bfs(matrix, start, target, size_x, size_y):
        queue = deque([start])
        visited = set()
        distance = 0
        while queue:
            for _ in range(len(queue)):
                x, y = queue.popleft()
                if (x, y) == target:
                    return distance
                if (x, y) in visited:
                    continue
                visited.add((x, y))
                if matrix[y][x] == 1:
                    continue
                for neighbour in Solution.get_neighbours(x, y, size_x, size_y):
                    if neighbour not in visited:
                        queue.append(neighbour)
            distance += 1
        return -1

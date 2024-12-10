from utils import AOCSolution


class Solution(AOCSolution):
    def _parse_input(self, puzzle_input: str):
        self._map = [[int(x) for x in list(row)] for row in puzzle_input]

    def _solve_common(self):
        self._trailheads = []
        for i in range(len(self._map)):
            for j in range(len(self._map[i])):
                if self._map[i][j] == 0:
                    self._trailheads.append((i, j))

        self._total_score = 0
        self._total_rating = 0
        for trailhead in self._trailheads:
            peaks, trails = Solution.hike(self._map, trailhead, set(), [], [])
            self._total_score += len(peaks)
            self._total_rating += len(trails)

    def solve_part_1(self):
        return self._total_score

    def solve_part_2(self):
        return self._total_rating

    @staticmethod
    def hike(
        topo_map: list[list[int]],
        position: tuple[int, int],
        peaks: set[tuple[int, int]],
        current_trail: list[tuple[int, int]],
        trails: list[list[tuple[int, int]]],
    ):
        max_i = len(topo_map) - 1
        max_j = len(topo_map[0]) - 1

        movement = {"up": (-1, 0), "down": (1, 0), "left": (0, -1), "right": (0, 1)}

        i, j = position
        current_trail = current_trail + [position]

        if topo_map[i][j] == 9:
            peaks.add(position)
            trails = trails + [current_trail]
            return peaks, trails

        moves = ["up", "down", "left", "right"]

        if i == 0:
            moves.remove("up")
        if i == max_i:
            moves.remove("down")
        if j == 0:
            moves.remove("left")
        if j == max_j:
            moves.remove("right")

        for move in moves:
            di, dj = movement[move]
            new_i, new_j = (i + di, j + dj)
            if topo_map[new_i][new_j] == topo_map[i][j] + 1:
                new_peaks, new_trails = Solution.hike(
                    topo_map, (new_i, new_j), peaks, current_trail, trails
                )
                peaks = peaks.union(new_peaks)
                for trail in new_trails:
                    if trail not in trails:
                        trails = trails + [trail]

        return peaks, trails

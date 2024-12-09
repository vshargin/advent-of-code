from utils import AOCSolution


class Solution(AOCSolution):
    def _parse_input(self, puzzle_input: str):
        self._disk_map = puzzle_input[0]

    def _solve_common(self):
        self._file_sizes = [
            int(file_size)
            for i, file_size in enumerate(self._disk_map)
            if int(i) % 2 == 0
        ]

        self._sequence = [
            file_id
            for file_ids in [
                [i // 2] * int(length) if i % 2 == 0 else [None] * int(length)
                for i, length in enumerate(self._disk_map)
            ]
            for file_id in file_ids
        ]

    def solve_part_1(self):
        defragmented_sequence = self._sequence.copy()

        while None in defragmented_sequence:
            if defragmented_sequence[-1] is None:
                defragmented_sequence.pop()
            else:
                defragmented_sequence[defragmented_sequence.index(None)] = (
                    defragmented_sequence.pop()
                )

        checksum = 0
        for i, file_id in enumerate(defragmented_sequence):
            checksum += i * file_id

        return checksum

    def solve_part_2(self):
        gaps = {}
        i = 0
        while i < len(self._sequence):
            if self._sequence[i] is None:
                start = i
                while self._sequence[i] is None:
                    i += 1
                gaps[start] = i - start
            else:
                i += 1

        file_starts = [
            self._sequence.index(file_id) for file_id in range(len(self._file_sizes))
        ]

        for file_id in reversed(range(0, len(self._file_sizes))):
            candidate_gaps = [
                start_position
                for start_position, gap_length in gaps.items()
                if gap_length >= self._file_sizes[file_id]
                and start_position < file_starts[file_id]
            ]
            if not candidate_gaps:
                continue
            else:
                new_file_start = min(candidate_gaps)
                gaps[new_file_start + self._file_sizes[file_id]] = (
                    gaps[new_file_start] - self._file_sizes[file_id]
                )
                del gaps[new_file_start]
                file_starts[file_id] = new_file_start

        checksum = 0
        for file_id in range(len(self._file_sizes)):
            checksum += sum(
                [
                    file_id * position
                    for position in range(
                        file_starts[file_id],
                        file_starts[file_id] + self._file_sizes[file_id],
                    )
                ]
            )

        return checksum

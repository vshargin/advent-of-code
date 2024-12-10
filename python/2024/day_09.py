from utils import AOCSolution


class Solution(AOCSolution):
    def _parse_input(self, puzzle_input: str):
        self._disk_map = puzzle_input[0]

    def _solve_common(self):
        pass

    def solve_part_1(self):
        sequence = [
            file_id
            for file_ids in [
                [i // 2] * int(length) if i % 2 == 0 else [None] * int(length)
                for i, length in enumerate(self._disk_map)
            ]
            for file_id in file_ids
        ]
        while None in sequence:
            if sequence[-1] is None:
                sequence.pop()
            else:
                sequence[sequence.index(None)] = sequence.pop()

        checksum = 0
        for i, file_id in enumerate(sequence):
            checksum += i * file_id

        return checksum

    def solve_part_2(self):
        cursor = 0
        files = {}
        gaps = {}
        for i, size in enumerate(self._disk_map):
            if int(i) % 2 == 0:
                files[int(i) // 2] = [cursor, int(size)]
            else:
                gaps[cursor] = int(size)
            cursor += int(size)

        for file_id in reversed(range(0, len(files))):
            candidate_gaps = [
                start_position
                for start_position, gap_length in gaps.items()
                if gap_length >= files[file_id][1]
                and start_position < files[file_id][0]
            ]
            if not candidate_gaps:
                continue
            else:
                new_file_start = min(candidate_gaps)
                gaps[new_file_start + files[file_id][1]] = (
                    gaps[new_file_start] - files[file_id][1]
                )
                del gaps[new_file_start]
                files[file_id][0] = new_file_start

        checksum = 0
        for file_id, file_info in files.items():
            checksum += sum(
                [
                    file_id * position
                    for position in range(
                        files[file_id][0],
                        files[file_id][0] + files[file_id][1],
                    )
                ]
            )

        return checksum

def check_overlap(start_a: int, end_a: int, start_b: int, end_b: int) -> bool:
    if len(set(range(start_a, end_a + 1))
           .intersection(set(range(start_b, end_b + 1)))) > 0:
        return True
    else:
        return False


def parse_input(input_line: str) -> tuple[int, int, int, int]:
    a, b = input_line.split(',')
    return int(a.split('-')[0]), int(a.split('-')[1]),\
        int(b.split('-')[0]), int(b.split('-')[1])


with open("inputs/day_04.txt") as input_file:
    puzzle_input = [parse_input(line)
                    for line in input_file.read().split("\n")]

overlapping_pair_count = 0

for pair in puzzle_input:
    if check_overlap(*pair):
        overlapping_pair_count += 1

print(overlapping_pair_count)

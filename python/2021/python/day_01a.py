def count_increases(input: list[int]) -> int:
    increase_count = 0

    for i in range(1, len(input)):
        if input[i] > input[i - 1]:
            increase_count += 1

    return increase_count


test_input = [199, 200, 208, 210, 200, 208, 240, 269, 260, 263]

assert count_increases(test_input) == 7

with open("inputs/day_01.txt") as input_file:
    puzzle_input = [int(line) for line in input_file.read().split("\n")]

print(count_increases(puzzle_input))

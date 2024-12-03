def get_priority(item: str) -> int:
    if ord(item) >= 65 and ord(item) <= 90:
        return ord(item) - 64 + 26
    elif ord(item) >= 97 and ord(item) <= 122:
        return ord(item) - 96


with open("inputs/day_03.txt") as input_file:
    puzzle_input = [line for line in input_file.read().split("\n")]

priorities_sum = 0

for n in range(0, len(puzzle_input), 3):
    rucksacks = puzzle_input[n:n+3]

    badge = set.intersection(*map(set, rucksacks)).pop()

    priorities_sum += get_priority(badge)

print(priorities_sum)

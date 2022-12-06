def get_priority(item: str) -> int:
    if ord(item) >= 65 and ord(item) <= 90:
        return ord(item) - 64 + 26
    elif ord(item) >= 97 and ord(item) <= 122:
        return ord(item) - 96


with open("inputs/day_03.txt") as input_file:
    puzzle_input = [line for line in input_file.read().split("\n")]

priorities_sum = 0

for rucksack in puzzle_input:
    first = rucksack[:len(rucksack) // 2]
    second = rucksack[len(rucksack) // 2:]

    priorities = map(get_priority, set(first).intersection(set(second)))
    priorities_sum += sum(priorities)

print(priorities_sum)

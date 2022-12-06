with open("inputs/day_01.txt") as input_file:
    puzzle_input = [int(line) if line else None
                    for line in input_file.read().split("\n")]

cumsum = 0
max_calories = 0

for food in puzzle_input:
    if food is not None:
        cumsum += food
    else:
        max_calories = max(cumsum, max_calories)
        cumsum = 0

print(max_calories)

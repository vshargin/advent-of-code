with open("inputs/day_01.txt") as input_file:
    puzzle_input = [int(line) if line else None
                    for line in input_file.read().split("\n")]

cumsum = 0
calorie_sums = []

for food in puzzle_input:
    if food is not None:
        cumsum += food
    else:
        calorie_sums.append(cumsum)
        cumsum = 0

print(sum(sorted(calorie_sums)[-3:]))

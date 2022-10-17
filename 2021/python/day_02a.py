def calculate_result(input: list[tuple[str, int]]) -> int:
    horizontal_position = 0
    vertical_position = 0

    for direction, distance in input:
        if direction == 'up':
            vertical_position -= distance
        elif direction == 'down':
            vertical_position += distance
        elif direction == 'forward':
            horizontal_position += distance

    return horizontal_position * vertical_position


test_input = [
    ('forward', 5),
    ('down', 5),
    ('forward', 8),
    ('up', 3),
    ('down', 8),
    ('forward', 2)
]

assert calculate_result(test_input) == 150


with open("inputs/day_02.txt") as input_file:
    puzzle_input = [(line.split(' ')[0], int(line.split(' ')[1]))
                    for line in input_file.read().split("\n")]

print(calculate_result(puzzle_input))

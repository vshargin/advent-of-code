from collections import deque


def parse_input(puzzle_input: str) -> tuple[list[deque], list[tuple]]:
    n_stacks = (len(puzzle_input[0]) + 1) // 4

    stacks = [deque() for _ in range(n_stacks)]
    commands = []

    for line in puzzle_input:
        if '[' in line:
            for i in range(n_stacks):
                if line[4 * i + 1] != ' ':
                    stacks[i].appendleft(line[4 * i + 1])
        elif line.startswith('move'):
            commands.append((int(line.split(' ')[1]),
                             int(line.split(' ')[3]),
                             int(line.split(' ')[5])))

    return (stacks, commands)


with open("inputs/day_05.txt") as input_file:
    puzzle_input = [line for line in input_file.read().split("\n")]

stacks, commands = parse_input(puzzle_input)

for quantity, source, destination in commands:
    for _ in range(quantity):
        stacks[destination - 1].append(stacks[source - 1].pop())

print(''.join([stack.pop() for stack in stacks]))

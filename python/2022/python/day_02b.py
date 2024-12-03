hand_values = {
    'rock': 1,
    'paper': 2,
    'scissors': 3
}

opponent_hands = {
    'A': 'rock',
    'B': 'paper',
    'C': 'scissors'
}

losing_hands = {
    'rock': 'scissors',
    'paper': 'rock',
    'scissors': 'paper'
}

winning_hands = {
    'rock': 'paper',
    'paper': 'scissors',
    'scissors': 'rock'
}


def score_game(opponent: str, player: str) -> int:
    scores = {
        'rock': {
            'paper': 6,
            'rock': 3,
            'scissors': 0
        },
        'paper': {
            'rock': 0,
            'paper': 3,
            'scissors': 6
        },
        'scissors': {
            'paper': 0,
            'scissors': 3,
            'rock': 6
        }
    }

    return scores[opponent][player]


with open("inputs/day_02.txt") as input_file:
    puzzle_input = [(line.split(' ')[0], line.split(' ')[1])
                    for line in input_file.read().split("\n")]

total_score = 0

for opponent, strategy in puzzle_input:
    opponent = opponent_hands[opponent]
    if strategy == 'Y':
        player = opponent
    elif strategy == 'X':
        player = losing_hands[opponent]
    elif strategy == 'Z':
        player = winning_hands[opponent]

    total_score += score_game(opponent, player)
    total_score += hand_values[player]

print(total_score)

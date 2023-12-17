import sys
import itertools

limits = {
    "red": 12,
    "green": 13,
    "blue": 14
}

def split_word(input, target):
    while True:
        pos = input.find(target)
        end = pos + len(target)
        if pos < 0:
            yield input
            return
        yield input[:pos]
        input = input[end:]

def get_nth_word(input, target, pos):
    parts = list(split_word(input, target))
    return parts[pos]


def is_round_valid(limits, round):
    moves = split_word(round, ", ")
    color_counts = (move.split(" ") for move in moves)
    return all(
        int(count) <= limits[color]
        for count, color in color_counts
    )

def is_game_valid(limits, game):
    rounds = split_word(game, "; ")
    return all(
        is_round_valid(limits, round)
        for round in rounds
    )

input = (line.strip() for line in sys.stdin)

games = (get_nth_word(line, ": ", 1) for line in input)

valid_games = (
    game_id for game_id, game in enumerate(games, start=1)
    if is_game_valid(limits, game)
)

print(sum(valid_games))


import sys
from functools import reduce
from collections import defaultdict
import re

color_regex = re.compile(r"([0-9]+) (red|green|blue)")

def product(it):
    return reduce(lambda val, acc: val * acc, it, 1)

def get_game_min_counts(color_counts):
    counts = defaultdict(list)
    for count, color in color_counts:
        counts[color].append(int(count))

    return {color: max(nums) for color, nums in counts.items()}    

def get_game_power(color_counts):
    return product(get_game_min_counts(color_counts).values())


input = (line.strip() for line in sys.stdin)

games = (color_regex.findall(line) for line in input)

game_powers = (
   get_game_power(game) for game in games
)

print(sum(game_powers))


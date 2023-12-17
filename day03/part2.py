import sys
import re
from functools import reduce
from collections import namedtuple, defaultdict

PartNumber = namedtuple("PartNumber", ["pos_x", "pos_y", "value"])
GearCoords = namedtuple("GearCoords", ["x", "y"])

def product(it):
    return reduce(lambda val, acc: val * acc, it, 1)

def find_number_coordinates(lines):
    number_re = re.compile(r"([0-9]+)")

    for line_num, line in enumerate(lines):
        matches = number_re.finditer(line)
        for res in matches:
            yield PartNumber(res.start(), line_num, res.group())

def find_neighboring_gears(lines, number):
    y_range = range(
        max(number.pos_y-1, 0),
        min(number.pos_y+2, len(lines))
    )
    
    x_range = range(
        max(number.pos_x - 1, 0),
        min(number.pos_x + len(number.value) + 1, len(lines[0]))
    )

    for y in y_range:
        for x in x_range:
            if lines[y][x] == '*':
                yield GearCoords(x=x, y=y)

def find_gear_powers(lines, part_numbers):
    gear_coords = defaultdict(list)
    for number in part_numbers:
        for gear in find_neighboring_gears(lines, number):
            gear_coords[gear].append(int(number.value))
    for gear, adjacent_numbers in gear_coords.items():
        if len(adjacent_numbers) != 2:
            continue
        yield product(adjacent_numbers)


lines = list(line.strip() for line in sys.stdin)

part_number_coords = find_number_coordinates(lines)

gear_powers = find_gear_powers(lines, part_number_coords)

print(sum(gear_powers))
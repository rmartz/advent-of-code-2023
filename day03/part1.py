import sys
import re
from collections import namedtuple

PartNumber = namedtuple("PartNumber", ["pos_x", "pos_y", "value"])


def find_number_coordinates(lines):
    number_re = re.compile(r"([0-9]+)")

    for line_num, line in enumerate(lines):
        matches = number_re.finditer(line)
        for res in matches:
            yield PartNumber(res.start(), line_num, res.group())

symbol_re = re.compile(".*([^0-9\.]).*")
assert symbol_re.match("..$..")
assert symbol_re.match(".*...")
assert symbol_re.match("%...")
assert symbol_re.match("...^")
assert not symbol_re.match("....")

def has_neighboring_symbol(lines, number):
    y_range = range(
        max(number.pos_y-1, 0),
        min(number.pos_y+2, len(lines))
    )
    
    x_start = max(number.pos_x - 1, 0)
    x_end = min(number.pos_x + len(number.value) + 1, len(lines[0]))

    return any(
        symbol_re.match(lines[y][x_start : x_end])
        for y in y_range
    )


lines = list(line.strip() for line in sys.stdin)

part_number_coords = find_number_coordinates(lines)

matched_numbers = (
    int(number.value) for number in part_number_coords
    if has_neighboring_symbol(lines, number)
)

print(sum(matched_numbers))
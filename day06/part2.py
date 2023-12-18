from math import sqrt, ceil
import sys
from functools import reduce

def calculate_winning_ranges(time, distance):
    # a + b = L
    # a * b >= R

    # a = 0.5 (sqrt(L*L - 4R) + L)
    # a = 0.5 (sqrt(L*L - 4R) - L)
    winning_range = sqrt(time * time - 4 * distance)
    
    if(int(winning_range) == winning_range):
        # We need to beat the record distance - if winning_range is an exact interval, we're tying at the extremes
        winning_range -= 1

    low = (time - winning_range) / 2
    high = (time + winning_range) / 2
    
    return range(int(ceil(low)), int(ceil(high)))

input = (line.strip() for line in sys.stdin)

races = (int(line[10:].replace(" ", "")) for line in input)
time = next(races)
distance = next(races)

winning_range = calculate_winning_ranges(time, distance)

print(len(winning_range))
import sys
import re

input = (line.strip() for line in sys.stdin)

first_digit_re = re.compile(r'^[^0-9]*([0-9])')

calibration_coords = ((
    int(first_digit_re.match(line).group(1) +
    first_digit_re.match(line[::-1]).group(1))
) for line in input)

print(sum(calibration_coords))
import sys
import re

input = (line.strip() for line in sys.stdin)

named_index = {name: str(number) for number, name in enumerate([
    "one", "two", "three","four", "five", "six", "seven", "eight", "nine"
], start=1)}

def reverse_named_digit(digit):
    return named_index.get(digit, digit)


named_digits = "|".join(named_index.keys())
first_digit_re = re.compile(f'([0-9]|{named_digits})')
last_digit_re = re.compile(f'([0-9]|{named_digits[::-1]})')


calibration_coords = ((
    line,
    first_digit_re.findall(line)[0],
    last_digit_re.findall(line[::-1])[0][::-1]
) for line in input)


calibration_digits = [(line, int(
    reverse_named_digit(first_digit) + reverse_named_digit(last_digit)
    )) for line, first_digit,last_digit in calibration_coords]

print(list(calibration_digits))
print(sum(value for _, value in calibration_digits))
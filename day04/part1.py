import sys

def remove_prefix(line, delimiter):
    pos = line.find(delimiter)
    return line[pos + len(delimiter):]

lines = (line.strip() for line in sys.stdin)

cards = (remove_prefix(line, ": ").split("|") for line in lines)

card_numbers = ([(num for num in numbers.split(" ") if num != "") for numbers in card] for card in cards)

matching_winning_numbers = (set(winning_numbers) & set(played_numbers) for winning_numbers, played_numbers in card_numbers)

card_scores = (int(pow(2, len(matches) - 1)) for matches in matching_winning_numbers)

print(sum(card_scores))
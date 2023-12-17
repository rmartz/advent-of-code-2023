import sys
from functools import cache

def remove_prefix(line, delimiter):
    pos = line.find(delimiter)
    return line[pos + len(delimiter):]

lines = (line.strip() for line in sys.stdin)

cards = (remove_prefix(line, ": ").split("|") for line in lines)

card_numbers = ([(num for num in numbers.split(" ") if num != "") for numbers in card] for card in cards)

matching_winning_numbers = (set(winning_numbers) & set(played_numbers) for winning_numbers, played_numbers in card_numbers)

card_scores = list(len(matches) for matches in matching_winning_numbers)

@cache
def get_recursive_card_score(card_num):
    global card_scores

    score = card_scores[card_num]
    return 1 + sum(get_recursive_card_score(card_num + offset + 1) for offset in range(score))

recursive_card_scores = (get_recursive_card_score(i) for i in range(len(card_scores)))

print(sum(recursive_card_scores))
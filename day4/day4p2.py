import re
from dataclasses import dataclass

file = open('day4\input.txt', 'r')
lines = file.readlines()

sum = 0

cards = []

@dataclass
class Card:
    number_wins: int
    number_copies: int

for i, line in enumerate(lines):
    _, winners, nums = re.split(r"[:|] ", line)
    winners = winners.split()
    nums = nums.split()

    numWins = 0
    for n in nums:
        for w in winners:
            if n == w:
                numWins += 1
    
    cards.append(Card(numWins, 1))

for i, card in enumerate(cards):
    sum += card.number_copies
    for j in range(1,card.number_wins + 1):
        cards[i + j].number_copies += card.number_copies


print(cards)
print(sum)
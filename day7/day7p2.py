from dataclasses import dataclass
from collections import Counter
from functools import cmp_to_key

#ranking hands themselves (without comparison to other hands)
def rankHand(cards):
    hCount = Counter(cards)
    #For part 2 just add J values to the highest value in hCount
    if 'J' in hCount.keys() and hCount['J'] != 5:
        # print(hCount)
        #find highest 
        jCount = hCount['J']
        hCount.pop('J')
        try:
            maxCount = max(hCount, key=hCount.get)
        except UnboundLocalError:
            print(jCount)
        hCount[maxCount] += jCount
        # print(hCount)

    #Default High Card
    rank = 1
    #Five of a Kind
    if 5 in hCount.values():
        rank = 7
    #Four of a Kind
    elif 4 in hCount.values():
        rank = 6
    #Full House
    elif 3 in hCount.values() and 2 in hCount.values():
        rank = 5
    #Three of a Kind
    elif 3 in hCount.values():
        rank = 4
    #Two-pair
    elif len([c for c in hCount.values() if c == 2]) == 2:
        rank = 3
    #One Pair
    elif 2 in hCount.values():
        rank = 2
    
    return rank
    
#letter order
order = ['A', 'K', 'Q', 'T', '9', '8', '7', '6', '5', '4', '3', '2', 'J']

def handCompare(hand1, hand2):
    for i in range(len(hand1.cards)):
        if hand1.cards[i] == hand2.cards[i]:
            continue
        if order.index(hand1.cards[i]) < order.index(hand2.cards[i]):
            return 1
        else:
            return -1



@dataclass
class Hand:
    cards: str
    bid: int
    rank: int = 0


file = open('day7\input.txt', 'r')
lines = file.readlines()

hands = []
for line in lines:
    cards, bid = line.split()
    hand = Hand(cards, int(bid), rankHand(cards))
    hands.append(hand)


rerankedHands = []
#separate by rank
for i in range(8):
    sameRank = [x for x in hands if x.rank == i]
    #sort hands 
    sameRank = sorted(sameRank, key=cmp_to_key(handCompare))
    #add new ranked hands to rerankedHands
    rerankedHands += sameRank


# print(rerankedHands)

total = 0

for i in range(len(rerankedHands)):
    total += rerankedHands[i].bid * (i + 1)

print(total)
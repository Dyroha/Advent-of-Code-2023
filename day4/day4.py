import re

file = open('day4\input.txt', 'r')
lines = file.readlines()

sum = 0
for line in lines:
    _, winners, nums = re.split(r"[:|] ", line)
    winners = winners.split()
    nums = nums.split()

    numWins = 0
    for n in nums:
        for w in winners:
            if n == w:
                numWins += 1
    
    if numWins:
        sum += pow(2, numWins - 1)

print(sum)
import numpy as np

file = open('day6\input.txt', 'r')
lines = file.readlines()

def getInput(line):
    _, nums = line.split(":")
    nums = nums.split()
    inp = ""
    for n in nums:
        inp += n
    return inp

time = int(getInput(lines[0]))
distance = int(getInput(lines[1]))
wins = 0

for hold in range(1,time):
    if (time - hold) * hold > distance:
        wins += 1

print(wins)
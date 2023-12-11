import numpy as np

file = open('day6\input.txt', 'r')
lines = file.readlines()

def splitInput(line):
    _, nums = line.split(":")
    return nums.split()

times = list(map(int,splitInput(lines[0])))
distances = list(map(int,splitInput(lines[1])))
wins = []

for i in range(len(times)):
    wins.append(0)
    for hold in range(1,times[i]):
        if (times[i] - hold) * hold > distances[i]:
            wins[i] += 1

print(wins)
print(np.prod(wins))
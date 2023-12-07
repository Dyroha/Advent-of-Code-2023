import re

file = open('day2\input.txt', 'r')
lines = file.readlines()

sum = 0
for line in lines:
    ls = re.split(r'[:;][ ]*', line.strip())
    gameId = ls[0][5:]
    valid = True
    for pick in ls[1:]:
        p = pick.split(', ')
        for cube in p:
            num,color = cube.split()
            num = int(num)
            if ((color == "red" and num > 12) or (color == "green" and num > 13) or (color == "blue" and num > 14)):
                valid = False
                break
    if valid:
        sum += int(gameId)

print(sum)
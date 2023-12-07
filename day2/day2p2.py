import re

file = open('day2\input.txt', 'r')
lines = file.readlines()

sum = 0
for line in lines:
    ls = re.split(r'[:;][ ]*', line.strip())
    r,g,b = 0,0,0
    for pick in ls[1:]:
        p = pick.split(', ')
        for cube in p:
            num,color = cube.split()
            num = int(num)
            if (color == "red" and num > r):
                r = num
            elif (color == "green" and num > g):
                g = num
            elif (color == "blue" and num > b):
                b = num
    sum += r*b*g

print(sum)
file = open('day1\input.txt', 'r')
lines = file.readlines()

total = 0
for line in lines:
    a, b = 0, 0
    for c in line:
        if c.isnumeric():
            a = c
            break
    for c in line[::-1]:
        if c.isnumeric():
            b = c
            break
    total += int(str(a)+str(b))

print(total)
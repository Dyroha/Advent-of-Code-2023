file = open('day1\input.txt', 'r')
lines = file.readlines()

total = 0
for line in lines:
    a, b = 0, 0
    
    #separate all numbers into new list then use the new list
    newLine = []
    for i in range(0,len(line)):
        if line[i].isnumeric():
            newLine.append(line[i])
        elif (line[i:i+3] == "one"):
            newLine.append(1)
            i += 2
        elif (line[i:i+3] == "two"):
            newLine.append(2)
            i += 2
        elif (line[i:i+5] == "three"):
            newLine.append(3)
            i += 4
        elif (line[i:i+4] == "four"):
            newLine.append(4)
            i += 3
        elif (line[i:i+4] == "five"):
            newLine.append(5)
            i += 3
        elif (line[i:i+3] == "six"):
            newLine.append(6)
            i += 2
        elif (line[i:i+5] == "seven"):
            newLine.append(7)
            i += 4
        elif (line[i:i+5] == "eight"):
            newLine.append(8)
            i += 4
        elif (line[i:i+4] == "nine"):
            newLine.append(9)
            i += 3

    a = newLine[0]
    b = newLine[-1]
    total += int(str(a)+str(b))

print(total)
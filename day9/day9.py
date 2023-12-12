file = open("day9/input.txt", "r")
lines = file.readlines()

def findSequence(nums):
    sequence = [nums]
    #do while for finding sequences
    while True:
        last = sequence[-1]
        s = []

        for i in range(len(last)-1):
            s.append(last[i+1] - last[i])

        sequence.append(s)
        try:
            if not any(s):
                break
        except IndexError:
            print(sequence)
            break

    return sequence

def interpolate(differences):
    d = differences[::-1]
    total = 0
    for i in range(len(d)):
        total += d[i][-1]

    return total
        

def stringsToInts(stringList):
    return [int(x) for x in stringList]

total = 0

for line in lines:
    total += interpolate(findSequence(stringsToInts(line.split())))

print(total)

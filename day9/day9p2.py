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
        # print(total, d[i][0])
        total = -total
        # if i % 2 == 0:            
        total += d[i][0]
        # else:
        #     total -= d[i][0]

    return total
        

def stringsToInts(stringList):
    return [int(x) for x in stringList]

total = 0
tests = ["0 3 6 9 12 15", "10 13 16 21 30 45", "1 3 6 10 15 21"]
# for t in tests:
#     print(interpolate(findSequence(stringsToInts(t.split()))))
for line in lines:
    total += interpolate(findSequence(stringsToInts(line.split())))

print(total)

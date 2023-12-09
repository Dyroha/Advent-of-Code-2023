file = open('day5\input.txt', 'r')
lines = file.readlines()

seeds = lines[0].strip("seeds: ").split()

def inRange(source, sourceStart, size):
    return sourceStart <= source <= sourceStart+size

def sourceToDestination(source, destinationStart, sourceStart):
    return destinationStart + source - sourceStart

rounds = []
#split into sections and format
section = -1
for line in lines[1:]:
    if line == "\n":
        continue
    elif line.endswith(":\n"):
        section += 1
    else:
        p = line.split()


#go through stages one by one

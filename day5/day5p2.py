file = open('day5\input.txt', 'r')
lines = file.readlines()

seeds = list(map(int, lines[0].strip("seeds: ").split()))
seeds = [[seeds[i*2],seeds[i*2+1]] for i in range(int(len(seeds)/2))]
bag = map(lambda x: [False,x], seeds)
seeds = list(bag)
print(seeds)


def inRange(source, sourceStart, size):
    return sourceStart <= source <= sourceStart+size

def sourceToDestination(source, destinationStart, sourceStart):
    return destinationStart + source - sourceStart

#split into sections and format
for line in lines[1:]:
    if line == "\n":
        continue
    elif line.endswith(":\n"):
        for seed in seeds:
            seed[0] = False
    else:
        p = list(map(int, line.split()))
        for i in range(len(seeds)):
            if seeds[i][0]:
                continue
            if inRange(seeds[i][1] , p[1], p[2]):
                seeds[i][0] = True
                seeds[i][1], newSeed = sourceToDestination(seeds[i][1], p[0], p[1])
                seeds.append(newSeed)
                
smallest = 931463584
for _,s in seeds:
    if s < smallest:
        smallest = s

print(smallest)

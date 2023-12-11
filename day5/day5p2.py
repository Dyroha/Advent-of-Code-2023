from dataclasses import dataclass

file = open('day5\input.txt', 'r')
lines = file.readlines()

@dataclass
class SeedRange:
    checked: bool
    start: int
    end: int

seeds = list(map(int, lines[0].strip("seeds: ").split()))
print(len(seeds))
seedBag = []
for i in range(int(len(seeds)/2)):
    seedBag.append(SeedRange(False, seeds[i*2], seeds[i*2] + seeds[i*2 + 1]))

print(seedBag)


def move(index, seedBag, range):
    seed = seedBag[i]
    rangeStart = range[1]
    rangeEnd = rangeStart + range[2]
    destinationStart = range[0]
    destinationEnd = destinationStart + range[2]
    #find overlap area
    startIn = False
    endIn = False
    ''' 
    range      <----------------->
    both in    <--startIn--EndIn->
    need to shift whole thing

    one in 
    <----------------->
    <-----------EndIn->
    end from rangeStart
    or
    <----------------->
    <---startIn------->

    

    '''
    if seed.start >= rangeStart:


    #make overlap new SeedRange with True checked
    #take that range off of original range even if that means splitting the thing
    #convert the overlap and append to end of seedBag



#split into sections and format
for line in lines[1:]:
    if line == "\n":
        continue
    elif line.endswith(":\n"):
        for seed in seedBag:
            seed.checked = False
    else:
        p = list(map(int, line.split()))
        for i in range(len(seedBag)):
            if seedBag[i].checked:
                continue
            move(i, seedBag, p)
                
smallest = 931463584
for _,s in seeds:
    if s < smallest:
        smallest = s

print(smallest)

import re

file = open('day3\input.txt', 'r')
lines = file.readlines()

def hasSymbol(string):
    return re.search(r'[^0-9.]', string)

#running total
sum = 0

#add filler for top row
lines.insert(0, "." * (len(lines[0])-1))
lines.append("." * (len(lines[0])-1))
#look at 3 lines at a time, get coord range of all parts on middle line and see if any symbols are adjacent, add part number to sum if adjacent to symbol
for i in range(0,len(lines)-2):
    line1 = lines[i].strip()
    line2 = lines[i+1].strip()
    line3 = lines[i+2].strip()
    
    #get part position ranges
    parts = []
    i = 0
    while i < len(line2):
        bounds = [0,0]
        if line2[i].isnumeric():
            bounds[0] = i
            #increment i until i+1 is not numeric
            while line2[i+1].isnumeric():
                i += 1
                if len(line2) < i+2:
                    break

            bounds[1] = i
            parts.append(tuple(bounds))
        i += 1

    validparts = {()}
    #check each line for symbols in those areas
    for p in parts:
        #line 2
        if(p[0] != 0 and hasSymbol(line2[p[0]-1])):
            validparts.add(p)
        elif (p[1] != (len(line2)-1) and hasSymbol(line2[p[1]+1])):
            validparts.add(p)
        #line 1 and 3
        newRange = (p[0]-1 if p[0] > 0 else p[0], p[1]+1 if p[1] < len(line1) else p[1])
        if(hasSymbol(line1[newRange[0]:newRange[1]+1]) or hasSymbol(line3[newRange[0]:newRange[1]+1])):
            validparts.add(p)
    
    #remove space holder
    validparts.remove(())

    #add all valid parts to sum
    for p in validparts:
        # print(p)
        # print(int(line2[p[0]:p[1]+1]))
        sum += int(line2[p[0]:p[1]+1])


print(sum)
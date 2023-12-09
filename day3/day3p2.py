file = open('day3\input.txt', 'r')
lines = file.readlines()

#running total
sum = 0

#trying something possibly better for p2

#4-tuple number, l, c1, c2 where c1 and c2 are the beginning and end of the number inclusive
nums = set()
#2-tuple of l, c for the line and character of the '*' in the document
stars = set()

#look for all coordiantes of '*' and all number ranges and put into sets
for i,line in enumerate(lines):
    j = 0
    while j < len(line):
        if line[j] == '*':
            stars.add((i,j))
            j += 1
        elif line[j].isnumeric():
            c1 = j
            j += 1
            while (line[j].isnumeric()):
                j += 1
                if(j >= len(line)):
                    break
            nums.add((int(line[c1:j]),i,c1,j-1))
        else:
            j += 1 

sum = 0
#see if '*' has exactly 2 numbers adjacent, multiply them and add them to sum
for s in stars:
    numCount = 0
    adjnums = []
    for n in nums:
        # within line range
        lr = s[0] - 1 <= n[1] <= s[0] + 1
        #within character range
        cr = n[2] - 1 <= s[1] <= n[3] + 1
        if lr and cr:
            adjnums.append(n[0])
            numCount += 1
    if(numCount == 2):
        sum += adjnums[0] * adjnums[1]

print(sum)
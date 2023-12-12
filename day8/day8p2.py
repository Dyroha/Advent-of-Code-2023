from dataclasses import dataclass
from numpy import prod

file = open('day8\input.txt', 'r')
lines = file.readlines()

instructions = lines[0].strip()

@dataclass
class Node:
    name: str
    children: tuple
    leftChild = None
    rightChild = None

def makeNode(line):
    #tidy variables
    name, children = line.split("=")
    leftChild, rightChild = children[2:-2].split(',')
    return Node(name.strip(), [leftChild, rightChild.strip()])

nodes = []
for line in lines[2:]:
    nodes.append(makeNode(line))

for node in nodes:
    l,r = node.children
    lNode = next((x for x in nodes if x.name == l), None)
    rNode = next((x for x in nodes if x.name == r), None)
    if not lNode or not rNode:
        print("Fail at", node.name)
        exit(1)
    node.leftChild = lNode
    node.rightChild = rNode

start = [x for x in nodes if x.name.endswith("A")]
print(start)

zHits = []

for node in start:
    count = 0
    current = node
    zs = []
    while True:
        if instructions[count % len(instructions)] == 'L':
            current = current.leftChild
        else:
            current = current.rightChild

        count += 1
        if current.name.endswith("Z"):
            zs.append((current,count))

        if current == node or count > 100000:
            break

    zHits.append(zs)

diff = []
for zs in zHits:
    diffs = []
    for i in range(len(zs)-1):
        diffs.append(zs[i+1][1] - zs[i][1])
    diff.append(diffs[0])

offsets = [x[0][1] for x in zHits]
print(offsets)
print(diff)

print(prod(diff))
from dataclasses import dataclass

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
    if node.name == "ZZZ":
        continue
    l,r = node.children
    lNode = next((x for x in nodes if x.name == l), None)
    rNode = next((x for x in nodes if x.name == r), None)
    if not lNode or not rNode:
        print("Fail at", node.name)
        exit(1)
    node.leftChild = lNode
    node.rightChild = rNode

start = next((x for x in nodes if x.name == "AAA"), None)
end = next((x for x in nodes if x.name == "ZZZ"), None)

print(start, end)

current = start
count = 0
while current != end:
    if instructions[count % len(instructions)] == 'L':
        current = current.leftChild
    else:
        current = current.rightChild
    count += 1

print(count)

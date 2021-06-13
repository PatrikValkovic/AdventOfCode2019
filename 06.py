#!/usr/bin/env python

with open('input_06.txt', 'r') as f:
    data = f.readlines()
data = list(map(lambda x: x.strip().split(')'), data))


class Node:
    def __init__(self, name):
        self.name = name
        self.to = []
        self.distance = -1
        self.parent = None

root = Node('COM')
nodes = {'COM': root}
for center, around in data:
    if center not in nodes:
        nodes[center] = Node(center)
    if around not in nodes:
        nodes[around] = Node(around)
    nodes[center].to.append(nodes[around])

for node in nodes.values():
    for ch in node.to:
        ch.parent = node

root.distance = 0
to_process = [root]
while len(to_process) != 0:
    current = to_process.pop()
    for ch in current.to:
        ch.distance = current.distance + 1
    to_process.extend(current.to)

print(sum(map(lambda x: x.distance, nodes.values())))

## Part 2
me = nodes['YOU']
santa = nodes['SAN']
from_node = me.parent
to_node = santa.parent
me.distance = -1

from collections import deque

to_process = deque()
to_process.append([from_node, me])
processed = set()

while to_node not in processed and len(to_process) != 0:
    current, get_from = to_process.pop()
    if current in processed:
        continue
    current.distance = get_from.distance + 1
    processed.add(current)
    to_process.append([current.parent, current])
    for ch in current.to:
        to_process.append([ch, current])

print(to_node.distance)


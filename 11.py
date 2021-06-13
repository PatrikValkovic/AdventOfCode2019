#!/usr/bin/env python
import numpy as np
import math

from Comp_09 import Comp

with open('input_11.txt', 'r') as f:
    data = f.readline().strip().split(',')
program = list(map(int, data))

c = Comp(program)
current_pos = (0,0)
direction = (0,1)
field = dict()

while c.simulate() == False:
    while not c.outputs.empty():
        col = c.outputs.get()
        move = c.outputs.get()
        field[current_pos] = col
        if move == 0:  # left
            if direction[0] == 0:
                direction = (-direction[1], 0)
            else:
                direction = (0, direction[0])
        elif move == 1:  # right
            if direction[0] == 0:
                direction = (direction[1], 0)
            else:
                direction = (0, -direction[0])
        current_pos = (current_pos[0] + direction[0], current_pos[1] + direction[1])

    if current_pos in field:
        c.inputs.put(field[current_pos])
    else:
        c.inputs.put(0)


print(len(field.keys()))


# part 2
c = Comp(program)
current_pos = (0,0)
direction = (0,1)
field = dict()
field[(0,0)] = 1

while c.simulate() == False:
    while not c.outputs.empty():
        col = c.outputs.get()
        move = c.outputs.get()
        field[current_pos] = col
        if move == 0:  # left
            if direction[0] == 0:
                direction = (-direction[1], 0)
            else:
                direction = (0, direction[0])
        elif move == 1:  # right
            if direction[0] == 0:
                direction = (direction[1], 0)
            else:
                direction = (0, -direction[0])
        current_pos = (current_pos[0] + direction[0], current_pos[1] + direction[1])

    if current_pos in field:
        c.inputs.put(field[current_pos])
    else:
        c.inputs.put(0)

min_row = np.min(list(map(lambda x: x[0], field.keys())))
max_row = np.max(list(map(lambda x: x[0], field.keys())))
min_column = np.min(list(map(lambda x: x[1], field.keys())))
max_column = np.max(list(map(lambda x: x[1], field.keys())))


identifier = np.zeros((max_row - min_row + 1, max_column - min_column + 1), dtype=int)
for k in field.keys():
    identifier[k[0] - min_row, k[1] - min_column] = field[k]

for r in identifier:
    for c in r:
        print('#' if c == 1 else ' ', end='')
    print()


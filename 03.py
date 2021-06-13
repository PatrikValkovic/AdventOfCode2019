#!/usr/bin/env python
"""
:Author Patrik Valkovic
:Created 05.12.2019 13:33
:Licence MIT
Part of 2019

"""

import math

with open('input_03.txt', 'r') as f:
    paths = f.readlines()
paths = [p.replace('\n', ' ').split(',') for p in paths]

def get_positions(path):
    current = (0, 0)
    over = set()
    for p in path:
        amount = int(p[1:])
        if p[0] == 'R':
            steps = (1, 0)
        elif p[0] == 'L':
            steps = (-1, 0)
        elif p[0] == 'U':
            steps = (0, 1)
        elif p[0] == 'D':
            steps = (0, -1)
        else:
            print(f'Unknown direction {p[0]}')
        for i in range(amount):
            current = (
                current[0] + steps[0],
                current[1] + steps[1]
            )
            over.add(current)
    return over

first_path_pos = get_positions(paths[0])
second_path_pos = get_positions(paths[1])
intersections = list(first_path_pos.intersection(second_path_pos))
s = sorted(intersections, key=lambda x: math.fabs(x[0]) + math.fabs(x[1]))
closest = s[0]
dist = int(math.fabs(closest[0]) + math.fabs(closest[1]))
print(dist)

# part 2
def steps_to_pos(path, pos):
    current = (0, 0)
    s = 0
    for p in path:
        amount = int(p[1:])
        if p[0] == 'R':
            steps = (1, 0)
        elif p[0] == 'L':
            steps = (-1, 0)
        elif p[0] == 'U':
            steps = (0, 1)
        elif p[0] == 'D':
            steps = (0, -1)
        else:
            print(f'Unknown direction {p[0]}')
        for i in range(amount):
            current = (
                current[0] + steps[0],
                current[1] + steps[1]
            )
            s += 1
            if current == pos:
                return s

s = sorted(intersections, key=lambda x: steps_to_pos(paths[0], x) + steps_to_pos(paths[1], x))
closest = s[0]
dist = steps_to_pos(paths[0], closest) + steps_to_pos(paths[1], closest)
print(dist)

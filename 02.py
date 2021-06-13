#!/usr/bin/env python
"""
:Author Patrik Valkovic
:Created 05.12.2019 13:06
:Licence MIT
Part of 2019

"""

import numpy as np

data = []
with open('input_02.txt', 'r') as f:
    data = f.readline().split(',')
data = list(map(int, data))
original_data = np.array(data)

data[1] = 12
data[2] = 2

pos = 0
while data[pos] != 99:
    if data[pos] == 1:
        data[data[pos+3]] = data[data[pos+1]] + data[data[pos + 2]]
    elif data[pos] == 2:
        data[data[pos + 3]] = data[data[pos + 1]] * data[data[pos + 2]]
    else:
        print(f'Cant handle code {data[pos]} at pos {pos}')
    pos += 4

print(data[0])


# Part 2
def part2():
    for i in range(100):
        for j in range(100):
            data = np.copy(original_data)
            data[1] = i
            data[2] = j
            pos = 0
            try:
                while data[pos] != 99:
                    if data[pos] == 1:
                        data[data[pos + 3]] = data[data[pos + 1]] + data[data[pos + 2]]
                    elif data[pos] == 2:
                        data[data[pos + 3]] = data[data[pos + 1]] * data[data[pos + 2]]
                    else:
                        print(f'Cant handle code {data[pos]} at pos {pos}')
                    pos += 4
                if data[0] == 19690720:
                    return (i, j)
            except IndexError:
                pass

noun, verb = part2()
print(noun * 100 + verb)

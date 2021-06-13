#!/usr/bin/env python

import numpy as np

data = []
with open('input_05.txt', 'r') as f:
    data = f.readline().replace('\n', ' ').split(',')
data_original = list(map(int, data))


def simulate(data, input):
    pos = 0
    i = iter(input)
    output = []
    while True:
        instruction = data[pos] % 100
        if instruction == 1:
            par1 = data[pos + 1]
            if data[pos] // 100 % 10 == 0:
                par1 = data[par1]
            par2 = data[pos + 2]
            if data[pos] // 1000 % 10 == 0:
                par2 = data[par2]
            data[data[pos + 3]] = par1 + par2
            pos += 4
        elif instruction == 2:
            par1 = data[pos + 1]
            if data[pos] // 100 % 10 == 0:
                par1 = data[par1]
            par2 = data[pos + 2]
            if data[pos] // 1000 % 10 == 0:
                par2 = data[par2]
            data[data[pos + 3]] = par1 * par2
            pos += 4
        elif instruction == 3:
            data[data[pos + 1]] = next(i)
            pos += 2
        elif instruction == 4:
            par1 = data[pos + 1]
            if data[pos] // 100 % 10 == 0:
                par1 = data[par1]
            output.append(data[data[pos + 1]])
            pos += 2
        elif instruction == 99:
            return output, data
        else:
            print(f'Cant handle code {instruction} at pos {pos}')
            pos += 1

o, d = simulate(np.copy(data_original), [1])
print(o[-1])


# part 2
def simulate2(data, input):
    pos = 0
    i = iter(input)
    output = []
    while True:
        instruction = data[pos] % 100
        if instruction == 1:
            par1 = data[pos + 1]
            if data[pos] // 100 % 10 == 0:
                par1 = data[par1]
            par2 = data[pos + 2]
            if data[pos] // 1000 % 10 == 0:
                par2 = data[par2]
            data[data[pos + 3]] = par1 + par2
            pos += 4
        elif instruction == 2:
            par1 = data[pos + 1]
            if data[pos] // 100 % 10 == 0:
                par1 = data[par1]
            par2 = data[pos + 2]
            if data[pos] // 1000 % 10 == 0:
                par2 = data[par2]
            data[data[pos + 3]] = par1 * par2
            pos += 4
        elif instruction == 3:
            data[data[pos + 1]] = next(i)
            pos += 2
        elif instruction == 4:
            par1 = data[pos + 1]
            if data[pos] // 100 % 10 == 0:
                par1 = data[par1]
            output.append(par1)
            pos += 2
        elif instruction == 5:
            par1 = data[pos + 1]
            if data[pos] // 100 % 10 == 0:
                par1 = data[par1]
            par2 = data[pos + 2]
            if data[pos] // 1000 % 10 == 0:
                par2 = data[par2]
            if par1 != 0:
                pos = par2
            else:
                pos += 3
        elif instruction == 6:
            par1 = data[pos + 1]
            if data[pos] // 100 % 10 == 0:
                par1 = data[par1]
            par2 = data[pos + 2]
            if data[pos] // 1000 % 10 == 0:
                par2 = data[par2]
            if par1 == 0:
                pos = par2
            else:
                pos += 3
        elif instruction == 7:
            par1 = data[pos + 1]
            if data[pos] // 100 % 10 == 0:
                par1 = data[par1]
            par2 = data[pos + 2]
            if data[pos] // 1000 % 10 == 0:
                par2 = data[par2]
            data[data[pos + 3]] = 1 if par1 < par2 else 0
            pos += 4
        elif instruction == 8:
            par1 = data[pos + 1]
            if data[pos] // 100 % 10 == 0:
                par1 = data[par1]
            par2 = data[pos + 2]
            if data[pos] // 1000 % 10 == 0:
                par2 = data[par2]
            data[data[pos + 3]] = 1 if par1 == par2 else 0
            pos += 4
        elif instruction == 99:
            return output, data
        else:
            print(f'Cant handle code {instruction} at pos {pos}')
            pos += 1


o, d = simulate2([3,12,6,12,15,1,13,14,13,4,13,99,-1,0,1,9], [0])
assert o[-1] == 0
o, d = simulate2([3,12,6,12,15,1,13,14,13,4,13,99,-1,0,1,9], [5])
assert o[-1] == 1

o, d = simulate2([3,3,1105,-1,9,1101,0,0,12,4,12,99,1], [0])
assert o[-1] == 0
o, d = simulate2([3,3,1105,-1,9,1101,0,0,12,4,12,99,1], [5])
assert o[-1] == 1

o, d = simulate2(np.copy(data_original), [5])
print(o[-1])


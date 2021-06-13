#!/usr/bin/env python
five = __import__('05')
import copy
import itertools


with open('input_07.txt', 'r') as f:
    program = f.readline()
program = list(map(int, program.split(',')))


phases = itertools.permutations(range(5))
highest = -10e10

for phase in phases:
    to_pass = 0
    for amp in phase:
        output, data = five.simulate2(copy.copy(program), [amp, to_pass])
        to_pass = output[0]
    if to_pass > highest:
        highest = to_pass

print(highest)

# part 2
from queue import Queue

def simulate(data, input: Queue, pos = 0):
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
            data[data[pos + 1]] = input.get()
            pos += 2
        elif instruction == 4:
            par1 = data[pos + 1]
            if data[pos] // 100 % 10 == 0:
                par1 = data[par1]
            pos += 2
            return par1, data, pos
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
            return None
        else:
            print(f'Cant handle code {instruction} at pos {pos}')
            pos += 1


phases = itertools.permutations([5, 6, 7, 8, 9])


highest = -10e10
best_perm = None
for phase in phases:
    states = [
        [copy.copy(program), Queue(), 0] for p in phase
    ]
    inputs = [
        [p] for p in phase
    ]
    inputs[0].append(0)
    for i, s in zip(inputs, states):
        for _ in i:
            s[1].put(_)
    cont = True
    while cont:
        for i in range(5):
            result = simulate(states[i][0], states[i][1], states[i][2])
            if result is None:
                if highest < inputs[0][-1]:
                    highest = inputs[0][-1]
                cont = False
                continue
            output, code, pos = result
            states[i][0] = code
            states[i][2] = pos
            states[(i + 1) % 5][1].put(output)
            inputs[(i + 1) % 5].append(output)

print(highest)

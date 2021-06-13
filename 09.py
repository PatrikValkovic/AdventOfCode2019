#!/usr/bin/env python
import numpy as np
from Comp_09 import Comp

with open('input_09.txt', 'r') as f:
    data = f.readline().strip().split(',')
program = list(map(int, data))

c = Comp(program)
c.inputs.put(1)
c.simulate()
while not c.outputs.empty():
    print(c.outputs.get())


# part2
c = Comp(program)
c.inputs.put(2)
c.simulate()
while not c.outputs.empty():
    print(c.outputs.get())


#!/usr/bin/env python
"""
:Author Patrik Valkovic
:Created 05.12.2019 13:59
:Licence MIT
Part of 2019

"""

import numpy as np

lower = 136818
upper = 685979
valid = set()

for p in np.arange(lower, upper + 1):
    are_same = False
    decrease = False
    in_str = str(p)
    digits = list(map(int, in_str))

    for f, d in zip(digits, digits[1:]):
        if f == d:
            are_same = True
        if d < f:
            decrease = True

    if are_same == False or decrease == True:
        continue

    valid.add(p)
print(len(valid))

# part 2
next_valid = set()
for p in valid:
    pairs = set()
    in_str = str(p)
    digits = list(map(int, in_str))
    for f, s in zip(digits, digits[1:]):
        if f == s:
            pairs.add(f)
    exactly_two = False
    for pair in pairs:
        if digits.count(pair) == 2:
            exactly_two = True
    if exactly_two:
        next_valid.add(p)
print(len(next_valid))


#!/usr/bin/env python
import numpy as np
import math

with open('input_10.txt', 'r') as f:
    data = f.readlines()
field = list(map(lambda l: l.strip(), data))
asteroids = np.array(list(
    map(lambda r: list(map(lambda ch: ch == '#', r)), field)
))


def detects(asteroids, pos_r, pos_c) -> list:
    detected = []
    for r in range(asteroids.shape[0]):
        for c in range(asteroids.shape[1]):
            if r == pos_r and c == pos_c:
                continue
            if asteroids[r, c] == False:
                continue
            row_span = r - pos_r
            col_span = c - pos_c
            gcd = math.gcd(row_span, col_span)
            row_span //= gcd
            col_span //= gcd
            can_detect = True
            for mult in np.arange(start=1, stop=gcd, dtype=int):
                if asteroids[pos_r + mult * row_span, pos_c + mult * col_span] == True:
                    can_detect = False
            if can_detect:
                detected.append((r, c))
    return detected


max_detect = -1
best_pos = (-1, -1)
for r in range(asteroids.shape[0]):
    for c in range(asteroids.shape[1]):
        if asteroids[r, c] == True:
            detected = len(detects(asteroids, r, c))
            if detected > max_detect:
                max_detect = detected
                best_pos = (r, c)

print(max_detect)

#part2

def sorting_method(pos):
    in_degree = np.rad2deg(math.atan2(- pos[0] + best_pos[0], pos[1] - best_pos[1]))
    moved = (360 - in_degree + 90) % 360
    return moved

asteroids[best_pos[0], best_pos[1]] = False
destroyed = []
while asteroids.any().any():
    detected = detects(asteroids, *best_pos)
    det_sort = sorted(detected, key=sorting_method)
    destroyed.extend(det_sort)
    for pos_r, pos_c in detected:
        asteroids[pos_r, pos_c] = False

print(destroyed[199][1] * 100 + destroyed[199][0])



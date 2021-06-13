#!/usr/bin/env python
import numpy as np

with open('input_08.txt', 'r') as f:
    data = f.readline().strip()
nums = list(map(int, data))


WIDTH = 25
HEIGHT = 6
layers = np.array(nums).reshape((-1, HEIGHT, WIDTH), order='C')
zeros = (layers == 0).sum(axis=2).sum(axis=1)
ones = (layers == 1).sum(axis=2).sum(axis=1)
twos = (layers == 2).sum(axis=2).sum(axis=1)
most_zeros = np.argmin(zeros)

print(ones[most_zeros] * twos[most_zeros])

# part 2

img = np.zeros(shape=(HEIGHT, WIDTH))
img[:,:] = 2

for layer in range(layers.shape[0]-1, -1, -1):
    for row in range(HEIGHT):
        for col in range(WIDTH):
            if layers[layer, row, col] != 2:
                img[row, col] = layers[layer, row, col]
img = img.astype(int)

for row in range(HEIGHT):
    for col in range(WIDTH):
        print('X' if img[row, col] == 1 else ' ', end='')
    print()

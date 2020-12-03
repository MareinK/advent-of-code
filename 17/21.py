import itertools

import numpy as np


def parse(inp):
    return np.array(list(map(list, inp.split('/')))) == '#'


def trans(a):
    for flip in [a, np.fliplr(a)]:
        for k in range(4):
            yield np.rot90(flip, k)


grids = [map(parse, l.split(' => ')) for l in open('21.txt').read().splitlines()]
rules = {tuple(t.flatten()): b for a, b in grids for t in trans(a)}

grid = np.array([[False, True, False], [False, False, True], [True, True, True]])

iterations = 18

for _ in range(iterations):
    n = grid.shape[0]
    k = 2 if n % 2 == 0 else 3
    new_n = n + n // k
    new_grid = np.zeros((new_n, new_n), dtype=bool)
    for x, y in itertools.product(range(n // k), repeat=2):
        xslice = slice(x * k, (x + 1) * k)
        yslice = slice(y * k, (y + 1) * k)
        square = grid[xslice, yslice]
        new_xslice = slice(x * (k + 1), (x + 1) * (k + 1))
        new_yslice = slice(y * (k + 1), (y + 1) * (k + 1))
        new_grid[new_xslice, new_yslice] = rules[tuple(square.flatten())]
    grid = new_grid

count = grid.sum()

print(count)
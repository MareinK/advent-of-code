import json

import numpy as np

data = json.load(open('infi.txt'))
flats = {x: y for x, y in data['flats']}

x = data['flats'][0][0]
jumps = []
while x != data['flats'][-1][0]:
    dists = {
        fx: dx
        for fx in flats
        if 0 < (dx := fx - x) - 1 + max(0, flats[fx] - flats[x]) <= 4
    }
    nx = max(dists, key=lambda x: (dists[x], x))
    jumps.append([nx - x - 1, max(0, flats[nx] - flats[x])])
    print(x, dists, nx)
    x = nx


print(jumps)
print(sum(x + y for x, y in jumps))

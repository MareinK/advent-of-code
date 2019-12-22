from itertools import cycle, islice

import numpy as np

v = np.array(list(map(int, open('16.txt').read())))
p = np.array(
    [
        list(islice(cycle(np.repeat([0, 1, 0, -1], i + 1)), 1, len(v) + 1))
        for i in range(len(v))
    ]
)
phase = lambda n: v if n == 0 else np.mod(np.abs(np.matmul(p, phase(n - 1))), 10)
print(''.join(map(str, phase(100)[:8])))

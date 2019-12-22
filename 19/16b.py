from math import comb
from operator import mul

s = open('16.txt').read()
k = int(s[:7])
assert k >= len(s) // 2  # true for my input, wrong answer otherwise
t = (10000 * list(map(int, s)))[k:]
x = [comb(99 + i, 99) for i in range(len(t))]
print(''.join(map(str, (sum(map(mul, x[: len(t) - i], t[i:])) % 10 for i in range(8)))))

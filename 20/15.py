ns = list(map(int, open("15.txt").read().split(",")))
for k in (2020, 30000000):
    seen = {n: i for i, n in enumerate(ns[:-1])}
    prv = ns[-1]
    for i in range(len(ns), k):
        nxt = i - 1 - seen[prv] if prv in seen else 0
        seen[prv] = i - 1
        prv = nxt
    print(prv)

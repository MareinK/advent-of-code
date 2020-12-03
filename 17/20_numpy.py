import collections
import re

import numpy

n = '(-?\d*)'
pat = re.compile(f'p=<{n},{n},{n}>, v=<{n},{n},{n}>, a=<{n},{n},{n}>')
particles = numpy.array([list(map(int, pat.match(l).groups())) for l in open('20.txt')])
remaining = set(range(len(particles)))


def collisions():
    positions = collections.defaultdict(set)
    for i, p in enumerate(particles):
        if i in remaining:
            positions[tuple(p[:3])].add(i)
    return [ids for ids in positions.values() if len(ids) > 1]


particles[:, 3:6] += particles[:, 6:9]

k = 100
for _ in range(k):
    remaining -= {i for ids in collisions() for i in ids}
    particles[:, :6] += particles[:, -6:]

print(len(remaining))
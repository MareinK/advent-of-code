import collections
import itertools
import re

import sympy

n = '(-?\d*)'
pat = re.compile(f'p=<{n},{n},{n}>, v=<{n},{n},{n}>, a=<{n},{n},{n}>')
values = [list(map(int, pat.match(l).groups())) for l in open('20.txt')]
particles = set(sympy.ImmutableMatrix(vals).reshape(3, 3) for vals in values)

M1 = sympy.MatrixSymbol('M1', 3, 3)
M2 = sympy.MatrixSymbol('M2', 3, 3)
t = sympy.symbols('t', integer=True, positive=True)
T = sympy.Matrix([[1, t, t * (t + 1) / 2]])
expr = sum(T * (M1 - M2))

collisions = collections.defaultdict(list)

# find first collisions between all pairs of particles
for p1, p2 in itertools.combinations(particles, 2):
    times = sympy.solvers.solve(expr.subs({M1: p1, M2: p2}), simplify=False)
    if times:
        collisions[min(times)].append({p1, p2})

# go through collisions in temporal order and remove both involved particles if they both still exist
for _, colls in sorted(collisions.items()):
    particles -= {x for coll in colls for x in coll if coll <= particles}

result = len(particles)
print(result)
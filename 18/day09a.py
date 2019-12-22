import collections
import re

DAY = 9

MAGIC = 23
JUMP = -7

def parse(line):
    return tuple(map(int, re.findall(r'\d+', line)))

def solve(data):
    n, k = data

    scores = collections.defaultdict(int)
    marbles = collections.deque([0])
    for i in range(1, k + 1):
        if i % MAGIC == 0:
            marbles.rotate(-JUMP)
            scores[i % n] += i + marbles.pop()
            marbles.rotate(-1)
        else:
            marbles.rotate(-1)
            marbles.append(i)

    return max(scores.values())

lines = open(f'day{DAY:02d}.txt').read().splitlines()
data = [parse(l) for l in lines]
answer = solve(data[0])
print(answer)
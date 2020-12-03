weakened = set()
infected = set()
flagged = set()

data = open('22.txt').read().splitlines()

for y, row in enumerate(data):
    for x, c in enumerate(row):
        if c == '#':
            infected.add((x, y))

pos = len(data[0]) // 2, len(data) // 2
dir = 0, -1
n = 10000000
count = 0

for _ in range(n):
    if pos in weakened:
        weakened.remove(pos)
        infected.add(pos)
        count += 1
    elif pos in infected:
        infected.remove(pos)
        flagged.add(pos)
        dir = -dir[1], dir[0]
    elif pos in flagged:
        flagged.remove(pos)
        dir = -dir[0], -dir[1]
    else:
        weakened.add(pos)
        dir = dir[1], -dir[0]
    pos = pos[0] + dir[0], pos[1] + dir[1]

print(count)
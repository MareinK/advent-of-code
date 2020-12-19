import copy
import itertools

directions = ((1, 0), (1, 1), (0, 1), (-1, 1), (-1, 0), (-1, -1), (0, -1), (1, -1))

state = list(map(list, open("11.txt").read().splitlines()))
dim_x, dim_y = len(state), len(state[0])

while True:
    new_state = copy.deepcopy(state)
    for x, y in itertools.product(range(dim_x), range(dim_y)):
        neighbors = 0
        for dx, dy in directions:
            nx, ny = x, y
            while 0 <= (nx := nx + dx) < dim_x and 0 <= (ny := ny + dy) < dim_y:
                if state[nx][ny] == "L":
                    break
                if state[nx][ny] == "#":
                    neighbors += 1
                    break
        if state[x][y] == "L" and neighbors == 0:
            new_state[x][y] = "#"
        if state[x][y] == "#" and neighbors >= 5:
            new_state[x][y] = "L"
    if repr(state) == repr(new_state):
        break
    state = new_state

print(sum(line.count("#") for line in state))

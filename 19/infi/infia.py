import json

import numpy as np

data = json.load(open('infi.txt'))
flats = {x: y for x, y in data['flats']}
jumps = data['sprongen']

assert list(flats) == sorted(list(flats))

x, y = data['flats'][0]
print(x, y)
for step, (dx, dy) in enumerate(jumps, 1):
    assert 0 <= dx + dy <= 4
    x += dx + 1
    y += dy
    print([dx, dy], [x, y], flats.get(x))
    if x in flats and flats[x] <= y:
        y = flats[x]
    else:
        print(step)
        break
else:
    assert [x, y] == data['flats'][-1]
    print(0)


# for i in range(max(flats.keys()) + 1):
#     print(('X' * flats.get(i, 0)).ljust(40))


# data = json.load(open('infi.txt'))
# flats_dict = {x - 1: y for x, y in data['flats']}  # make flat positions 0-indexed
# flats = np.array(
#     [flats_dict.get(i, 0) for i in range(max(flats_dict.keys()) + 1)]
# )  # at each position, height of flat or 0 if no flat
# jumps = np.array(data['sprongen'])

# x_delta = jumps[:, 0]
# y_delta = jumps[:, 1]

# x_delta += 1  # each step move one right
# x_pos = np.concatenate(
#     ([0], np.cumsum(x_delta))
# )  # cumulative steps are x positions, concat with initial pos
# x_pos += data['flats'][0][0] - 1  # start at x position of first flat (0-indexed)

# flat_height = flats[x_pos]  # heights of visited flats
# height_diff = np.diff(flat_height)  # differences between consecutive visited flats

# # a step is a failure if there is no flat or if the jump does not bridge the height difference
# failure = np.logical_or(flat_height[1:] == 0, y_delta < height_diff)

# if any(failure):
#     print(np.where(failure)[0][0] + 1)  # first failure step, 1-indexed
# else:
#     print(0)

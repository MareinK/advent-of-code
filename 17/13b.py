layers = dict(map(int, l.split(':')) for l in open('13.txt'))

nlayers = max(layers) + 1
lengths = {i: 2*n - 2 for i, n in layers.items()}

start = -1
caught = True
while caught:
    start += 1
    caught = False

    for i in range(nlayers):
        if i in layers and (start + i == 0 or (start + i) % lengths[i] == 0):
            caught = True

print(start)

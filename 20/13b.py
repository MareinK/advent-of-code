import operator

vals = [
    [i, int(v)]
    for i, v in enumerate(open("13.txt").read().splitlines()[1].split(","))
    if v != "x"
]

print(vals)
exit()

start = 100000000000000
max_i, max_val = max(vals, key=operator.itemgetter(1))
offset = max_i + start % max_val

time = start - offset
while True:
    if all((time + i) % val == 0 for i, val in vals):
        break
    time += max_val

print(time)

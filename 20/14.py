import collections
import itertools
import re

instructions = open("14.txt").readlines()

# part 1
memory = collections.defaultdict(int)
for instruction in instructions:
    if m := re.match(r"mask = ([01X]*)", instruction):
        mask_and = int(m[1].translate(str.maketrans("01X", "011")), 2)
        mask_or = int(m[1].translate(str.maketrans("01X", "010")), 2)
    if m := re.match(r"mem\[(\d*)\] = (\d*)", instruction):
        memory[int(m[1])] = int(m[2]) & mask_and | mask_or
print(sum(memory.values()))

# part 2
memory = collections.defaultdict(int)
for instruction in instructions:
    if m := re.match(r"mask = ([01X]*)", instruction):
        mask_and = int(m[1].translate(str.maketrans("01X", "110")), 2)
        mask_or = int(m[1].translate(str.maketrans("01X", "010")), 2)
        masks_or = list(
            map(
                sum,
                itertools.chain.from_iterable(
                    itertools.combinations(
                        [2 ** i for i, c in enumerate(reversed(m[1])) if c == "X"], r
                    )
                    for r in range(m[1].count("X") + 1)
                ),
            )
        )
    if m := re.match(r"mem\[(\d*)\] = (\d*)", instruction):
        for mask in masks_or:
            memory[int(m[1]) & mask_and | mask_or | mask] = int(m[2])
print(sum(memory.values()))

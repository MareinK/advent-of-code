import functools
import itertools
import operator
import re

# input
data = open("16.txt").read()
fields = {
    name: ((int(a1), int(b1)), (int(a2), int(b2)))
    for name, a1, b1, a2, b2 in re.findall(r"(.*): (.*)-(.*) or (.*)-(.*)", data)
}
your_ticket = tuple(
    int(x) for x in re.search(r"your ticket:\n(.*)", data).group(1).split(",")
)
nearby_tickets = {
    tuple(int(x) for x in t.split(","))
    for t in re.search(r"nearby tickets:\n((?:.*\n?)*)", data).group(1).split("\n")
}

# preprocess
fields_valid_values = {
    name: set(itertools.chain(range(a1, b1 + 1), range(a2, b2 + 1)))
    for name, ((a1, b1), (a2, b2)) in fields.items()
}
all_valid_values = set(itertools.chain(*fields_valid_values.values()))

# part 1
print(
    sum(
        filter(
            lambda value: value not in all_valid_values,
            itertools.chain(*nearby_tickets),
        )
    )
)

# part 2
actual_values = tuple(
    map(
        set,
        zip(
            *filter(
                lambda ticket: all(value in all_valid_values for value in ticket),
                nearby_tickets,
            )
        ),
    )
)

fields_index_candidates = {
    name: set(
        filter(
            lambda i: actual_values[i] <= fields_valid_values[name],
            range(len(fields)),
        )
    )
    for name in fields
}

fields_index = {}
for name, index_candidates in sorted(
    fields_index_candidates.items(), key=operator.itemgetter(1)
):
    index = next(iter(index_candidates - set(fields_index.values())))
    fields_index[name] = index

print(
    functools.reduce(
        operator.mul,
        map(
            lambda name: your_ticket[fields_index[name]],
            filter(lambda name: "departure" in name, fields),
        ),
    )
)

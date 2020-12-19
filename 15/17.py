import itertools

ns = list(map(int, open("17.txt")))

print(
    len(
        list(
            filter(
                lambda n: n == 150,
                map(
                    sum,
                    itertools.chain.from_iterable(
                        itertools.combinations(ns, r) for r in range(len(ns) + 1)
                    ),
                ),
            )
        )
    )
)

minlen = min(
    map(
        len,
        filter(
            lambda ns: sum(ns) == 150,
            itertools.chain.from_iterable(
                itertools.combinations(ns, r) for r in range(len(ns) + 1)
            ),
        ),
    )
)

print(
    len(
        list(
            filter(
                lambda ns: sum(ns) == 150 and len(ns) == minlen,
                itertools.chain.from_iterable(
                    itertools.combinations(ns, r) for r in range(len(ns) + 1)
                ),
            )
        )
    )
)
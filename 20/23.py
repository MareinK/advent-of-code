import collections
import math


def play(cups, n):
    links = [None] * (len(cups) + 1)
    for c1, c2 in zip(cups, cups[1:] + [cups[0]]):
        links[c1] = c2
    max_num = max(cups)

    current = cups[0]

    for _ in range(n):
        pick1 = links[current]
        pick2 = links[pick1]
        pick3 = links[pick2]

        destination = max_num if current == 1 else current - 1
        while destination == pick1 or destination == pick2 or destination == pick3:
            destination = max_num if destination == 1 else destination - 1

        nxt = links[pick3]
        links[current], links[destination], links[pick3] = (
            nxt,
            pick1,
            links[destination],
        )
        current = nxt

    result = [1]
    while len(result) < len(cups):
        result.append(links[result[-1]])

    return result


# parts 1 + 2
cups = list(map(int, open("23.txt").read()))
print("".join(map(str, play(cups, 100)[1:])))
print(math.prod(play(cups + list(range(10, 1000001)), 10000000)[1:3]))

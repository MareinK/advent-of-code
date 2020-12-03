import collections

Part = collections.namedtuple('Part', ['a', 'b', 's'])
PartEnd = collections.namedtuple('PartEnd', ['part', 'end'])


def parse(l):
    a, b = map(int, l.split('/'))
    return a, b, a + b


parts = {Part(*parse(l)) for l in open('24.txt')}
starts = {part for part in parts if 0 in part}
supports = collections.defaultdict(set)
for part in parts:
    supports[part.a].add(part)
    supports[part.b].add(part)


def get_bridges(partends):
    successors = supports[partends[-1].end] - set(part for part, _ in partends)
    result = [partends]
    for succ in successors:
        next_end = succ.a if succ.b == partends[-1].end else succ.b
        next_partends = partends + [PartEnd(succ, next_end)]
        for bridge in get_bridges(next_partends):
            result.append(bridge)
    return result


all_bridges = [
    bridge for start in starts for bridge in get_bridges([PartEnd(start, start.a if start.b == 0 else start.b)])]

scores = [(len(bridge), sum(s for (_, _, s), _ in bridge)) for bridge in all_bridges]
result = max(scores)[0]

print(result)
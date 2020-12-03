import collections
import re

Entry = collections.namedtuple('Entry', ['name', 'weight', 'children'])
pattern = re.compile('(\w*) \((\w*)\)(?: -> (.*))?')

groups = [pattern.match(line).groups() for line in open('7.txt').readlines()]
entries = [Entry(n, int(w), c.split(', ') if c else []) for n, w, c in groups]

programs = dict()
nobottom = set()
for entry in entries:
    programs[entry.name] = entry
    for child in entry.children:
        nobottom.add(child)

bottoms = set(programs) - nobottom
assert(len(bottoms) == 1)
bottom = bottoms.pop()

weights = dict()

def get_weight(name):
    global weights
    if name in weights:
        return weights[name]
    program = programs[name]
    ws = [get_weight(c) for c in program.children]
    weight = sum(ws) + program.weight
    weights[name] = weight
    return weight

get_weight(bottom)

def wrong_program(name):
    global weights
    program = programs[name]
    counter = collections.Counter(weights[c] for c in program.children)
    counter2 = collections.Counter((weights[c], c) for c in program.children)
    print(name, counter)
    if not counter or min(counter.values()) != 1:
        return None, name
    else:
        nm = max(counter2.items())[0][1]
        g, w = wrong_program(nm)
        if g:
            return g, w
        else:
            return programs[w].weight + counter.most_common()[0][0] - counter.most_common()[-1][0], w

good, wrong = wrong_program(bottom)

print(good)
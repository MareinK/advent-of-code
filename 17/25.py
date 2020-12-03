import collections
import re

start_pat = re.compile('Begin in state (\w).')
steps_pat = re.compile('Perform a diagnostic checksum after (\d+) steps.')
state_pat = re.compile('''In state (\w):\n((?:.*\n?){8})''')
trans_pat = re.compile('''\s*If the current value is (\d)+:
\s*- Write the value (\d)+.
\s*- Move one slot to the (\w+).
\s*- Continue with state (\w+).''')

inp = open('25.txt').read()

state = start_pat.search(inp).groups()[0]
steps = int(steps_pat.search(inp).groups()[0])
trans = {(s, int(v)): (int(w), 1 if 'r' in m else -1, n) for s, t in state_pat.findall(inp) for v, w, m, n in trans_pat.findall(t)}

tape, cursor = collections.defaultdict(int), 0
for _ in range(steps):
    tape[cursor], m, state = trans[(state, tape[cursor])]
    cursor += m

checksum = sum(tape.values())
print(checksum)
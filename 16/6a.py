import collections
messages = [list(line.strip()) for line in open('6.txt')]
counters = [collections.Counter(col) for col in zip(*messages)]
answer = ''.join([c.most_common(1)[0][0] for c in counters])
print(answer)

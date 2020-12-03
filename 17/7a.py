import collections

digits = collections.deque(int(d) for d in open('1.txt').read())
shift = 1
others = digits.copy()
others.rotate(shift)
matches = [x for x, y in zip(digits, others) if x == y]
result = sum(matches)

print(result)
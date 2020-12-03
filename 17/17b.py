import collections

steps = int(open('17.txt').read())
n = 50_000_000
lock = collections.deque([0])

result = None

for i in range(1, n + 1):
    lock.rotate(-steps)
    if lock[-1] == 0:
        result = i
    lock.append(i)

print(result)

import queue
import string

maze = open('19.txt').read().splitlines()
all_letters = set(x for row in maze for x in row if x in string.ascii_uppercase)
# all_letters = set(list(all_letters)[:2])  # can be used to test with a few letters

def val(x, y):
    try:
        return maze[y][x]
    except IndexError:
        return ' '

frontier = queue.Queue()
frontier.put((maze[0].index('|'), 0, 0, 1, frozenset(), 1))
seen = set()
steps = None

while not frontier.empty():
    x, y, dx, dy, letters, steps = frontier.get()
    if (x, y, letters) in seen:
        continue
    seen.add((x, y, letters))
    if val(x, y) in string.ascii_uppercase:
        letters |= {val(x, y)}
    if letters == all_letters:
        break
    for ndx, ndy in [(dx, dy), (dy, dx), (-dy, -dx)]:
        nx, ny = x + ndx, y + ndy
        if val(nx, ny) != ' ':
            frontier.put((nx, ny, ndx, ndy, letters, steps + 1))

print(steps)
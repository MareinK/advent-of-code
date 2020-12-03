import string

maze = [list(row) for row in open('19.txt').read().splitlines()]

x, y = maze[0].index('|'), 0
dx, dy = (0, 1)


def val(x, y):
    try:
        return maze[y][x]
    except IndexError:
        return ' '


letters = ''

while True:
    v = val(x, y)
    if v == ' ':
        break
    if v in string.ascii_uppercase:
        letters += v
    if v == '+':
        if val(x + dy, y + dx) is not ' ':
            dx, dy = dy, dx
        elif val(x - dy, y - dx) is not ' ':
            dx, dy = -dy, -dx
    x += dx
    y += dy

print(letters)
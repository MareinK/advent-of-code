instructions = open('1.txt').read().split(', ')
x,y,dir = 0,0,0
for instruction in instructions:
  r, d = instruction[0], int(instruction[1:])
  dir = (dir + {'L':-1, 'R':1}[r]) % 4
  x += d * {0: 0, 1: 1, 2: 0, 3: -1}[dir]
  y += d * {0: 1, 1: 0, 2: -1, 3: 0}[dir]
print(abs(x)+abs(y))

import math
instructions = open('1.txt').read().split(', ')
x,y,dir = 0,0,0
visited = set()
def visit(x,y):
  if (x,y) in visited:
    print(abs(x)+abs(y))
    exit()
  visited.add((x,y))
def moveto(newx,newy):
  if y == newy:
    for i in range(x,newx,int(math.copysign(1,newx+1-x))):
      visit(i,y)
  if x == newx:
    for j in range(y,newy,int(math.copysign(1,newy+1-y))):
      visit(x,j)
  return newx,newy
for instruction in instructions:
  r, d = instruction[0], int(instruction[1:])
  dir = (dir + {'L':-1, 'R':1}[r]) % 4
  newx = x + d * {0: 0, 1: 1, 2: 0, 3: -1}[dir]
  newy = y + d * {0: 1, 1: 0, 2: -1, 3: 0}[dir]
  moveto(newx,newy)
  x,y = newx, newy

instructions = [line.strip() for line in open('2.txt')]
x,y = 0,0
keys = [['5','X','2','X','1'],
        ['X','6','X','3','X'],
        ['A','X','7','X','4'],
        ['X','B','X','8','X'],
        ['D','X','C','X','9']]
answer = ''
for line in instructions:
  for c in line:
    newx = x+{'U':1, 'D':-1, 'L':-1, 'R':1}[c]
    newy = y+{'U':-1, 'D':1, 'L':-1, 'R':1}[c]
    x,y = (newx,newy) if 0 <= newx < 5 and 0 <= newy < 5 else (x,y)
  answer += keys[y][x]
print(answer)

instructions = [line.strip() for line in open('2.txt')]
x,y = 1,1
restrict = lambda x: min(max(x,0),2)
keys = [['1','2','3'],['4','5','6'],['7','8','9']]
answer = ''
for line in instructions:
  for c in line:
    x = restrict(x+{'U':0, 'D':0, 'L':-1, 'R':1}[c])
    y = restrict(y+{'U':-1, 'D':1, 'L':0, 'R':0}[c])
  answer += keys[y][x]
print(answer)

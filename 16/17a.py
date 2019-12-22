import hashlib, queue

SIZE = 4,4

def search(start_state,get_successors,is_goal):
  visited = set()
  frontier = queue.Queue()
  frontier.put(start_state)
  while not frontier.empty():
    state = frontier.get()
    if state in visited: continue
    visited.add(state)
    if is_goal(state):
      return state
    for successor in get_successors(state):
      frontier.put(successor)
      
def get_successors(state):
  x,y,s,m = state
  for i,xd,yd,c in [(0,0,-1,'U'),(1,0,1,'D'),(2,-1,0,'L'),(3,1,0,'R')]:
    if 0 <= x+xd < SIZE[0] and 0 <= y+yd < SIZE[1]:
      if m.hexdigest()[i] in 'bcdef':
        n = m.copy()
        n.update(c.encode('UTF-8'))
        yield x+xd,y+yd,s+c,n
  
def is_goal(state):
  x,y,_,_ = state
  return (x,y) == (SIZE[0]-1,SIZE[1]-1)
      
code = open('17.txt').read()
m = hashlib.md5()
m.update(code.encode('UTF-8'))
r = search((0,0,'',m),get_successors,is_goal)
print(r[2])

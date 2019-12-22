import collections, hashlib, queue

State = collections.namedtuple('State',['pos','goals','steps'])
State.__eq__ = lambda self,other: (self.pos,self.goals) == (other.pos,other.goals)
State.__ne__ = lambda self,other: not self.__eq__(other)
State.__hash__ = lambda self: hash((self.pos,self.goals))

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
  x,y = state.pos
  for dx,dy in [(0,1),(0,-1),(1,0),(-1,0)]:
    if maze[x+dx,y+dy] != '#':
      newgoals = set(state.goals)
      if is_int(maze[x+dx,y+dy]):
        newgoals = newgoals.union(set([int(maze[x+dx,y+dy])]))
      newstate = State((x+dx,y+dy),tuple(newgoals),state.steps+1)
      yield newstate
  
def is_goal(state):
  return set(state.goals) == goals

def is_int(x):
  try:
    int(x)
    return True
  except:
    return False

goals = set()
maze = collections.defaultdict(lambda: '#')
for i,line in enumerate(open('24.txt')):
  for j,c in enumerate(line.strip()):
    maze[(j,i)] = c
    if is_int(c):
      goals.add(int(c))
      if int(c) == 0:
        startpos = (j,i)

state = State(startpos,tuple([0]),0)
r = search(state,get_successors,is_goal)

print(r.steps)

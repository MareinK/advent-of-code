import queue

number = int(open('13.txt').read())

GOAL_STATE = (31,39)

def heuristic(state):
  return sum(abs(a-b) for a,b in zip(state,GOAL_STATE))

def path_search(start_state,get_successors,is_goal):
  visited = set()
  frontier = queue.PriorityQueue()
  frontier.put((0,start_state,0))
  while not frontier.empty():
    _,state,pathlen = frontier.get()
    if state in visited: continue
    visited.add(state)
    for successor in get_successors(state,pathlen):
      frontier.put((pathlen + heuristic(successor) + 1,successor,pathlen + 1))
  return visited
  
def is_goal(state):
  return False

def wall(state):
  x,y = state
  if x < 0 or y < 0:
    return True
  value = x*x + 3*x + 2*x*y + y + y*y + number
  return "{0:b}".format(value).count('1') % 2 == 1

def get_successors(state,pathlen):
  if pathlen != 50:
    x,y = state
    for dx,dy in [(1,0),(0,1),(-1,0),(0,-1)]:
      new_state = (x+dx,y+dy)
      if not wall(new_state):
        yield new_state

start_state = (1,1)

result = path_search(start_state,get_successors,is_goal)
print(len(result))

import collections, itertools, queue, copy, re

MIN_FLOOR, MAX_FLOOR, END_FLOOR = 0,3,3
MAX_CARRY = 2
State = collections.namedtuple('State',['elevator','floors'])

# hack to get PriorityQueue working...
State.__lt__ = lambda *x, **y: 0
State.__gt__ = lambda *x, **y: 0
State.__le__ = lambda *x, **y: 0
State.__ge__ = lambda *x, **y: 0

State.__hash__ = lambda state: hash(state.elevator) ^ hash(tuple(tuple(sorted(state.floors[floor])) for floor in sorted(state.floors)))

def load_start_state():
  data = open('11.txt').readlines()
  floornames = {'first':0,'second':1,'third':2,'fourth':3}
  floor_pattern = re.compile(r'The (\S+) floor contains (.*).')
  item_pattern = re.compile(r'(?:(\w*)(?:-compatible)? (generator|microchip))')

  state = State(0,collections.defaultdict(set))

  for line in data:
    floorname,itemnames = floor_pattern.search(line).groups()
    floor = floornames[floorname]
    for name,kind in item_pattern.findall(itemnames):
      item = '{}_{}'.format(kind[0],name)
      state.floors[floor].add(item)
  return state

def heuristic(state):
  value = 0
  for floor,items in state.floors.items():
    value += (END_FLOOR-floor)*len(items)
  return value*3 # faking a consitent heuristic

def path_search(start_state,get_successors,is_goal):
  visited = set()
  frontier = queue.PriorityQueue()
  frontier.put((0,start_state,0))
  while not frontier.empty():
    _,state,pathlen = frontier.get()
    if state in visited: continue
    visited.add(state)
    if is_goal(state):
      return state,pathlen
    for successor in get_successors(state):
      frontier.put((pathlen + heuristic(successor) + 1,successor,pathlen + 1))
  
def is_goal(state):
  return all(i==END_FLOOR or not items for i,items in state.floors.items())

def get_successors(state):
  floor = state.floors[state.elevator]
  for items in combinations_up_to(floor,MAX_CARRY):
    if not items: continue
    valid_elevators = [state.elevator+i for i in [-1,+1] if MIN_FLOOR <= state.elevator+i <= MAX_FLOOR]
    for new_elevator in valid_elevators:
      new_state = State(new_elevator,copy.deepcopy(state.floors))
      new_state.floors[state.elevator] -= set(items)
      new_state.floors[new_elevator] |= set(items)
      if valid(new_state):
        yield new_state

def valid(state):
  for floor,items in state.floors.items():
    if floor == MIN_FLOOR: continue
    microchips = set(item[2:] for item in items if item.startswith('m'))
    generators = set(item[2:] for item in items if item.startswith('g'))
    loose_chips = microchips - generators
    if microchips - generators and generators:
      return False
  return True

def combinations_up_to(l,r):
  for i in range(r+1):
    yield from itertools.combinations(l, i)
    
start_state = load_start_state()
x = path_search(start_state,get_successors,is_goal)
print(x[1])

# only gives the correct answer some of the time...
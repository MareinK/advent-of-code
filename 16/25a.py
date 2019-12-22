import collections, re

def is_int(x):
  try:
    int(x)
    return True
  except:
    return False

def cpy(x,y):
  if not is_int(y):
    if is_int(x):
      registers[y] = int(x)
    else:
      registers[y] = registers[x]
  return 1

def inc(x):
  if not is_int(x):
    registers[x] += 1
  return 1

def dec(x):
  if not is_int(x):
    registers[x] -= 1
  return 1

def jnz(x,y):
  if is_int(y):
    y = int(y)
  else:
    y = registers[y]
  if is_int(x) and int(x) != 0:
    return y
  elif not is_int(x) and registers[x] != 0:
    return y
  else:
    return 1
  
def out(x):
  if is_int(x):
    x = int(x)
  else:
    x = registers[x]
  return x

instructions = {re.compile(r'cpy (-?\w+) (-?\w+)'): cpy,
                re.compile(r'inc (-?\w+)'): inc,
                re.compile(r'dec (-?\w+)'): dec,
                re.compile(r'jnz (-?\w+) (-?\w*)'): jnz,
                re.compile(r'out (-?\w+)'): out}

data = open('25.txt').readlines()
code = []
for line in data:
  for pattern,f in instructions.items():
    m = pattern.match(line)
    if m:
      code.append((f,m.groups()))

n = 1
while True:
  registers = collections.defaultdict(int)
  registers['a'] = n
  pointer = 0

  prev = 1
  good = True
  seen = set()
  while True:
    s = (frozenset(registers.items()),pointer)
    if s in seen:
      break
    seen.add(s)
    f,args = code[pointer]
    if f == out:
      x = out(*args)
      if x == prev:
        good = False
        break
      prev = x
      pointer += 1
    else:
      pointer += f(*args)
  if good:
    print(n)
    break
  n += 1

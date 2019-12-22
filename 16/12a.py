import collections, re

registers = collections.defaultdict(int)
pointer = 0

def is_int(x):
  try:
    int(x)
    return True
  except:
    return False

def cpy(x,y):
  if is_int(x):
    registers[y] = int(x)
  else:
    registers[y] = registers[x]
  return 1

def inc(x):
  registers[x] += 1
  return 1

def dec(x):
  registers[x] -= 1
  return 1

def jnz(x,y):
  if is_int(x) and int(x) != 0:
    return int(y)
  elif not is_int(x) and registers[x] != 0:
    return int(y)
  else:
    return 1

instructions = {re.compile(r'cpy (\w*) (\w*)'): cpy,
                re.compile(r'inc (\w*)'): inc,
                re.compile(r'dec (\w*)'): dec,
                re.compile(r'jnz (\w*) (-?\d*)'): jnz}

data = open('12.txt').readlines()
code = []
for line in data:
  for pattern,f in instructions.items():
    m = pattern.match(line)
    if m:
      code.append(lambda f=f,m=m: f(*m.groups()))

while pointer < len(code):
  pointer += code[pointer]()

print(registers['a'])

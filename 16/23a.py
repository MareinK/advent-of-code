import collections, re

registers = collections.defaultdict(int)
registers['a'] = 7
pointer = 0

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

def tgl(x):
  if is_int(x):
    x = int(x)
  else:
    x = registers[x]
  if 0 <= pointer+x < len(code):
    f,args = code[pointer+x]
    if len(args) == 1:
      if f == inc:
        f = dec
      else:
        f = inc
    else:
      if f == jnz:
        f = cpy
      else:
        f = jnz
    code[pointer+x] = (f,args)
  return 1

instructions = {re.compile(r'cpy (-?\w+) (-?\w+)'): cpy,
                re.compile(r'inc (-?\w+)'): inc,
                re.compile(r'dec (-?\w+)'): dec,
                re.compile(r'jnz (-?\w+) (-?\w*)'): jnz,
                re.compile(r'tgl (-?\w+)'): tgl}

data = open('23.txt').readlines()
code = []
for line in data:
  for pattern,f in instructions.items():
    m = pattern.match(line)
    if m:
      code.append((f,m.groups()))

while pointer < len(code):
  f,args = code[pointer]
  pointer += f(*args)

print(registers['a'])

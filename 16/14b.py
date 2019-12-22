import hashlib, re

salt = open('14.txt').read().strip()

threes = {}
fives = {}
pattern_three = re.compile(r'(\w)\1{2}')
pattern_five = re.compile(r'(\w)\1{4}')

def gethash(i):
  code = (salt+str(i))
  for _ in range(2017):
    code = hashlib.md5(code.encode('utf-8')).hexdigest()
  return code

def three(i):
  if i not in threes:
    m = pattern_three.findall(gethash(i))
    if m:
      threes[i] = m[0]
    else:
      threes[i] = ''
  return threes[i]

def five(i):
  if i not in fives:
    m = pattern_five.findall(gethash(i))
    if m:
      fives[i] = m[0]
    else:
      fives[i] = ''
  return fives[i]
      
i = 0
found = 0
while found < 64:
  if three(i) != '' and any(five(j) == three(i) for j in range(i+1,i+1+1000)):
    found += 1
  i += 1

print(i-1)


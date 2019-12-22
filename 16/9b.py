import re

def length(data):
  matches = pattern.finditer(data)
  i = 0
  result = 0
  for match in matches:
    l,n = map(int,match.groups())
    if match.start() >= i:
      result += match.start()-i
      result += length(data[match.end():match.end()+l])*n
      i = match.end()+l
  result += len(data)-i
  return result

data = ''.join([line.strip() for line in open('9.txt')])
pattern = re.compile(r'\((\d*)x(\d*)\)')
print(length(data))

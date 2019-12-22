import re
data = ''.join([line.strip() for line in open('9.txt')])
matches = re.finditer(r'\((\d*)x(\d*)\)',data)
i = 0
result = ''
for match in matches:
  l,n = map(int,match.groups())
  if match.start() >= i:
    result += data[i:match.start()]
    result += data[match.end():match.end()+l]*n
    i = match.end()+l
result += data[i:]
print(len(result))

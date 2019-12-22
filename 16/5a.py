import itertools, hashlib
id = open('5.txt').read()
answer = ''
for i in itertools.count():
  if len(answer) == 8:
    break
  hash = hashlib.md5((id+str(i)).encode('utf-8')).hexdigest()
  if hash[:5] == '00000':
    answer += hash[5]
print(answer)

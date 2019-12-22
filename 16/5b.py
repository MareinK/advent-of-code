import itertools, hashlib
id = open('5.txt').read()
answer = ['-']*8
for i in itertools.count():
  if not any(c=='-' for c in answer):
    break
  hash = hashlib.md5((id+str(i)).encode('utf-8')).hexdigest()
  if hash[:5] == '00000':
    j,c = hash[5:7]
    j = int(j,16)
    if j < 8 and answer[j] == '-':
      answer[j] = c
print(''.join(answer))

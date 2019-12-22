import collections, difflib, string, re
pattern = r'((?:\w*-?)*)-(\d*)\[(\w*)\]'
lines = [re.search(pattern,line).groups() for line in open('4.txt')]
def check(code,checksum):
  counter = collections.Counter(code.replace('-',''))
  order = [x for _,x in sorted([(-n,x) for x,n in  counter.items()])]
  return ''.join(order[:5]) == checksum
def rotate(c,id):
  if c not in string.ascii_lowercase:
    return ' '
  else:
    ix = (string.ascii_lowercase.index(c)+id) % len(string.ascii_lowercase)
    return string.ascii_lowercase[ix]
def decode(code,id):
  return ''.join([rotate(c,id) for c in code])

names = {decode(code,int(id)):id for code,id,checksum in lines if check(code,checksum)}
answer = names[difflib.get_close_matches('north pole objects',names,n=1)[0]]
print(answer)

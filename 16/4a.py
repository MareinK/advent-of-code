import collections, re
pattern = r'((?:\w*-)*)(\d*)\[(\w*)\]'
lines = [re.search(pattern,line).groups() for line in open('4.txt')]
def check(name,checksum):
  counter = collections.Counter(name.replace('-',''))
  order = [x for _,x in sorted([(-n,x) for x,n in  counter.items()])]
  return ''.join(order[:5]) == checksum
answer = sum([int(id) for name,id,checksum in lines if check(name,checksum)])
print(answer)

import collections, re
arrangement = open('15.txt').read().splitlines()
pattern = re.compile(r'Disc #(\d*) has (\d*) positions; at time=0, it is at position (\d*).')
Disc = collections.namedtuple('Disc',['number','size','start'])
discs = [Disc(*map(int,pattern.match(line).groups())) for line in arrangement]
discs.append(Disc(len(discs)+1,11,0))

i = 0
while True:
  if all((disc.start + i + disc.number) % disc.size == 0 for disc in discs):
    break
  i += 1
    
print(i)

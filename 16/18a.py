rows = []
row = [c=='.' for c in open('18.txt').read()]
for _ in range(40):
  rows.append(row)
  row = [a==b for a,b in zip([1]+row[:-1],row[1:]+[1])]
print(sum(map(sum,rows)))

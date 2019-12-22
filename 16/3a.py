triangles = [list(map(int,line.split())) for line in open('3.txt')]
validity = [sum(t)-max(t) > max(t) for t in triangles]
print(sum(validity))

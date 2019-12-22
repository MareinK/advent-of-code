import numpy as np
triangles = [list(map(int,line.split())) for line in open('3.txt')]
triangles = np.array(triangles).T.reshape((len(triangles),3))
validity = [sum(t)-max(t) > max(t) for t in triangles]
print(sum(validity))

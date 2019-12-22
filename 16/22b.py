import collections, re
import numpy as np

Node = collections.namedtuple('Node',['x','y','size','used','avail','use'])
node_pattern = re.compile(r'\/dev\/grid\/node-x(\d+)-y(\d+)\s+(\d+)T\s+(\d+)T\s+(\d+)T\s+(\d+)%')
data = open('22.txt').read()
nodes = [Node(*map(int,node)) for node in node_pattern.findall(data)]

width = max(node.y+1 for node in nodes)
height = max(node.x+1 for node in nodes)
gridsize = (width,height)

size = np.zeros(gridsize)
used = np.zeros(gridsize)

for node in nodes:
  used[node.y,node.x] = node.used    

from matplotlib import pyplot as plt
plt.imshow(used, interpolation='nearest')
plt.show()

# move 0 to top row = 20
# move 0 to right = 32
# move G to left = 35*5 = 175]
# sum = 227

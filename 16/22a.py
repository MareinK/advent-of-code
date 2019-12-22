import collections, re
import intervaltree

Node = collections.namedtuple('Node',['x','y','size','used','avail','use'])
node_pattern = re.compile(r'\/dev\/grid\/node-x(\d+)-y(\d+)\s+(\d+)T\s+(\d+)T\s+(\d+)T\s+(\d+)%')
data = open('22.txt').read()
nodes = [Node(*map(int,node)) for node in node_pattern.findall(data)]

tree = intervaltree.IntervalTree()
for node in nodes:
  tree[0:node.avail] = node

print(sum(len(tree[node.used]-set([node])) for node in nodes if node.used != 0))

import collections, itertools, ast, os
import matplotlib.pyplot as plt
from matplotlib import cm
import pandas as pd
import numpy as np
      
def get_filepaths():
  for i,j in itertools.product(range(26),['a','b']):
    path = '{}{}.py'.format(i,j)
    if os.path.isfile(path):
      yield path

def get_pystdlib():
  with open('pystdlib.txt') as f:
    return f.read().split()

def get_imports(path):
  with open(path) as f:        
    root = ast.parse(f.read(), path)

  for node in ast.iter_child_nodes(root):
    if isinstance(node, ast.Import):
      module = []
    elif isinstance(node, ast.ImportFrom):  
      module = node.module.split('.')
    else:
      continue

    for n in node.names:
      yield module[0] if module else n.name.split('.')[0]

filepaths = list(get_filepaths())
pystdlib = get_pystdlib()
imports = {p:set(get_imports(p)) for p in filepaths}
counts = collections.Counter(itertools.chain.from_iterable(imports.values()))

no_imports = 0
standard_imports = 0

tick = ':heavy_check_mark:'

table = []
for path in filepaths:
  row = ['{} ({})'.format(path.split('.')[0],len(imports[path]))]
  if not imports[path]:
    no_imports += 1
    row.append(tick)
  else:
    row.append('')
  if any(x in pystdlib for x in imports[path]):
    row.append(tick)
    standard_imports += 1
  else:
    row.append('')
  for lib,n in counts.most_common():
    if lib not in pystdlib:
      if lib in imports[path]:
        row.append(tick)
      else:
        row.append('')
  table.append(row)

def filelength(path):
  with open(path) as f:
    content = f.read()
  lines = len([line for line in content.splitlines() if line.strip() and line.strip()[0] != '#'])
  treesize = len(list(ast.walk(ast.parse(content))))
  return lines,treesize
  
lengths = []
for path in filepaths:
  lengths.append(filelength(path))

fig = plt.figure()
ax = fig.add_subplot(111)
ax2 = ax.twinx()

width = 0.4

df = pd.DataFrame(lengths)
df[0].plot(kind='bar', color=cm.viridis(0.25), ax=ax, width=width, position=1, label='Lines of code', align='center')
df[1].plot(kind='bar', color=cm.viridis(0.75), ax=ax2, width=width, position=0, label='AST size', align='center')

ax.set_ylabel('Lines of code')
ax2.set_ylabel('AST size')

handles = ax.get_legend_handles_labels()[0]+ax2.get_legend_handles_labels()[0]
labels = ax.get_legend_handles_labels()[1]+ax2.get_legend_handles_labels()[1]
plt.legend(handles,labels,loc=2)

plt.xlim([-0.5,len(filepaths)-0.5])
ax.set_xticklabels([path.split('.')[0] if 'a' in path else 'b' for path in filepaths], rotation=0)

ax.set_xticks(np.arange(-0.5,len(filepaths),2), minor=True)
ax.xaxis.grid(True, which='minor')
for tick in ax.xaxis.get_major_ticks():
  tick.label.set_fontsize(6)
  
plt.title('Complexity measures')
plt.savefig('complexity_measures.png')

metric_corr = df[0].corr(df[1])
if len(lengths) % 2 != 0:
  lengths = lengths + [(0,0)]
loc_vals = np.array(lengths)[:,0].reshape(len(lengths)//2,2)
ast_vals = np.array(lengths)[:,1].reshape(len(lengths)//2,2)
loc_diff = (loc_vals[:,1]/loc_vals[:,0]).mean()*100-100
ast_diff = (ast_vals[:,1]/ast_vals[:,0]).mean()*100-100

impheader = ['`{}` ({})'.format(imp,n) for imp,n in counts.most_common() if imp not in pystdlib]
header = ['Part','None ({})'.format(no_imports),'Standard ({})'.format(standard_imports)] + impheader
header_str = '| '+' | '.join(header)+' |'
div_str = '| '+' | '.join(':---:' for _ in header)+' |'
content_str = '\n'.join('| '+' | '.join(row)+' |' for row in table)
table_str = '\n'.join([header_str, div_str, content_str])

with open('readme_template.md') as f:
  template = f.read()

readme = template.format(metric_correlation=metric_corr,loc_diff=loc_diff,ast_diff=ast_diff,imports_table=table_str)

with open('readme.md','w') as f:
  f.write(readme)
  
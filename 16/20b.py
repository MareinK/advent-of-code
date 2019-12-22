import numpy as np
arr = np.ones(2**32,dtype=bool)
for line in open('20.txt'):
  a,b = map(int,line.split('-'))
  arr[a:b+1] = False
print(len(np.where(arr)[0]))

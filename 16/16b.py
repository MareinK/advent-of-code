import numpy as np
n = 35651584
a = np.array(list(map(int,open('16.txt').read())))
while len(a) < n:
  a = np.concatenate((a,[0],np.logical_not(a[::-1])))
a = a[:n]
while len(a)%2 == 0:
  a = np.logical_not(np.logical_xor(*a.reshape(len(a)//2,2).transpose()))
print(''.join(np.char.mod('%d',a)))

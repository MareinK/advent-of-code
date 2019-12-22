import math
n = int(open('19.txt').read())
print(2*(n-2**math.floor(math.log(n,2)))+1)

import math
n = int(open('19.txt').read())
#x = math.floor(decimal.Decimal(n-1).ln()/decimal.Decimal(3).ln()) # for high precision, important for some values of n
x = math.floor(math.log(n-1,3))
y = n - 3**x
if y <= 3**x:
  z = y-1
else:
  z = -3**x+2*y-1
print(z+1)

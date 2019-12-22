import re
import numpy as np

def swap_pos(arr,x,y):
  x,y = int(x),int(y)
  arr[x],arr[y] = arr[y],arr[x]
  return arr
  
def swap_letter(arr,x,y):
  a,b = np.where(arr==x)[0][0], np.where(arr==y)[0][0]
  arr[a],arr[b] = arr[b],arr[a]
  return arr
  
def rotate_steps(arr,lr,x):
  x = int(x)
  d = -1 if lr == 'left' else 1
  return np.roll(arr,d*x)
  
def rotate_letter(arr,x):
  y = np.where(arr==x)[0][0]
  if y >= 4:
    y+=1
  return np.roll(arr,y+1)

def reverse(arr,x,y):
  x,y = int(x),int(y)
  arr[x:y+1] = arr[x:y+1][::-1]
  return arr

def move(arr,x,y):
  x,y = int(x),int(y)
  a = arr[x]
  arr = np.delete(arr,x)
  return np.insert(arr,y,a)

operations = {re.compile(r'swap position (\d+) with position (\d+)'): swap_pos,
              re.compile(r'swap letter (\w) with letter (\w)'): swap_letter,
              re.compile(r'rotate (left|right) (\d+) steps?'): rotate_steps,
              re.compile(r'rotate based on position of letter (\w)'): rotate_letter,
              re.compile(r'reverse positions (\d+) through (\d+)'): reverse,
              re.compile(r'move position (\d+) to position (\d+)'): move}

arr = np.array(list('abcdefgh'))

instructions = open('21.txt').readlines()

for instruction in instructions:
  for pattern,f in operations.items():
    m = pattern.match(instruction)
    if m:
      arr = f(arr,*m.groups())
      
print(''.join(c for c in arr))

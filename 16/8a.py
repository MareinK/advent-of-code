import re
import numpy as np
instructions = [line.strip() for line in open('8.txt')]
def rect(arr,x,y): arr[:y,:x] = 1
def row(arr,i,n): arr[i] = np.roll(arr[i],n)
def column(arr,i,n): arr[:,i] = np.roll(arr[:,i],n)
actions = {re.compile(r'rect (\d*)x(\d*)'): rect,
           re.compile(r'rotate row y=(\d*) by (\d*)'): row,
           re.compile(r'rotate column x=(\d*) by (\d*)'): column}
arr = np.zeros((6,50));
for instruction in instructions:
  for pattern,action in actions.items():
    match = pattern.match(instruction)
    if match:
      action(arr,*map(int,match.groups()))
print(int(arr.sum()))

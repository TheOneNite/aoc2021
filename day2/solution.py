import sys
import os
import input



inputList = input.puzzle.split('\n')
# inputList = input.test.split('\n')

depth = 0
pos = 0
aim = 0

i = 0

for com in inputList:
    arr = com.split(' ')
    dir = arr[0]
    mag = int(arr[1])
    if dir == 'forward':
        pos = pos + mag
        depth = depth + aim * mag
    elif dir == 'up':
        aim = aim - mag
    elif dir == 'down':
        aim = aim + mag
    print(depth, pos)


print(depth * pos)
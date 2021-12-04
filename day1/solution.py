import sys
import os
import input

def removeIncomplete(list):
    return len(list) == 3

print(input)

inputList = input.puzzle.split('\n')
# inputList = input.test

depthChanges = 0
prev = 0
mappedDepths = []

i = 0
for x in inputList:
    depth = int(x)
    for j in mappedDepths:
        if len(j) < 3:
            j.append(depth) 
    mappedDepths.append([depth])
    i = i+1

print(mappedDepths)

mappedDepths = list(filter(removeIncomplete,mappedDepths))

iList = 0
for list in mappedDepths:
    total = list[0]+list[1]+list[2]
    mappedDepths[iList] = total
    iList = iList + 1

print(mappedDepths)
for depth in mappedDepths: 
    # depth = int(x)
    print(depth)
    if prev > 0 :
        if depth > prev :
            depthChanges = depthChanges + 1
    prev = depth

print("deepenings",depthChanges)
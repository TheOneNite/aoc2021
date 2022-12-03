import sys
import os
from inputs import day1

test = '''1000
2000
3000

4000

5000
6000

7000
8000
9000

10000'''

inputList = day1.split('\n')
elves = []
elfId = 1
cals = 0
for line in inputList:
    if len(line) > 0:
        cals = cals + int(line)
    else:
        # elves[elfId] = cals
        elves.append(cals)
        elfId = elfId+1
        cals = 0


elves.sort()
print(elves)

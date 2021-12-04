import sys
import os
from input import day3 



test = '''00100
11110
10110
10111
10101
01111
00111
11100
10000
11001
00010
01010'''
inputList = day3.split('\n')
# inputList = test.split('\n')


def toDecimal (bin):
    binary = bin[::-1]
    place = 1
    total = 0
    for i in range(0, len(binary)):
        total = total + place * int(binary[i])
        place = place * 2
    return total

def filterAtPosition(inputList, i, isO2):
    
    count = 0
    for bin in inputList:
        count = count + int(bin[i])
    targetVal = 0
    if isO2:
        targetVal = 1
    if count < (len(inputList) / 2):
        if targetVal:
            targetVal = 0
        else:
            targetVal = 1
    def isCandidate(value):
        return int(value[i]) == targetVal
    candidates = list(filter(isCandidate, inputList))
    if len(candidates) == 1:
        return candidates[0]
    else:
        return filterAtPosition(candidates, i+1, isO2)


o2 = filterAtPosition(inputList, 0, True)
co2 = filterAtPosition(inputList, 0, False)
lifeSupport = toDecimal(o2) * toDecimal(co2)
print(lifeSupport)



# l = len(inputList[1])
# count = []
# for j in range(0,l):
#     count.append(0)

# for bin in inputList:
#     for i in range(0,l):
#         count[i] = count[i] + int(bin[i])

# gamma = ''
# epsilon = ''

# for i in range(0,l):
#     target = len(inputList) / 2
#     if count[i] < target:
#         gamma = gamma + '0'
#         epsilon = epsilon + '1'
#     else:
#         gamma = gamma + '1'
#         epsilon = epsilon + '0'


# print(gamma, epsilon)
# power = toDecimal(gamma)*toDecimal(epsilon) 
# print(power)




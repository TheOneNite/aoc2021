from input import day7

pos = [16,1,2,0,4,2,7,1,2,14]
pos = day7

max = 9999999999999999999999999999999999999999

pos.sort()
fuel = 0
prevFuel = max
best = 0

stepSize = int(len(pos) / 3)

def calcFuel(x, target):
    distance = abs(x - target)
    cost = 0
    for u in range(1, distance+1):
        cost += u
    return cost


for target in range(0, pos[len(pos) - 1]):
    print('align on ',target)
    for i, x in enumerate(pos[0:len(pos):stepSize]):
        fuel = fuel + calcFuel(x, target)
    print(fuel)
    if fuel > prevFuel:
        print('inflect at', target - 1)
        best = target - 1
        prevFuel = max
        # stepSize = stepSize - 1
        break
    else:
        prevFuel = fuel
        fuel = 0

while stepSize > 0:
    print('step', stepSize, 'best', best)
    for target in range(best - stepSize*2, best + stepSize*2):
        print('search towards', target)
        sample = pos[0 : len(pos)+1:stepSize]
        for i, x in enumerate(pos):
            fuel = fuel + calcFuel(x, target)
        print(fuel, prevFuel)
        if fuel > prevFuel:
            fuel = 0
            prevFuel = max
            print('inflect at', target - 1)
            best = target - 1
            # # if stepSize == 1:
            #     print(target - 1, 'FOUND')
            stepSize = int(stepSize / 2)
            break
        else:
            prevFuel = fuel
            fuel = 0
    #exit condition
    # stepSize = stepSize - 1

fuel = 0
for x in pos:
    fuel += calcFuel(x,best)

print('total fuel', fuel)
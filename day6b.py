from input import day6

test1 = [3,4,3,1,2]

birthsE = 0
birthsO = 0

pop = [0,0,0,0,0,0,0,0,0]

for fish in day6:
    pop[fish] = pop[fish] + 1

newFish = 0
for day in range(0, 256):
    print('day',day+1)
    newPop = [0,0,0,0,0,0,0,0,0]
    for age, number in enumerate(newPop):
        if age != 8:
            newPop[age] = pop[age + 1]
    newPop[6] = newPop[6] + pop[0]
    newPop[8] = newFish
    newFish = newPop[0]
    # print(pop)
    # print('births',newFish)
    # print(newPop)
    pop = newPop

print('total fishes',sum(pop))
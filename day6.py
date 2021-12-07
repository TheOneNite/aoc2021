from input import day6

test1 = [3,4,3,1,2]

birthsE = 0
birthsO = 0

pop = day6

for day in range(0, 256):
    print(day)
    newFish = 0
    for i, fish in enumerate(pop):
        births = 0
        if fish == 0:
            newFish = newFish+1
            pop[i] = 6
        else:
            pop[i] = fish - 1
        # if day % 2 > 0:
        #     birthsO = births
        #     newFish = birthsE
        # else:
        #     birthsE = births
        #     newFish = birthsO
    if newFish > 0:
        for b in range(0, newFish):
            pop.append(8)
    print(newFish)

print('total fishes',len(pop))
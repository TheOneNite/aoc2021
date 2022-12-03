from inputs import day3

test = '''vJrwpWtwJgWrhcsFMMfFFhFp
jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL
PmmdzqPrVvPwwTWBwg
wMqvLMZHhHMvwLHjbvcjnnSBnvTQFn
ttgJtRGJQctTZtZT
CrZsJsPPZsGzwwsLwLmpwMDw'''

index = 'abcdefghijklmnopqrstuvwxyz'

sacks = day3.splitlines()

groups = []
for i in range(0, len(sacks), 3):
    chunk = sacks[i:i+3]
    groups.append(chunk)


print(groups)

badges = []
for group in groups:
    elf1 = group[0]
    elf2 = group[1]
    elf3 = group[2]
    for c in elf1:
        print(c)
        if c in elf2 and c in elf3:
            badges.append(c)
            break
print(badges)


# overlap = []
ans = 0
# for single in sacks:
#     dupes = []
#     splitI = int(len(single) / 2)
#     cOne = single[0:splitI]
#     cTwo = single[splitI:len(single)]
#     for c in cOne:
#         if c in cTwo:
#             dupes.append(c)
#     deDuped = list(dict.fromkeys(dupes))
#     overlap.extend(deDuped)

for item in badges:
    print(item)
    prio = index.find(item) + 1
    if prio < 1:
        prio = index.find(item.swapcase()) + 27
    ans = ans + prio
    print(prio)
    prio = 0

print(ans)
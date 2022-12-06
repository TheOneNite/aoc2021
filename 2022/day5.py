
from inputs import day5

test = '''    [D]    
[N] [C]    
[Z] [M] [P]
 1   2   3 

move 1 from 2 to 1
move 3 from 1 to 3
move 2 from 2 to 1
move 1 from 1 to 2'''

lines = day5.splitlines()
stacks = lines[:lines.index('')]
moves = lines[lines.index('')+1:]

stacks.reverse()

ship = {}

labels = stacks[0]
for i in range(1,len(labels),4):
        stackId = int(labels[i])
        ship[stackId] = []

# print(ship)
for row in stacks[1:]:
    for stack, i in enumerate(range(1,len(row),4)):
        crate = row[i].strip()
        if len(crate) > 0:
            ship[stack+1].append(crate)


# print(ship)

for inst in moves:
    brkdwn = inst.split(' ')
    n = int(brkdwn[1])
    source = int(brkdwn[3])
    dest = int(brkdwn[5])
    grab = ship[source][len(ship[source])-n:len(ship[source])]
    print(grab)
    for m in range(0,n):
        ship[source].pop()
    ship[dest] = ship[dest] + (grab)

tops = []
for stack in ship:
    print(stack)
    tops.append(ship[stack][-1])
print(''.join(tops))

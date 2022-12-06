from inputs import day4

test = '''2-4,6-8
2-3,4-5
5-7,7-9
2-8,3-7
6-6,4-6
2-6,4-8'''

pairs = day4.splitlines()

def getAssignBounds(str):
    nums = str.split('-')
    return (int(nums[0]), int(nums[1])+1)

ans = 0
for pair in pairs:
    assignment = pair.split(',')
    left = range(*getAssignBounds(assignment[0]))
    right = range(*getAssignBounds(assignment[1]))

    if len(left) < len(right):
        a1 = left
        a2 = right
    else:
        a2 = left
        a1 = right
    
    for id in a1:
        if id in a2:
            ans = ans + 1 
            break
    
# print(list(range(1,1)))
print(ans)


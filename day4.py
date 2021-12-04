import input 


nums = [7,4,9,5,11,17,23,2,0,14,21,24,10,16,13,6,15,25,12,22,18,20,8,19,3,26,1]
testBoards = '''22 13 17 11  0
 8  2 23  4 24
21  9 14 16  7
 6 10  3 18  5
 1 12 20 15 19

 3 15  0  2 22
 9 18 13 17  5
19  8  7 25 23
20 11 10 24  4
14 21 16 12  6

14 21 17 24  4
10 16 15  9 19
18  8 23 26 20
22 11 13  6  5
 2  0 12  3  7
'''

rows = [[0,  1,  2,  3,  4,],
[5 , 6,  7,  8,  9,],
[10 ,11, 12, 13, 14,],
[15, 16, 17, 18, 19, ],
[20, 21, 22, 23, 24,]]

 #5 with same x%5 is col
 # slice, store in dict

boards = input.day4Boards.split('\n\n')
winningBoards = []
winningCall = {}
finishedBoards = {}


def checkWin(candidates):
    # print('candidates',candidates)
    winners = []
    for tup in candidates:
        board = tup[0]
        candidateI = tup[1]
        mods = list(map(lambda ind:ind%5, board))
        for mod in range(0,5):
            if mods.count(mod) > 4:
                    board.sort()
                    winners.append(candidateI)
        board.sort()
        for row in rows:
            if all(i in board for i in row):
                winners.append(candidateI)
    return winners
    


i = 0
hitI = []
for board in boards:
    cleanedBoard = board.split('\n')
    boardString = ' '.join(cleanedBoard)
    numStrBoard = list(filter(lambda s:len(s)>0 ,boardString.split(' ')))
    numBoard = list(map(lambda s: int(s), numStrBoard))
    boards[i] = numBoard
    i = i+1
    hitI.append([])

for x in input.day4Nums:
    num = int(x)
    j = 0
    for boardI, board in enumerate(boards):
        # print(board)
        if num in board and boardI not in winningBoards:
            hitI[j].append(board.index(num))
        j=j + 1
    # print()
    if any(len(ele) > 4 for ele in hitI):
        #this is a list comprehension, creates index-key pairs for which boards could be winners
        # print(hitI)
        print(hitI[63])

        candidates = [(hitInds, candInd) for candInd, hitInds in enumerate(hitI) if len(hitInds) > 4 and candInd not in winningBoards]
        # print(candidates)
        winner = checkWin(candidates)
        if len(winner) > 0:
            for won in winner:
                winningBoards.append(won)
                winningCall[won] = num
            # too high 27...p1
            # too low 25908p1
    j = 0

losingBoardIndex = winningBoards.pop()
print('lastwinner',losingBoardIndex)
winningHits = hitI[losingBoardIndex]
winningBoard=boards[losingBoardIndex]
print(winningBoard)
print(winningHits)
unmarkedNums = [num for ind, num in enumerate(winningBoard) if ind not in winningHits]
score = sum(unmarkedNums)*winningCall[losingBoardIndex]
print(score)
#38092 too high

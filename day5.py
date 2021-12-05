from input import day5
test1 = '''0,9 -> 5,9
8,0 -> 0,8
9,4 -> 3,4
2,2 -> 2,1
7,0 -> 7,4
6,4 -> 2,0
0,9 -> 2,9
3,4 -> 1,4
0,0 -> 8,8
5,5 -> 8,2'''

def strToCoord(string):
    coords = string.split(' -> ')
    coords = list(map(lambda str:str.split(','),coords))
    coords = [(int(nsA[0]), int(nsA[1])) for nsA in coords]
    # print(coords)
    return coords

arr = day5.split('\n')
lines = list(map(strToCoord, arr))
# straightLines = list(filter(lambda line:line[0][0]==line[1][0] or line[0][1]==line[1][1], lines))
# print(straightLines)

#grid is a map with array of xs at key y
grid = []

for line in lines:
    # print(line)
    start = line[0]
    end = line[1]
    if start[0] == end[0]:
        #push same x line
        x = start[0]
        tiles = [start[1], end[1]]
        tiles.sort()
        # print(tiles)
        for y in range(tiles[0], tiles[1]+1):
            if(len(grid) < y+1):
                for i in range(len(grid),y+1):
                    grid.append([])
            row = grid[y]
            if len(row) < x+1:
                for i in range(len(row), x+1):
                    row.append(0)
            # print(x)
            row[x] = row[x] + 1
            # print(row)
    elif start[1] == end[1]:
        #push same y line
        y = start[1]
        if(len(grid) < y+1):
            for i in range(len(grid),y+1):
                grid.append([])
        row = grid[y]
        tiles = [start[0], end[0]]
        tiles.sort()
        # print(tiles)
        if len(row) < tiles[1]+1:
            for i in range(len(row), tiles[1]+1):
                row.append(0)
        for x in range(tiles[0], tiles[1]+1):
            # print(x)
            row[x] = row[x] + 1
    else:
        # print(line)
        dir = [start[0] - end[0], start[1] - end[1]]
        for i, n in enumerate(dir):
            if n < 0:
                dir[i] = 1
            else:
                dir[i] = -1
        length = [start[0], end[0]]
        length.sort()
        length = length[1] - length[0]
        coord = {'x':start[0], 'y':start[1]}
        # print(coord)
        for tile in range(0, length+1):
            # print(tile)
            if len(grid) < coord['y']+1:
                for i in range(len(grid), coord['y']+1):
                    grid.append([])
            row = grid[coord["y"]]
            if len(row) < coord['x']+1:
                for i in range(len(row), coord['x']+1):
                    row.append(0)
            row[coord['x']] = row[coord['x']] + 1
            coord['x'] = coord['x'] + dir[0]
            coord['y'] = coord['y'] + dir[1]
            # print(coord)

       
# print(grid)
vents = [tile for cols in grid for tile in cols]
overlaps = [tile for tile in vents if tile > 1]
print(len(overlaps))
#4640 too low

#17690 too low

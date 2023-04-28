with open("test_input.txt") as infile:
    heightmap = infile.read().splitlines()
    low_points = []
    for i, row in enumerate(heightmap):
        col_list = []
        for col in row:
            col_list.append(int(col))
        heightmap[i] = col_list
    
    for y, row in enumerate(heightmap):
        for x, col in enumerate(row):
            print(x, y)
            if x > 0:
                if heightmap[y][x-1] < col:
                    continue
            if x < len(row):
                if heightmap[y][x+1] < col:
                    continue
            if y > 0:
                if heightmap[y-1][x] < col:
                    continue
            if y < len(heightmap):
                if heightmap[y+1][x] < col:
                    continue
            low_points.append(col)
    
    print(low_points)
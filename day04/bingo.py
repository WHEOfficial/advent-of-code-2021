with open("input.txt", 'r') as infile:
    nums = [int(num) for num in infile.readline().split(",")]
    boards = []

    while infile.readline() != "":
        board = []
        for i in range(5):
            raw_row = infile.readline().strip().split(" ")
            row = []
            for j in raw_row:
                try:
                    row.append(int(j))
                except ValueError:
                    pass
            board.append(row)
        boards.append(board)
    
    print(boards)
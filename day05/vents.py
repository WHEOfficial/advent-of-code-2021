with open("test_input.txt", 'r') as infile:
    lines = [line.split(" -> ") for line in infile.read().splitlines()]
    for line in lines:
        for pair in line:
            print(pair.split(","))
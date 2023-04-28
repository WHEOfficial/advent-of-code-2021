visited = []
queue = {'0,0': 0}
backtrack = {}

def key_to_point(key):
    return [int(i) for i in key.split(',')]

def point_to_key(point):
    return ','.join([str(i) for i in point])

def add_point(new_point, old_point):
    old_x, old_y = key_to_point(old_point)
    queue[old_point]

with open("test_input.txt", 'r') as infile:
    risks = infile.read().splitlines()
    for i, l in enumerate(risks):
        risks[i] = [int(c) for c in l]
    
    WIDTH = len(risks)

    point = key_to_point(min(queue, key=queue.get))
    x, y = point
    if x > 0:
        new_point = risks[y][x-1]

    if y > 0:
        print(risks[y-1][x])
    if x < WIDTH - 1:
        print(risks[y][x+1])
    if y < WIDTH - 1:
        print(risks[y+1][x])
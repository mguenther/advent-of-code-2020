grid = [l.strip() for l in open('/home/pi/Documents/AdventOfCode/3.in', 'r').readlines()]

maxX = len(grid[0])
maxY = len(grid)

slopes = [(1,1), (3,1), (5,1), (7,1), (1,2)]
ans = 1

for slope in slopes:
    position = (0,0)
    tree = 0

    while position[1] < maxY:
        print "Checking position: " + str(position)
        if grid[position[1]][position[0] % maxX] == '#':
            tree += 1
        position = (position[0] + slope[0], position[1] + slope[1])

    ans *= tree

print ans
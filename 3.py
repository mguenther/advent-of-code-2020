grid = [l.strip() for l in open('3.in', 'r').readlines()]

max_x = len(grid[0])
max_y = len(grid)

slopes = [(1,1), (3,1), (5,1), (7,1), (1,2)]
ans = 1

for slope in slopes:
    position = (0,0)
    tree = 0

    while position[1] < max_y:
        if grid[position[1]][position[0] % max_x] == '#':
            tree += 1
        position = (position[0] + slope[0], position[1] + slope[1])

    ans *= tree

print(ans)
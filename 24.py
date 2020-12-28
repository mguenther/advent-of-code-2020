lines = [l.strip() for l in open('24.in', 'r').readlines()]

d = {
    'e': (1,0),
    'w': (-1, 0),
    'ne': (1, -1),
    'nw': (0, -1),
    'se': (0,1),
    'sw': (-1, 1)
}

tiles = {}

# wasn't necessary for part one
for x in range(-100,100):
    for y in range(-100, 100):
        tiles[(x,y)] = True

for moves in lines:
    pos = (0,0)
    i = 0
    while i < len(moves):
        if moves[i:i+2] in d:
            direction = d[moves[i:i+2]]
            pos = (pos[0] + direction[0], pos[1] + direction[1])
            i += 2
        elif moves[i:i+1] in d:
            direction = d[moves[i:i+1]]
            pos = (pos[0] + direction[0], pos[1] + direction[1])
            i += 1
        else:
            raise Exception('Unable to process line: ' + moves)
    #if pos in tiles:
    tiles[pos] = not tiles[pos]
    #else:
    #    tiles[pos] = False

res = 0
for pos in tiles:
    if not tiles[pos]:
        res += 1
print(res)

day = 1

while day <= 100:

    to_flip = []
    for pos in tiles:

        adjacent_black_tiles = 0
        for dx, dy in d.values():
            adj = (pos[0] + dx, pos[1] + dy)
            if adj in tiles and not tiles[adj]:
                adjacent_black_tiles += 1
        if tiles[pos]:
            # the tile at the given position is white
            if adjacent_black_tiles == 2:
                to_flip.append(pos)
        else:
            # the tile at the given position is black
            if adjacent_black_tiles == 0 or adjacent_black_tiles > 2:
                to_flip.append(pos)
    for pos in to_flip:
        tiles[pos] = not tiles[pos]

    day += 1

res = 0
for pos in tiles:
    if not tiles[pos]:
        res += 1
print(res)
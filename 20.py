from typing import Dict, List

import math
import pprint


def rotate(tile: List[str]) -> List[str]:
    return list(''.join(x[::-1]) for x in zip(*tile))


def rotate_s(s: str) -> str:
    return '\n'.join(rotate(s.splitlines()))


def flip(tile: List[str]) -> List[str]:
    return [s[::-1] for s in tile]


def flip_s(xs: List[str]) -> List[str]:
    r = []
    for s in xs:
        res = []
        lines = s.splitlines()
        for l in lines:
            res.append(''.join(reversed(l)))
        r.append('\n'.join(res))
    return r


def parse(filename: str) -> Dict:

    raw_tiles = [l for l in open(filename, 'r').read().strip().split('\n\n')]
    tiles = {}

    for raw_tile in raw_tiles:
        lines = raw_tile.strip('\n').split('\n')
        index, tile = int(lines[0].split(' ')[1].strip('\n').strip(':')), lines[1:]
        orientations = [
            tile,
            rotate(tile),
            rotate(rotate(tile)),
            rotate(rotate(rotate(tile)))
        ]
        orientations += flip(orientations)
        edges = [
            tile[0],
            rotate(tile)[0],
            rotate(rotate(tile))[0],
            rotate(rotate(rotate(tile)))[0]
        ]
        edges += flip(edges)
        tiles[index] = {
            'orientations': orientations,
            'edges': edges,
            'neighbours': set()
        }
    return tiles


def assemble(tiles):

    N = int(math.sqrt(len(tiles)))
    grid = [[(0,0)] * N for _ in range(N) ] # 1st: tile ID, 2nd: chosen orientation
    unassigned_tiles = set(tiles.keys())

    def place_tile(number=0):

        if TRACING:
            number_of_assigned_tiles = N**2-len(unassigned_tiles)+1
            number_of_unassigned_tiles = N**2-number_of_assigned_tiles+1
            progress_bar = '[' + ('#' * number_of_assigned_tiles) + ('.' * (number_of_unassigned_tiles)) + ']'
            print(progress_bar)

        if number == N ** 2:
            return True

        row, column = int(math.floor(number / N)), number % N

        for unassigned_tile in list(unassigned_tiles):
            
            for i, orientation in enumerate(tiles[unassigned_tile]['orientations']):

                aligns_with_top_tile = True
                aligns_with_left_tile = True

                if row > 0:
                    # check if the orientation aligns with the border of an
                    # already placed tile in the row above
                    adjacent_tile_id, chosen_orientation = grid[row-1][column]
                    adjacent_tile = tiles[adjacent_tile_id]['orientations'][chosen_orientation]
                    aligns_with_top_tile = all(orientation[0][i] == adjacent_tile[BORDER_LENGTH_OF_TILE-1][i] for i in range(BORDER_LENGTH_OF_TILE))

                if column > 0:
                    # check if the orientation aligns with the right border of
                    # a tile that was already placed to the left
                    adjacent_tile_id, chosen_orientation = grid[row][column-1]
                    adjacent_tile = tiles[adjacent_tile_id]['orientations'][chosen_orientation]
                    aligns_with_left_tile = all(orientation[i][0] == adjacent_tile[i][BORDER_LENGTH_OF_TILE-1] for i in range(BORDER_LENGTH_OF_TILE))

                if aligns_with_top_tile and aligns_with_left_tile:
                    # we found a tile that fits into the current assignment, we
                    # place it and continue assigning tiles
                    grid[row][column] = (unassigned_tile, i)
                    unassigned_tiles.remove(unassigned_tile)
                    if place_tile(number+1):
                        return True
                    unassigned_tiles.add(unassigned_tile)
        return False
    
    place_tile()

    return grid


def augment_with_neighbouring_edges(tiles):
    for i, l in tiles.items():
        for j, r in tiles.items():
            if i == j:
                continue
            shared_edges = [shared_edge for shared_edge in l['edges'] if shared_edge in r['edges']]
            if len(shared_edges) != 0:
                tiles[i]['neighbours'].add(j)
                tiles[j]['neighbours'].add(i)


def find_tiles_with_neighbours(neighbours, tiles):
    subset_of_tiles = {}
    for i, l in tiles.items():
        if len(tiles[i]['neighbours']) == neighbours:
            subset_of_tiles[i] = l
    return subset_of_tiles


def find_corners(tiles):
    return find_tiles_with_neighbours(2, tiles)


def find_edges(tiles):
    return find_tiles_with_neighbours(3, tiles)


def find_inner_tiles(tiles):
    return find_tiles_with_neighbours(4, tiles)


def place(tiles, assembly):
    N = int(math.sqrt(len(tiles)))
    puzzle = ''
    for puzzle_row in range(N):
        for tile_row in range(1, BORDER_LENGTH_OF_TILE-1):
            for puzzle_column in range(N):    
                for tile_column in range(1, BORDER_LENGTH_OF_TILE-1):
                    tile_id, orientation = assembly[puzzle_row][puzzle_column]
                    tile = tiles[tile_id]['orientations'][orientation]
                    puzzle += tile[tile_row][tile_column]
            puzzle += '\n'
    return puzzle


def part_one(tiles):
    result = 1
    for i, l in find_corners(tiles).items():
        if len(tiles[i]['neighbours']) == 2:
            result *= i
    return result


def part_two(tiles):

    assembly = assemble(tiles)

    puzzle = place(tiles, assembly)
    puzzle_orientations = [
        puzzle,
        rotate_s(puzzle),
        rotate_s(rotate_s(puzzle)),
        rotate_s(rotate_s(rotate_s(puzzle))),
    ]
    puzzle_orientations += flip_s(puzzle_orientations)
    monster_pattern = [
        '                  # ',
        '#    ##    ##    ###',
        ' #  #  #  #  #  #   '
    ]
    monster_indices = [(r, c) for r in range(len(monster_pattern)) for c in range(len(monster_pattern[r])) if monster_pattern[r][c] == '#']

    for puzzle in puzzle_orientations:

        p = puzzle.splitlines()
        monster = 0
        for r in range(len(p) - 3):
            for c in range(len(p) - 20):
                if all(p[r + dr][c + dc] == '#' for dr, dc in monster_indices):
                    monster += 1
        if monster > 0:
            total = sum(row.count('#') for row in p)
            result = total - monster * len(monster_indices)
            return result


# I borrowed a couple of things from https://github.com/kresimir-lukin/AdventOfCode2020/blob/main/day20.py

TRACING = False
BORDER_LENGTH_OF_TILE = 10

tiles = parse('20.in')
augment_with_neighbouring_edges(tiles)

print("Part one: " + str(part_one(tiles)))
print("Part two: " + str(part_two(tiles)))
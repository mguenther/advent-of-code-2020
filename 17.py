from typing import Set, Tuple

import itertools
import pprint


def number_of_neighbours(coordinate: Tuple[int,int,int,int], M: Set[Tuple[int,int,int,int]]) -> int:
    x, y, z, w = coordinate
    neighbours = 0
    for dx, dy, dz, dw in itertools.product([-1, 0, 1], repeat=4):
        if dx == 0 and dy == 0 and dz == 0 and dw == 0:
            continue
        if (x+dx,y+dy,z+dz,w+dw) in M:
            neighbours += 1
    return neighbours

lines = [l.strip() for l in open('17.sample', 'r').readlines()]
l, u = -15, 15
M = set()
M_ = set()
for i,x in enumerate(lines):
    for j,y in enumerate(x):
        if y == '#':
            M.add((i,j,0,0))

for i in range(0, 6):
    M_ = set()
    for x in range(l, u):
        for y in range(l, u):
            for z in range(l, u):
                for w in range(l, u):
                    neighbours = number_of_neighbours((x,y,z,w), M)
                    if (x,y,z,w) in M and neighbours in [2,3]:
                        M_.add((x,y,z,w))
                    if (x,y,z,w) not in M and neighbours == 3:
                        M_.add((x,y,z,w))
    M = M_

print(len(M))
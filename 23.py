from typing import Dict, List, Tuple

import pprint


class Node(object):
    
    def __init__(self, value: int, next = None):
        self._value = value
        self._next = next

    def get_value(self) -> int:
        return self._value

    def get_next(self):
        return self._next

    def set_next(self, next):
        self._next = next

    def pickup(self):
        
        n1 = self.get_next()
        n2 = n1.get_next()
        n3 = n2.get_next()

        self.set_next(n3.get_next())
        n3.set_next(None)
        
        return n1

    def insert(self, next):

        old_next = self.get_next()

        self.set_next(next)

        n = next
        while n.get_next() != None:
            n = n.get_next()
        n.set_next(old_next)


    def __repr__(self):
        if self._next is None:
            return str(self.get_value())
        else:
            return str(self.get_value()) + ' -> ' + str(self.get_next().get_value())


def solution(cups: List[int]) -> str:
    s = ''
    i = cups.index(1)
    for j in range(1, 9):
        s += str(cups[(i+j) % 9])
    return s


def solve_part_one(cups: str, max_simulation_time=100) -> str:

    cups = [int(i) for i in cups]
    current_cup = cups[0]
    tick = 0

    while tick < max_simulation_time:

        index_current_cup = cups.index(current_cup)
        indices_pickup = [
            (index_current_cup + 1) % 9,
            (index_current_cup + 2) % 9,
            (index_current_cup + 3) % 9
        ]

        pickup = list(map(lambda x: cups[x], indices_pickup))
        
        for cup in pickup: 
            cups.remove(cup)

        destination_cup = (current_cup - 1) % 9
        while destination_cup in pickup or destination_cup == 0:
            destination_cup = (destination_cup - 1) % 10

        index_destination_cup = cups.index(destination_cup)

        for i, cup in enumerate(pickup, start=1):
            cups.insert(index_destination_cup + i, cup)

        # we have to update the index to the current cup, since
        # this might have changed during list alteration
        index_current_cup = cups.index(current_cup)
        current_cup = cups[(index_current_cup+1) % 9]
        tick += 1
    
    return solution(cups)


def solve_part_two(cups: str, max_simulation_time=10000000) -> int:

    def build_indexed_linked_list(cups: List[int]) -> Tuple[Dict[int, Node], Node]:
        index = {}
        for i, cup in enumerate(cups):
            index[cup] = Node(cup)
        for pair in zip(cups, cups[1:] + cups[:1]):
            index[pair[0]].set_next(index[pair[1]])
        return index, index[cups[0]]

    def to_values(n: Node) -> int:
        values = []
        while n != None:
            values.append(n.get_value())
            n = n.get_next()
        return values

    cups = [int(i) for i in cups] + list(range(10, 1000000+1))
    index, current_cup = build_indexed_linked_list(cups)
    size = len(cups)
    tick = 0

    while tick < max_simulation_time:

        pickup = current_cup.pickup()
        values = to_values(pickup)

        destination = (current_cup.get_value() - 1) % size
        while destination == 0 or destination in values:
            destination = (destination - 1) % (size+1)
        destination_cup = index[destination]

        destination_cup.insert(pickup)
        current_cup = current_cup.get_next()

        tick += 1

    return index[1].get_next().get_value() * index[1].get_next().get_next().get_value()


print(solve_part_one('158937462'))
print(solve_part_two('158937462'))
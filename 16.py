
from functools import reduce
from typing import Callable, Dict, List, Tuple

import pprint


def parse_constraints(parser_mode: int) -> bool:
    return bool((parser_mode >> 0) & 1)

def parse_my_ticket(parser_mode: int) -> bool:
    return bool((parser_mode >> 1) & 1)

def parse_nearby_tickets(parser_mode: int) -> bool:
    return bool((parser_mode >> 2) & 1)

def to_range_function(range_: str) -> Callable:
    lower, upper = range_.split('-')
    loweri, upperi = int(lower), int(upper)
    return lambda x: x >= loweri and x <= upperi

def to_constraints(ranges_: List[str]) -> List[Callable]:
    return [to_range_function(range_) for range_ in ranges_]

def evaluate_constraint(probe: int, constraint: List[Callable]) -> bool:
    return True in map(lambda x: x(probe), constraint)

def parse(filename: str) -> Tuple[Dict[str, List[Callable]], List[int], List[List[int]]]:
    parser_mode = 1
    constraints = {}
    my_ticket = []
    nearby_tickets = []

    lines = [l.strip() for l in open(filename, 'r').readlines() if l.strip() != '']

    for line in lines:
        if line.startswith('your') or line.startswith('nearby'):
            parser_mode = parser_mode << 1
            continue
        if (parse_constraints(parser_mode)):
            name, ranges = line.split(':')
            constraints[name.strip()] = to_constraints(ranges.split(' or '))
        elif (parse_my_ticket(parser_mode)):
            ticket_data = [int(constraint) for constraint in line.split(',')]
            my_ticket = ticket_data
        elif (parse_nearby_tickets(parser_mode)):
            ticket_data = [int(constraint) for constraint in line.split(',')]
            nearby_tickets.append(ticket_data)
        else:
            print("Unrecognized parser mode.")
            sys.exit(1)
    return constraints, my_ticket, nearby_tickets

def find_candidates(valid_nearby_tickets: List[List[int]], constraints: Dict[str, List[Callable]]) -> Dict[int, List[str]]:
    possible_fields_for_index = {} # key: index, value: list of possible fields
    for idx in range(len(valid_nearby_tickets[0])):
        possible = []
        for constraint in constraints:
            all_match = True
            for valid_nearby_ticket in valid_nearby_tickets:
                all_match = all_match and evaluate_constraint(valid_nearby_ticket[idx], constraints[constraint])
            if all_match:
                possible.append(constraint)
        possible_fields_for_index[idx] = possible
    return possible_fields_for_index

def find_candidates_with_single_value_left(candidates: Dict[int, List[str]]) -> List[str]:
    idx_field_assignments = []
    for idx in candidates:
        if len(candidates[idx]) == 1:
            idx_field_assignments.append((idx, candidates[idx][0]))
    return idx_field_assignments

def find_assignment(candidates: Dict[int, List[str]]) -> Dict[int, str]:
    assignment = {}
    while len(candidates) != 0:
        idx, field = find_candidates_with_single_value_left(candidates)[0] # be greedy if there are multiple
        assignment[idx] = field
        del candidates[idx]
        for idx in candidates:
            if field in candidates[idx]:
                candidates[idx] = [f for f in candidates[idx] if f != field]
    return assignment

def indices_for_departure_fields(assignment: Dict[int, str]) -> List[int]:
    res = []
    for idx in assignment:
        if assignment[idx].startswith('departure'):
            res.append(idx)
    return res

constraints, my_ticket, nearby_tickets = parse('16.in')
valid_nearby_tickets = []
invalid_number_per_ticket = []

for nearby_ticket in nearby_tickets:
    invalid_ticket = False
    for number in nearby_ticket:
        at_least_one_is_valid = False
        for constraint in constraints:
            res = evaluate_constraint(number, constraints[constraint])
            at_least_one_is_valid = at_least_one_is_valid or res
        if not at_least_one_is_valid:
                invalid_ticket = True
                invalid_number_per_ticket.append(number)
                break
    if not invalid_ticket:
        valid_nearby_tickets.append(nearby_ticket)
        

print("Solution to part one: " + str(sum(invalid_number_per_ticket)))

candidates = find_candidates(valid_nearby_tickets, constraints)

pprint.pprint(candidates)

assignment = find_assignment(candidates)

pprint.pprint(assignment)

print("Solution to part two: " + str(reduce(lambda x,y: x*y, map(lambda i: my_ticket[i], indices_for_departure_fields(assignment)))))
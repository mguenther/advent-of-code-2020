from typing import List


def solve_first_part(lines: List[str]):
    number_of_valid_lines = 0
    for line in lines:
        rule, content = line.split(':')
        min_max, symbol = rule.strip().split(' ')
        min, max = [int(t) for t in min_max.split('-')]
        occurences = len([c for c in content.strip() if c == symbol.strip()])
        if occurences >= min and occurences <= max:
            number_of_valid_lines += 1
    return number_of_valid_lines


def solve_second_part(lines: List[str]):
    number_of_valid_lines = 0
    for line in lines:
        rule, content = [token.strip() for token in line.split(':')]
        indices, symbol = rule.split(' ')
        first, second = [int(index)-1 for index in indices.split('-')]
        if content[first] == symbol and content[second] != symbol:
            number_of_valid_lines += 1
        if content[first] != symbol and content[second] == symbol:
            number_of_valid_lines += 1
    return number_of_valid_lines


lines = [l.strip() for l in open('2.in', 'r').readlines()]

print(solve_first_part(lines))
print(solve_second_part(lines))
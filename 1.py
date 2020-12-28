from typing import List


def solve_for_two(numbers: List[int]) -> int:
    for i in range(len(numbers)):
        for j in range(len(numbers)):
            if i == j:
                continue
            x, y = numbers[i], numbers[j]
            if x + y == 2020:
                return x * y


def solve_for_three(numbers: List[int]) -> int:
    for i in range(len(numbers)):
        for j in range(len(numbers)):
            for k in range(len(numbers)):
                if i == j and j == k:
                    continue
                x, y, z = numbers[i], numbers[j], numbers[k]
                if x + y + z == 2020:
                    return x * y * z


numbers = [int(line.strip()) for line in open('1.in', 'r').readlines()]

print(solve_for_two(numbers))
print(solve_for_three(numbers))

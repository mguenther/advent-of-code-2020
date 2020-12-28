from typing import Any, Callable, List


def memoize(function: Callable) -> Callable:
    from functools import wraps

    memo = {}

    @wraps(function)
    def wrapper(*args):
        if args in memo:
            return memo[args]
        else:
            rv = function(*args)
            memo[args] = rv
            return rv
    return wrapper


def candidates(joltage: int) -> List[int]:
    return range(joltage+1, joltage+4)


def solve_first_part() -> int:
    current_joltage = 0
    differences = {
      1: 0,
      2: 0,
      3: 1
    }

    for joltage in joltages:
        differences[candidates(current_joltage).index(joltage)+1] += 1
        current_joltage = joltage

    return differences[1] * differences[3]


def intersect(lst1: List[Any], lst2: List[Any]) -> List[Any]:
    return [value for value in lst1 if value in lst2]


@memoize
def solve_second_part(current_joltage: int) -> int:
    available_adapters = [a for a in joltages if a > current_joltage]
    if len(available_adapters) == 0:
        return 1
    compatible_adapters = intersect(candidates(current_joltage), available_adapters)
    sum = 0
    for adapter in compatible_adapters:
        sum += solve_second_part(adapter)
    return sum


joltages = [int(joltage) for joltage in open('10.in').readlines()]
joltages.sort()

print(solve_second_part(0))
joltages = [int(joltage) for joltage in open('10.in').readlines()]
joltages.sort()

def memoize(function):
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

def candidates(joltage):
    return range(joltage+1, joltage+4)

def firstPart():
    current_joltage = 0
    differences = {
      1: 0,
      2: 0,
      3: 1
    }

    for joltage in joltages:
        differences[candidates(current_joltage).index(joltage)+1] += 1
        current_joltage = joltage

    print differences
    print differences[1] * differences[3]

def intersect(lst1, lst2):
    return [value for value in lst1 if value in lst2]

@memoize
def secondPart(current_joltage):
    available_adapters = [a for a in joltages if a > current_joltage]
    if len(available_adapters) == 0:
        return 1
    compatible_adapters = intersect(candidates(current_joltage), available_adapters)
    sum = 0
    for adapter in compatible_adapters:
        sum += secondPart(adapter)
    return sum

print(secondPart(0))
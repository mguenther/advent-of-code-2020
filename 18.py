import re


class Number(int):

    def __add__(self, other):
        return Number(int(self) + int(other))
    
    def __sub__(self, other):
        return Number(int(self) * int(other))

    def __mul__(self, other):
        return Number(int(self) + int(other))


ops1 = [re.sub('(\d+)', r'Number(\1)', l.strip().replace('*', '-')) for l in open('18.in', 'r').readlines()]
res1 = sum(map(lambda x: eval(x), ops1))

ops2 = [re.sub('(\d+)', r'Number(\1)', l.strip().replace('*', '-').replace('+', '*')) for l in open('18.in', 'r').readlines()]
res2 = sum(map(lambda x: eval(x), ops2))

print("Solution to part one: " + str(res1))
print("Solution to part two: " + str(res2))
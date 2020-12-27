# Schreibe hier Deinen Code :-)

numbers = [int(line) for line in open('/home/pi/Documents/AdventOfCode/1.in', 'r').readlines()]

def solveForThree():
    for x in range(len(numbers)):
        for y in range(len(numbers)):
            for z in range(len(numbers)):
                if (x == y and y == z):
                    continue
                xn, yn, zn = numbers[x], numbers[y], numbers[z]
                if xn + yn + zn == 2020:
                    return xn * yn * zn

def solveForTwo():
    for l in range(len(numbers)):
        for r in range(len(numbers)):
            if l == r:
                continue
            ln, rn = numbers[l], numbers[r]
            if ln + rn == 2020:
                return ln * rn

print "Solution for 1st part: ", solveForTwo()
print "Solution for 2nd part: ", solveForThree()

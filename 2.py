

lines = open('/home/pi/Documents/AdventOfCode/2.in', 'r').readlines()

def solveFirstPart():
    number_of_valid_lines = 0
    for line in lines:
        rule, content = line.split(':')
        min_max, symbol = rule.strip().split(' ')
        min, max = [int(t) for t in min_max.split('-')]
        occurences = len([c for c in content.strip() if c == symbol.strip()])
        if occurences >= min and occurences <= max:
            number_of_valid_lines += 1
    print "Found " + str(number_of_valid_lines) + " valid lines (1st part) in the input."

def solveSecondPart():

    number_of_valid_lines = 0
    for line in lines:
        rule, content = [token.strip() for token in line.split(':')]
        indices, symbol = rule.split(' ')
        first, second = [int(index)-1 for index in indices.split('-')]

        if content[first] == symbol and content[second] != symbol:
            number_of_valid_lines += 1
        if content[first] != symbol and content[second] == symbol:
            number_of_valid_lines += 1
    print "Found " + str(number_of_valid_lines) + " valid lines (2nd part) in the input."

solveFirstPart()
solveSecondPart()
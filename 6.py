from collections import defaultdict


def solveFirstPart():

    sum = 0
    questionnaire = {}

    for line in open('/home/pi/Documents/AdventOfCode/6.in', 'r'):
        if not line.strip():
            sum += len(questionnaire)
            questionnaire = {}
        else:
            for c in line.strip():
                questionnaire[c] = 1

    return sum

def solveSecondPart():

    sum = 0
    questionnaire = defaultdict(lambda: 0)
    group_size = 0

    for line in open('/home/pi/Documents/AdventOfCode/6.in', 'r'):
        if not line.strip():
            for question in questionnaire.keys():
                if questionnaire[question] == group_size:
                        sum += 1
            questionnaire = defaultdict(lambda: 0)
            group_size = 0
        else:
            for c in line.strip():
                occurences_of_c = questionnaire[c] + 1
                questionnaire[c] = occurences_of_c
            group_size += 1
    return sum

print "Solution to first part: " + str(solveFirstPart())
print "Solutions to second part: " + str(solveSecondPart())
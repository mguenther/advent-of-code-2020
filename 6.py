from collections import defaultdict


def solve_first_part() -> int:

    sum = 0
    questionnaire = {}

    for line in open('6.in', 'r'):
        if not line.strip():
            sum += len(questionnaire)
            questionnaire = {}
        else:
            for c in line.strip():
                questionnaire[c] = 1

    return sum


def solve_second_part() -> int:

    sum = 0
    questionnaire = defaultdict(lambda: 0)
    group_size = 0

    for line in open('6.in', 'r'):
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


print(solve_first_part())
print(solve_second_part())
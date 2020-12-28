from typing import List


def solve_first_part(prog: List[str]) -> int:

    ip = 0
    acc = 0
    seen = set()

    while True:
        if ip in seen:
            return(acc)
        seen.add(ip)
        ins = prog[ip]
        operator, operand = ins.split(' ')
        if operator == 'nop':
            ip += 1
        elif operator == 'acc':
            acc += int(operand)
            ip += 1
        elif operator == 'jmp':
            ip += int(operand)


def solve_second_part(prog: List[str]) -> int:

    max_instructions_per_changed_program = 1000

    for incIp in range(len(prog)):
        modifiedProg = list(prog)
        if modifiedProg[incIp].split(' ')[0] == 'jmp':
            modifiedProg[incIp] = 'nop ' + modifiedProg[incIp].split(' ')[1]
        elif modifiedProg[incIp].split(' ')[0] == 'nop':
            modifiedProg[incIp] = 'jmp ' + modifiedProg[incIp].split(' ')[1]
        else:
            continue

        ip = 0
        acc = 0
        executed_instructions = 0

        while 0 <= ip < len(modifiedProg) and executed_instructions < max_instructions_per_changed_program:
            ins = modifiedProg[ip]
            operator, operand = ins.split(' ')
            executed_instructions += 1
            if operator == 'nop':
                ip += 1
            elif operator == 'acc':
                acc += int(operand)
                ip += 1
            elif operator == 'jmp':
                ip += int(operand)
        if ip >= len(modifiedProg):
            return acc


print(solve_first_part(open('8.in', 'r').readlines()))
print(solve_second_part(open('8.in', 'r').readlines()))
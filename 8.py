prog = open('8.in', 'r').readlines()

def solvePartOne():

    ip = 0
    acc = 0
    seen = set()

    while True:
        if ip in seen:
            print acc
            print last_jump_ip
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

def solvePartTwo():

    max_instructions_per_changed_program = 1000

    for incIp in range(len(prog)):
        modifiedProg = list(prog)
        if modifiedProg[incIp].split(' ')[0] == 'jmp':
            print "Changing " + modifiedProg[incIp] + " to nop " + modifiedProg[incIp].split(' ')[1] + " in line " + str(incIp) + "."
            modifiedProg[incIp] = 'nop ' + modifiedProg[incIp].split(' ')[1]
        elif modifiedProg[incIp].split(' ')[0] == 'nop':
            print "Changing " + modifiedProg[incIp] + " to jmp " + modifiedProg[incIp].split(' ')[1] + " in line " + str(incIp) + "."
            modifiedProg[incIp] = 'jmp ' + modifiedProg[incIp].split(' ')[1]
        else:
            print "No change for line " + str(incIp) + "."
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
            print "IP: ", ip
            print "length: ", len(modifiedProg)
            return acc

print solvePartTwo()
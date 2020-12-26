def partOne():

    pos = (0, 0) # N/S, W/E
    face = 'E'
    faces = ['N', 'E', 'S', 'W']

    for instruction in [l for l in open('12.in').readlines()]:
        operator = instruction[0]
        operand = int(instruction[1:])
        if operator == 'F':
            if face == 'E':
                pos = (pos[0], pos[1] + operand)
            elif face == 'W':
                pos = (pos[0], pos[1] - operand)
            elif face == 'N':
                pos = (pos[0] - operand, pos[1])
            elif face == 'S':
                pos = (pos[0] + operand, pos[1])
        elif operator == 'N':
            pos = (pos[0] - operand, pos[1])
        elif operator == 'S':
            pos = (pos[0] + operand, pos[1])
        elif operator == 'E':
            pos = (pos[0], pos[1] + operand)
        elif operator == 'W':
            pos = (pos[0], pos[1] - operand)
        elif operator == 'L':
            face = faces[(faces.index(face) - (operand / 90)) % len(faces)]
        elif operator == 'R':
            face = faces[(faces.index(face) + (operand / 90)) % len(faces)]

    print("Position: ", pos)
    print("Manhattan distance: ", (abs(pos[0]) + abs(pos[1])))

def partTwo():

    pos = (0, 0) # N/S, W/E
    waypoint = (-1, 10) # N/S, W/E
    face = 'E'
    faces = ['N', 'E', 'S', 'W']

    for instruction in [l for l in open('12.in').readlines()]:
        operator = instruction[0]
        operand = int(instruction[1:])
        if operator == 'F':
            pos = (pos[0] + waypoint[0] * operand, pos[1] + waypoint[1] * operand)
        elif operator == 'N':
            waypoint = (waypoint[0] - operand, waypoint[1])
        elif operator == 'S':
            waypoint = (waypoint[0] + operand, waypoint[1])
        elif operator == 'E':
            waypoint = (waypoint[0], waypoint[1] + operand)
        elif operator == 'W':
            waypoint = (waypoint[0], waypoint[1] - operand)
        elif operator == 'L':
            times = operand / 90
            for i in range(times):
                waypoint = (-1 * waypoint[1], waypoint[0])
        elif operator == 'R':
            times = operand / 90
            for i in range(times):
                waypoint = (waypoint[1], -1 * waypoint[0])

    print("Position: ", pos)
    print("Manhattan distance: ", (abs(pos[0]) + abs(pos[1])))

partTwo()
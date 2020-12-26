import sys


def solvePartOne():

    def earliest_departure_by_bus(bus, left, right):
        return [i % bus for i in range(left, right+1)].index(0)

    lines = [l for l in open('13.in').readlines()]
    earliest_departure_at = int(lines[0].strip())
    schedule = [int(bus) for bus in lines[1].strip().split(',') if bus != 'x']
    left, right = earliest_departure_at, earliest_departure_at + max(schedule)
    earliest_departures = { bus: earliest_departure_by_bus(bus, left, right) for bus in schedule}
    bus, waiting = min(earliest_departures.items(), key=lambda x: x[1])
    print(bus, waiting)
    print(bus * waiting)

schedule = [bus for bus in [l for l in open('13.in').readlines()][1].strip().split(',')]

# We build up the solution by solving the relation between the first two
# busses by looking for their intersecting timestamp. Multiples of this
# intersecting timestamp will always retain the same relationship between
# the first two busses. Now, we look for an multiple (respecting the offset,
# of course!) of that timestamp that conforms also with th next bus (and so on),
# adjusting timestamps on the way. Due to the fact that the bus schedules are
# prime, we are guaranteed to get the earliest solution that respects all busses
# using this approach.
def solvePartTwo(schedule):
    schedule_with_indices = [(offset, int(bus)) for offset, bus in enumerate(schedule) if bus != 'x']
    timestamp = 0
    lcm = 1
    for offset, bus in schedule_with_indices:
        while (timestamp + offset) % bus != 0:
            timestamp += lcm
        lcm *= bus
    return timestamp

print(solvePartTwo(schedule))

# This was my first solution which iteratively increases the lowest bus
# offset until we found a solution that satisfies timestampes for all busses.
# This runs slow for the samples (up to 10-30 seconds) and becomes unbearable
# if we run this against the input data (it will take hours on a fast machine).
def solvePartTwoTooSlow(schedule):
    while True:

        bus, smallest_departure_at = min(schedule, key=lambda x: x[1])
        index = schedule.index((bus, smallest_departure_at))
        if (bus == 'x'):
            schedule[index] = (bus, sys.maxsize)
        else:
            schedule[index] = (bus, smallest_departure_at + int(bus))

        is_contiguous = True
        departure_at = schedule[0][1]
        for i in range(1, len(schedule)):
            if schedule[i][0] == 'x':
                continue
            _, next_departure = schedule[i]
            if next_departure - i == departure_at:
                continue
            else:
                is_contiguous = False
                break
        if is_contiguous:
            print(departure_at)
            sys.exit(0)
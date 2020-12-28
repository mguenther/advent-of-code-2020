import numpy as np


def initial_assignment():
    assignment = np.zeros(rows * cols).reshape(rows, cols)
    for row in range(rows):
        for col in range(cols):
            assignment[row][col] = T[lines[row][col]]
    return assignment


def occupied_seats_part_two(row, col, assignment):
    occupied_seats = 0
    for delta_row in directions:
        for delta_col in directions:
            if delta_row == 0 and delta_col == 0:
                continue
            probe_row, probe_col = row + delta_row, col + delta_col
            while probe_row >= 0 and probe_row < rows and probe_col >= 0 and probe_col < cols:
                if assignment[probe_row][probe_col] == T['#']:
                    occupied_seats += 1
                    break
                elif assignment[probe_row][probe_col] == T['L']:
                    break
                else:
                    probe_row, probe_col = probe_row + delta_row, probe_col + delta_col
    return occupied_seats


def occupied_seats_adjacent_to(row, col, assignment):
    occupied_seats = 0
    for delta_row in directions:
        for delta_col in directions:
            if delta_row == 0 and delta_col == 0:
                continue
            probe_row, probe_col = row + delta_row, col + delta_col
            if probe_row < 0 or probe_row >= rows:
                continue
            if probe_col < 0 or probe_col >= cols:
                continue
            if assignment[probe_row][probe_col] == T['#']:
                occupied_seats += 1
    return occupied_seats


def next_assignment(assignment):
    new_assignment = np.zeros(rows * cols).reshape(rows, cols)
    number_of_changes = 0
    for row in range(rows):
        for col in range(cols):
            occupied_seats = occupied_seats_part_two(row, col, assignment)
            if assignment[row][col] == T['L'] and occupied_seats == 0:
                new_assignment[row][col] = T['#']
                number_of_changes += 1
            elif assignment[row][col] == T['#'] and occupied_seats >= 5:
                new_assignment[row][col] = T['L']
                number_of_changes += 1
            else:
                new_assignment[row][col] = assignment[row][col]
    assignment = new_assignment
    return (new_assignment, number_of_changes)


def find_fixpoint_assignment(assignment):
    while True:
        assignment, number_of_changes = next_assignment(assignment)
        if (number_of_changes == 0):
            # we have reached the fixpoint
            return assignment


def total_number_of_occupied_seats(assignment):
    t = 0
    for row in range(rows):
        for col in range(cols):
            if assignment[row][col] == T['#']:
                t += 1
    return t


T = {
    'L': 1.0,
    '.': 2.0,
    '#': 3.0
}

directions = [-1, 0, +1]

lines = [l.strip() for l in open('11.in', 'r').readlines()]

rows = len(lines)
cols = len(lines[0])

print(total_number_of_occupied_seats(find_fixpoint_assignment(initial_assignment())))
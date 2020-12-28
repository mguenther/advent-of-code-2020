# This solution works with Python 2.7. It won't give you the correct result
# if you use Python 3.x.

def lower_half(rows):
    l, r = rows
    return (l, l + (r - l) / 2)


def upper_half(rows):
    l, r = rows
    return (l + 1 + (r - l) / 2, r)


def find_row(boarding_code):
    row = 0
    rows = (0, 127)
    direction = boarding_code[0]
    for i in range(0, 7):
        direction = boarding_code[i]
        if direction == 'F':
            rows = lower_half(rows)
            row = rows[0]
        elif direction == 'B':
            rows = upper_half(rows)
            row = rows[1]
    return row


def find_column(boarding_code):
    column = 0
    columns = (0, 7)
    direction = boarding_code[7]
    for i in range(7, 10):
        direction = boarding_code[i]
        if direction == 'L':
            columns = lower_half(columns)
            column = columns[0]
        elif direction == 'R':
            columns = upper_half(columns)
            column = columns[1]
    return column


def find_seat(boarding_code):
    return find_row(boarding_code) * 8 + find_column(boarding_code)


def highest_seat_id(list_of_boarding_codes):
    highest = 0
    for boarding_code in list_of_boarding_codes:
        seat_id = find_seat(boarding_code)
        if seat_id > highest:
            highest = seat_id
    return highest


def missing_seat_id(list_of_boarding_codes):
    seat_ids = [find_seat(boarding_code) for boarding_code in list_of_boarding_codes]
    seat_ids.sort()
    missing = 0
    l = seat_ids[0]
    for i in range(1, len(seat_ids)):
        if seat_ids[i] - l > 1:
            missing = seat_ids[i] - 1
            break
        l = seat_ids[i]
    return missing


list_of_boarding_codes = [b.strip() for b in open('5.in', 'r').readlines()]
print(highest_seat_id(list_of_boarding_codes))
print(missing_seat_id(list_of_boarding_codes))
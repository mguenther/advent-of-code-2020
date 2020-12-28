from typing import Callable, Dict


def skip_validation(value: str) -> bool:
    return True


def is_valid_birth_year(value: str) -> bool:
    birth_year = int(value)
    return birth_year >= 1920 and birth_year <= 2002


def is_valid_issue_year(value: str) -> bool:
    issue_year = int(value)
    return issue_year >= 2010 and issue_year <= 2020


def is_valid_expiration_year(value: str) -> bool:
    expiration_year = int(value)
    return expiration_year >= 2020 and expiration_year <= 2030


def is_valid_height(value: str) -> bool:
    is_valid = False
    if value.endswith('cm'):
        height = int(value.split('cm')[0])
        is_valid = height >= 150 and height <= 193
    elif value.endswith('in'):
        height = int(value.split('in')[0])
        is_valid = height >= 59 and height <= 76
    return is_valid


def is_valid_hair_color(value: str) -> bool:
    is_valid = True
    if value.startswith('#'):
        color_code = value.split('#')[1]
        for c in color_code:
            is_valid = is_valid and c in '0123456789abcdef'
    else:
        is_valid = False
    return is_valid


def is_valid_eye_color(value: str) -> bool:
    return value in ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']


def is_valid_passport_id(value: str) -> bool:
    is_valid = len(value) == 9
    for c in value:
        is_valid = is_valid and c in '0123456789'
    return is_valid


def number_of_valid_passports(rules: Dict[str, Callable]) -> int:
    passport = {}
    nvalid = 0
    for line in open('4.in', 'r'):
        if not line.strip():
            # end-of-passport or end-of-file
            valid = True
            for field in ['ecl', 'pid', 'eyr', 'hcl', 'byr', 'iyr', 'hgt']:
                if field not in passport or not rules[field](passport[field]):
                    valid = False
            if valid:
                nvalid += 1
            passport = {}
        else:
            attrs = line.strip().split(' ')
            for attr in attrs:
                key, value = attr.split(':')
                passport[key] = value
    return nvalid


VALIDATION_FOR_FIRST = {
    'ecl': skip_validation,
    'pid': skip_validation,
    'eyr': skip_validation,
    'hcl': skip_validation,
    'byr': skip_validation,
    'iyr': skip_validation,
    'hgt': skip_validation
}

VALIDATION_FOR_SECOND = {
    'ecl': is_valid_eye_color,
    'pid': is_valid_passport_id,
    'eyr': is_valid_expiration_year,
    'hcl': is_valid_hair_color,
    'byr': is_valid_birth_year,
    'iyr': is_valid_issue_year,
    'hgt': is_valid_height
}

print(number_of_valid_passports(VALIDATION_FOR_FIRST))
print(number_of_valid_passports(VALIDATION_FOR_SECOND))
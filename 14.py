from functools import reduce
from typing import List

import re
import sys


def apply_bitmask(value: int, bitmask: str) -> int:
    v = value
    for i,b in enumerate(bitmask):
        if b == 'X':
            continue
        elif b == '1':
            if (v >> (35 - i)) & 0b1 == 0:
                v += 1 << (35 - i)
        elif b == '0':
            if (v >> (35 - i)) & 0b1 == 1:
                v -= 1 << (35 - i)
    return v


def decoder_version_1(lines: List[str]) -> int:
    
    progmem = {}
    bitmask = 'X' * 36

    for line in lines:
        if line.startswith('mem'):
            address, value = regex_mem.findall(line)[0]
            progmem[int(address)] = apply_bitmask(int(value), bitmask)
        elif line.startswith('mask'):
            bitmask = regex_msk.findall(line)[0]
        else:
            print("Unrecognized operation: ", line)
            sys.exit(1)

    return sum(progmem.values())


def generate(mask: str, i: int = 0) -> List[str]:
    for j in range(i, len(mask)):
        if mask[j] == 'X':
            return reduce(list.__add__, [
                generate(mask[:j] + '0' + mask[j+1:], j+1),
                generate(mask[:j] + '1' + mask[j+1:], j+1)
            ])
    return [mask]


def decoder_version_2(lines: List[str]) -> int:

    progmem = {}
    bitmask = '0' * 36

    for line in lines:
        if line.startswith('mem'):
            address, value = regex_mem.findall(line)[0]
            address = '{0:b}'.format(int(address))
            address = '0' * (36-len(address)) + address
            address_mask = []
            for a, b in zip(address, bitmask):
                if b == '0':
                    address_mask.append(a)
                elif b == '1':
                    address_mask.append('1')
                else:
                    address_mask.append('X')
            for generated_address in generate("".join(address_mask)):
                progmem[generated_address] = int(value)
        elif line.startswith('mask'):
            bitmask = regex_msk.findall(line)[0]
        else:
            print("Unrecognized operation: ", line)
            sys.exit(1)

    return sum(progmem.values())


lines = [l.strip() for l in open('14.in', 'r').readlines()]

regex_mem = re.compile('mem\[([0-9]+)\] = ([0-9]+)')
regex_msk = re.compile('mask = ([01X]{36})')

print(decoder_version_1(lines))
print(decoder_version_2(lines))
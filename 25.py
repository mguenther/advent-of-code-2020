def transform(subject_number, loop_size):
    return pow(subject_number, loop_size, 20201227)
    # Fast Exponentiation (still too slow):
    #if loop_size == 0:
    #    return 1
    #elif loop_size % 2 == 0:
    #    return transform((subject_number ** 2) % 20201227, loop_size / 2)
    #else:
    #    return (subject_number * transform(subject_number, loop_size - 1)) % 20201227
    # Naive version (way to slow!):
    # v = 1
    # for _ in range(loop_size):
    #     v *= subject_number
    #     rem = v % 20201227
    #     v = rem
    # return v


def determine_loop_size(public_key):
    loop_size = 1
    while transform(7, loop_size) != public_key:
        loop_size += 1
    return loop_size


public_key_1, public_key_2 = 11239946, 10464955
loop_size_2 = determine_loop_size(public_key_2)
encryption = transform(public_key_1, loop_size_2)
print(encryption)
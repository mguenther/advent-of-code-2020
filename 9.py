params = {
    'window_size': 25,
    'file': '9.in'
}

numbers = [int(n) for n in open(params['file'], 'r').readlines()]

def find_invalid_number(numbers):
    for i in range(len(numbers)-params['window_size']):
        window = numbers[i:i+params['window_size']]
        probe = numbers[i+params['window_size']]
        probe_valid = False
        for j in range(len(window)):
            for k in range(len(window)):
                if j == k:
                    continue
                if window[j] + window[k] == probe:
                    probe_valid = True
        if not probe_valid:
            # we found the first number that is not the sum of any pair of numbers
            # in the window of previously seen numbers
            return probe

def find_encryption_weakness(invalid_number, numbers):
    for window_size in range(2, len(numbers)):
        for i in range(len(numbers)-window_size):
            window = numbers[i:i+window_size]
            if sum(window) == invalid_number:
                return min(window) + max(window)

print(find_encryption_weakness(find_invalid_number(numbers), numbers))
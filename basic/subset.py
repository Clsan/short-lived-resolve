array = [1, 2, 3, 4, 5, 6]


def convert(num):
    s = str(bin(num))[2:]
    return '0' * (len(array) - len(s)) + s


assert convert(2) == '000010'
assert convert(5) == '000101'
assert convert(16) == '010000'


def calculate_subset(binary_string):
    subset = []
    for i in range(0, len(array)):
        if binary_string[i] == '1':
            subset.append(array[i])
    return subset


assert calculate_subset('000010') == [5]
assert calculate_subset('000101') == [4, 6]
assert calculate_subset('010000') == [2]

for i in range(0, 2**len(array)):
    print(calculate_subset(convert(i)))

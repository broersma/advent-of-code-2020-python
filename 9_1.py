import little_helper
from itertools import combinations

def answer(input, pre_size=25):
    """
    >>> answer('''35
    ... 20
    ... 15
    ... 25
    ... 47
    ... 40
    ... 62
    ... 55
    ... 65
    ... 95
    ... 102
    ... 117
    ... 150
    ... 182
    ... 127
    ... 219
    ... 299
    ... 277
    ... 309
    ... 576''', pre_size=5)
    127
    """
    lines = [int(line) for line in input.split('\n')]

    start = pre_size
    preamble = lines[:pre_size]
    for i in range(0, len(lines) - pre_size):
        preamble = lines[i:i+pre_size]
        number = lines[i+pre_size]
        if not any(sum(combo) == number for combo in combinations(preamble, 2)):
            return number


if __name__ == '__main__':
    little_helper.help(2020, __file__, answer)

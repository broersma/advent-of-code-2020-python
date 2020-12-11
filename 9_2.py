import little_helper
from collections import deque
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
    62
    """
    lines = [int(line) for line in input.split('\n')]

    start = pre_size
    preamble = lines[:pre_size]
    the_number = 0
    for i in range(0, len(lines) - pre_size):
        preamble = lines[i:i+pre_size]
        number = lines[i+pre_size]
        if not any(sum(combo) == number for combo in combinations(preamble, 2)):
            the_number = number
            break

    numbers = deque()
    for num in lines:
        numbers.append(num)
        while sum(numbers) > the_number:
            numbers.popleft()
        if sum(numbers) == the_number:
            return min(numbers) + max(numbers)


if __name__ == '__main__':
    little_helper.help(2020, __file__, answer)

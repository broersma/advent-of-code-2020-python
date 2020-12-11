import little_helper

from collections import defaultdict


def answer(input):
    """
    >>> answer('''16
    ... 10
    ... 15
    ... 5
    ... 1
    ... 11
    ... 7
    ... 19
    ... 6
    ... 12
    ... 4''')
    35
    """
    lines = sorted(int(line) for line in input.split('\n'))

    lines = [0] + lines
    lines.append(lines[-1] + 3)

    diffs = defaultdict(int)
    for a,b in zip(lines[:-1], lines[1:]):
        diffs[b-a] += 1

    return diffs[1] * diffs[3]


if __name__ == '__main__':
    little_helper.help(2020, __file__, answer)

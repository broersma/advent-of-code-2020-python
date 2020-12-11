import little_helper
from collections import defaultdict


def answer(input):
    """
    >>> answer('''nop +0
    ... acc +1
    ... jmp +4
    ... acc +3
    ... jmp -3
    ... acc -99
    ... acc +1
    ... jmp -4
    ... acc +6''')
    5
    """
    lines = input.split('\n')

    visited = defaultdict(int)
    current = 0
    acc = 0

    while True:
        if visited[current] == 1:
            break
        visited[current] += 1
        op, value = lines[current].split(' ', 1)
        value = int(value)
        if op == 'nop':
            current += 1
        elif op == 'acc':
            acc += value
            current += 1
        elif op == 'jmp':
            current += value

    return acc


if __name__ == '__main__':
    little_helper.help(2020, __file__, answer)

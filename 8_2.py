import little_helper
from collections import defaultdict


def flip_op(op):
    if op[0] == 'nop':
        return ('jmp', op[1])
    elif op[0] == 'jmp':
        return ('nop', op[1])

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
    8
    """
    lines = input.split('\n')


    ops = [(line.split(' ', 1)[0], int(line.split(' ', 1)[1])) for line in lines]

    changed = -1

    while True:
        i = 1
        while True:
            if ops[changed+i][0] in ['nop', 'jmp']:
                if changed != -1:
                    ops[changed] = flip_op(ops[changed])
                changed = changed+i
                ops[changed] = flip_op(ops[changed])
                break
            i+=1

        visited = defaultdict(int)
        current = 0
        acc = 0
        while True:
            if current == len(ops):
                return acc
            if visited[current] == 1:
                break
            visited[current] += 1
            op, value = ops[current]
            if op == 'nop':
                current += 1
            elif op == 'acc':
                acc += value
                current += 1
            elif op == 'jmp':
                current += value


if __name__ == '__main__':
    little_helper.help(2020, __file__, answer)

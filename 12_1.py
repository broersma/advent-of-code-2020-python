import little_helper


def answer(input):
    """
    >>> answer('''F10''')
    10
    >>> answer('''N3''')
    3
    >>> answer('''E3''')
    3
    >>> answer('''S3''')
    3
    >>> answer('''W3''')
    3
    >>> answer('''R90
    ... F5
    ... N5''')
    0
    >>> answer('''L90
    ... F5
    ... S5''')
    0
    >>> answer('''L270
    ... F5
    ... N5''')
    0
    >>> answer('''L180
    ... F5
    ... N5''')
    10
    >>> answer('''F10
    ... N3
    ... F7
    ... R90
    ... F11''')
    25
    >>> answer('''L90
    ... F5
    ... S10''')
    5
    >>> answer('''L180
    ... F5
    ... S10''')
    15
    >>> answer('''L270
    ... F5
    ... S10''')
    15
    >>> answer('''R90
    ... F5
    ... S10''')
    15
    >>> answer('''R180
    ... F5
    ... S10''')
    10
    >>> answer('''R270
    ... F5
    ... S10''')
    5
    """
    lines = input.split('\n')

    dx = 1
    dy = 0
    posx = 0
    posy = 0

    for line in lines:
        command = line[0]
        amount = int(line[1:])
        if command == 'F':
            for i in range(amount):
                posx += dx
                posy += dy
        if command == 'R' or command == 'L':
            if command == 'L':
                amount = 90 if amount == 270 else 270 if amount == 90 else 180
            if amount == 90:
                if dx == 0 and dy == 1:
                    dx = 1
                    dy = 0
                elif dx == 1 and dy == 0:
                    dx = 0
                    dy = -1
                elif dx == 0 and dy == -1:
                    dx = -1
                    dy = 0
                elif dx == -1 and dy == 0:
                    dx = 0
                    dy = 1
            if amount == 180:
                dx = -dx
                dy = -dy
            if amount == 270:
                if dx == 0 and dy == 1:
                    dx = -1
                    dy = 0
                elif dx == 1 and dy == 0:
                    dx = 0
                    dy = 1
                elif dx == 0 and dy == -1:
                    dx = 1
                    dy = 0
                elif dx == -1 and dy == 0:
                    dx = 0
                    dy = -1
        if command == 'N':
            posy += amount
        if command == 'S':
            posy -= amount
        if command == 'E':
            posx += amount
        if command == 'W':
            posx -= amount
    return abs(posx)+abs(posy)


if __name__ == '__main__':
    little_helper.help(2020, __file__, answer)

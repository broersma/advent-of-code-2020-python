import little_helper
import math


def answer(input):
    """
    >>> answer('''F10
    ... N3
    ... F7
    ... R90
    ... F11''')
    286
    """
    lines = input.split('\n')

    dx = 10
    dy = 1
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
            if command == 'R':
                amount = 90 if amount == 270 else 270 if amount == 90 else 180

            theta = math.pi * amount / 180
            dx, dy = (round(dx * math.cos(theta) - dy * math.sin(theta)), round(dy * math.cos(theta) + dx * math.sin(theta)))
        if command == 'N':
            dy += amount
        if command == 'S':
            dy -= amount
        if command == 'E':
            dx += amount
        if command == 'W':
            dx -= amount
    return abs(posx)+abs(posy)


if __name__ == '__main__':
    little_helper.help(2020, __file__, answer)

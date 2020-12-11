import little_helper


FLOOR = 0
EMPTY = 1
OCCUPIED = 2


def num_occupied_neighbor_seats(seats, y, x):
    count = 0
    for ddy in (-1, 0, 1):
        for ddx in (-1, 0, 1):
            if not (ddy == 0 and ddx == 0):
                dy = 0
                dx = 0
                while True:
                    dy += ddy
                    dx += ddx
                    if 0 <= y+dy < len(seats) and 0 <= x+dx < len(seats[0]):
                        if seats[y+dy][x+dx] == OCCUPIED:
                            count += 1
                            break
                        elif seats[y+dy][x+dx] == EMPTY:
                            break
                    else:
                        break
    return count

def answer(input):
    """
    >>> answer('''L.L
    ... L..''')
    3
    >>> answer('''L.LL.LL.LL
    ... LLLLLLL.LL
    ... L.L.L..L..
    ... LLLL.LL.LL
    ... L.LL.LL.LL
    ... L.LLLLL.LL
    ... ..L.L.....
    ... LLLLLLLLLL
    ... L.LLLLLL.L
    ... L.LLLLL.LL''')
    26
    """
    seats = [[EMPTY if c == 'L' else FLOOR for c in line] for line in input.split('\n')]

    changed = True
    while changed:
        changed = False
        new_seats = [[FLOOR]*len(seats[0]) for i in range(len(seats))]
        for y in range(len(seats)):
            for x in range(len(seats[0])):
                status = seats[y][x]
                if status == EMPTY:
                    if num_occupied_neighbor_seats(seats, y, x) == 0:
                        new_seats[y][x] = OCCUPIED
                        changed = True
                    else:
                        new_seats[y][x] = EMPTY
                elif status == OCCUPIED:
                    if num_occupied_neighbor_seats(seats, y, x) >= 5:
                        new_seats[y][x] = EMPTY
                        changed = True
                    else:
                        new_seats[y][x] = OCCUPIED
                else:
                    new_seats[y][x] = FLOOR
        seats = new_seats

    count = 0
    for y in range(len(seats)):
        for x in range(len(seats[0])):
            status = seats[y][x]
            if status == OCCUPIED:
                count += 1
    return count


if __name__ == '__main__':
    little_helper.help(2020, __file__, answer)

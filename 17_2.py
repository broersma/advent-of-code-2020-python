import little_helper

def neighbors(cube):
    """
    >>> len(list(neighbors((0,0,0,0))))
    80
    """
    x,y,z,w = cube
    for dx in range(-1, 2):
        for dy in range (-1, 2):
            for dz in range(-1, 2):
                for dw in range(-1, 2):
                    if (dx,dy,dz,dw) != (0,0,0,0):
                        yield (x+dx, y+dy, z+dz, w+dw)

def get_num_active_neighbors(cube, active_cubes):
    return len(list(neighbor for neighbor in neighbors(cube) if neighbor in active_cubes))


def answer(input):
    """
    >>> answer('''.#.
    ... ..#
    ... ###''')
    848
    """
    lines = input.split('\n')

    active_cubes = set()
    z = 0
    w = 0
    for y, line in enumerate(lines):
        for x, ch in enumerate(line):
            if ch == '#':
                active_cubes.add((x,y,z,w))

    for i in range(6):
        cubes_to_check = set()
        for active_cube in active_cubes:
            cubes_to_check.add(active_cube)
            cubes_to_check.update(neighbors(active_cube))

        new_active_cubes = set()
        for cube in cubes_to_check:
            if cube in active_cubes:
                if get_num_active_neighbors(cube, active_cubes) in (2, 3):
                    new_active_cubes.add(cube)
            else:
                if get_num_active_neighbors(cube, active_cubes) == 3:
                    new_active_cubes.add(cube)
        active_cubes = new_active_cubes
    return len(active_cubes)


if __name__ == '__main__':
    little_helper.help(2020, __file__, answer)

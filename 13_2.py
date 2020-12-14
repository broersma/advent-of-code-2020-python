import little_helper


def answer(input):

    """
    >>> answer('''
    ... 2,3,5''')
    8
    >>> answer('''
    ... 2,3''')
    2
    >>> answer('''
    ... 2,x,3''')
    4
    >>> answer('''
    ... 2,x,x,3''')
    0
    >>> answer('''
    ... 3,2''')
    3
    >>> answer('''
    ... 3,x,2''')
    0
    >>> answer('''
    ... 3,x,x,2''')
    3
    >>> answer('''
    ... 3,5''')
    9
    >>> answer('''
    ... 5,3''')
    5
    >>> answer('''
    ... 17,x,13,19''')
    3417
    >>> answer('''
    ... 7,13,x,x,59,x,31,19''')
    1068781
    >>> answer('''
    ... 67,7,59,61''')
    754018
    >>> answer('''
    ... 67,x,7,59,61''')
    779210
    >>> answer('''
    ... 1789,37,47,1889''')
    1202161486
    """
    lines = input.split('\n')

    b = lines[1].split(",")

    z = sorted([(-t%int(i),int(i)) for t,i in enumerate(b) if i != 'x'], key=lambda x:x[1], reverse=False)

    start = z[0][0]
    step = z[0][1]
    current = start
    num = 2
    while True:
        zzz = set((current-t)%int(i) for t,i in z[:num])
        if len(zzz) == 1:
            if num < len(z):
                step *= z[num-1][1]
                num += 1
            else:
                return current
        current += step



if __name__ == '__main__':
    little_helper.help(2020, __file__, answer)

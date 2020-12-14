import little_helper
from functools import reduce


def getstart(aa, bb):
    """

    """
    i,a = aa
    j,b = bb
    return j + (((b*i+j) % a) * b)


def getmod(a,b):
    """
    >>> getmod(2,3)
    6
    >>> getmod(3,5)
    15
    >>> getmod(2,4)
    4
    >>> getmod(3,6)
    6
    >>> getmod(3,6)
    6
    """
    if b % a == 0:
        return b
    return a*b

def combine(aa, bb):
    """
    >>> combine((0,5), (0,2))
    (0, 10)
    >>> combine((0,5), (1,2))
    (5, 10)
    >>> combine((0,5), (2,3))
    (5, 15)
    >>> combine((2,3), (0,5))
    (5, 15)
    """


    i,a = aa
    j,b = bb
    if a > b:
        aa, bb = bb, aa
    start = getstart(aa, bb)
    mod = getmod(a, b)
    return (start, mod)

#a = 3
#b = 5
#for i in range(a):
#    for j in range(b):
#        print(f"a={a}, i={i}, b={b}, j={j},  x={combine((i,a),(j,b))}")
#
#print()
#
#a = 5
#b = 3
#for i in range(a):
#    for j in range(b):
#        x = combine((j,b),(i,a))
#        x_w = combine((i,a),(j,b))
#        x_j = x[0]-i
#        x_mb = x_j / 5
#        print(f"a={a}, i={i}, b={b}, j={j}, x={x}, x-j={x_j}, x/b={x_mb}, x[wrong]={x_w[0]} should be x={x[0]}")


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
    #print(z)

    #a = reduce(combine, z)
    #print(a)
    #return a[0]
    #print(z)

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
    return
    #   # s = set((x+t)%int(i) for t,i in z)
    #    if len(s) == 1:
    #        return x

    """
    print('   ', end='')
    for j in [2,3,5,7,11,13,17]:
        print(str(j).rjust(2), end='')
    print()
    for i in range(11*13+1):
        print(str(i).ljust(3), end='')
        for j in [2,3,5,7,11,13,17]:
            if (i+0)%j == 0:
                print(" X", end='')
            else:
                print(" .", end='')
        print()

    return

    max = z[0]
    step = max[1]
    t = 0

    while True:
        x = y - max_t
        s = set((x+t)%int(i) for t,i in z)
        if len(s) == 1:
            return x
        t += step


    print(z)
    """


    max_t, max_id = max(((int(i)-t, int(i)) for (t, i) in z), key=lambda x: x[1])
    #start = reduce(lambda x,y: x*y, (x[1] for x in z), 1)
    #print(start)
    y = 0
    #for x in range(start, )
    while True:
        #s = set((f"({x}+{t})%{int(i)}", (x+t)%int(i)) for t,i in enumerate(b) if i != 'x')
        x = y - max_t
        s = set((x+t)%int(i) for t,i in z)
        if len(s) == 1:
            return x
        y += max_id



if __name__ == '__main__':
    little_helper.help(2020, __file__, answer)

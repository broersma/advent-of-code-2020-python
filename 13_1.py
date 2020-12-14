import little_helper

# defaultdict(list), defaultdict(int), deque.rotate/append
from collections import defaultdict, deque
# functools.reduce(function, iterable[, initializer])
from functools import reduce
# islice(seq, [start,] stop [, step])
from itertools import islice
import re
#import networkx as nx
#from numba import jit
from sys import exit


def answer(input):
    """
    >>> answer('''939
    ... 7,13,x,x,59,x,31,19''')
    295
    """
    lines = input.split('\n')

    a = int(lines[0])
    b = lines[1].split(",")

    bus_wait = {}
    for i in b:
        if i != 'x':
            id = int(i)
            min_t = 100000
            for j in range(id):
                if (a + j) % id == 0:
                    min_t = min(min_t, j)
            bus_wait[id] = min_t

    bus = min(bus_wait, key=bus_wait.get)
    return bus * bus_wait[bus]


if __name__ == '__main__':
    little_helper.help(2020, __file__, answer)

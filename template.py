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
    >>> answer('''123
    ... 456''')
    123
    456
    """
    lines = input.split('\n')

    for line in lines:
        print(line)

    return None


if __name__ == '__main__':
    little_helper.help(2020, __file__, answer)

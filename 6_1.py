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
    >>> answer('''abc
    ... 
    ... a
    ... b
    ... c
    ... 
    ... ab
    ... ac
    ... 
    ... a
    ... a
    ... a
    ... a
    ... 
    ... b''')
    11
    """
    lines = input.split('\n\n')

    total_yes_answers = 0
    for group in lines:
        yes_answers = set()
        for person in group.split('\n'):
            for answer in person:
                yes_answers.add(answer)
        total_yes_answers += len(yes_answers)
    return total_yes_answers


if __name__ == '__main__':
    little_helper.help(2020, __file__, answer)

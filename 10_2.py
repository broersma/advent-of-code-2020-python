import little_helper

from cachetools import cached, keys


answer_cache = {}
@cached(answer_cache, key=lambda xs, current: keys.hashkey(current))
def get_options(xs, current):
    count = 0
    for diff in (1,2,3):
        next = current + diff
        if next in xs:
            count += get_options(xs, next)
    result = max(count, 1)
    return result

def answer(input):
    """
    >>> answer_cache.clear()
    >>> answer('''3''')
    1
    >>> answer_cache.clear()
    >>> answer('''16
    ... 10
    ... 15
    ... 5
    ... 1
    ... 11
    ... 7
    ... 19
    ... 6
    ... 12
    ... 4''')
    8
    """
    xs = set(int(line) for line in input.split('\n'))

    return get_options(xs, 0)


if __name__ == '__main__':
    little_helper.help(2020, __file__, answer)

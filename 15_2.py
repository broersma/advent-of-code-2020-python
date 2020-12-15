import little_helper
from collections import defaultdict


def the_answer(numbers, final_turn):
    """
    >>> the_answer([0,3,6], 2020)
    436
    >>> the_answer([0,0,0], 2020)
    104
    """
    """
    >>> the_answer([0,3,6], 30000000)
    175594
    >>> the_answer([1,3,2], 30000000)
    2578
    >>> the_answer([2,3,1], 30000000)
    6895259
    """
    last_turn = defaultdict(list)
    last_number = 0
    turn = 0
    for number in numbers:
        turn += 1
        last_turn[number].append(turn)
        last_number = number
    
    while True:
        if len(last_turn[last_number]) < 2:
            number = 0
        else:
            turns = last_turn[last_number]
            number = turns[-1] - turns[-2]
        turn += 1
        last_turn[number].append(turn)
        last_number = number
        if turn == final_turn:
            break
    return last_number


def answer(input):
    numbers = [int(x) for x in input.split(',')]

    return the_answer(numbers, 30000000)


if __name__ == '__main__':
    little_helper.help(2020, __file__, answer)

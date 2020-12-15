import little_helper
from collections import defaultdict


def answer(input):
    """
    >>> answer('''0,3,6''')
    436
    """
    lines = input.split(',')

    last_turn = defaultdict(list)
    last_number = 0
    turn = 0
    for line in lines:
        number = int(line)
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
        if turn == 2020:
            break


    return last_number


if __name__ == '__main__':
    little_helper.help(2020, __file__, answer)

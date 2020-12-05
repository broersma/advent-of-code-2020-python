import little_helper


def answer(input):
    """
    >>> answer('''FBFBBFFRLR''')
    357
    """
    lines = input.split('\n')
    high_id = 0
    min_row = 0
    max_row = 127
    min_col = 0
    max_col = 7
    for line in lines:
        row = line[:-3]
        col = line[-3:]

        row_id = int(row.replace('F', '0').replace('B', '1'),2)
        col_id = int(col.replace('R', '1').replace('L', '0'),2)

        seat_id = row_id * 8 + col_id

        high_id = max(high_id, seat_id)
    return high_id


if __name__ == '__main__':
    little_helper.help(2020, __file__, answer)

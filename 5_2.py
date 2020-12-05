import little_helper


def answer(input):
    lines = input.split('\n')
    high_id = 0
    min_row = 0
    max_row = 127
    min_col = 0
    max_col = 7
    seats = set()
    for line in lines:
        row = line[:-3]
        col = line[-3:]

        row_id = int(row.replace('F', '0').replace('B', '1'),2)
        col_id = int(col.replace('R', '1').replace('L', '0'),2)

        seat_id = row_id * 8 + col_id

        seats.add(seat_id)

    seats_ordered = sorted(seats)
    for i, seat in enumerate(seats_ordered):
        if seat+1 != seats_ordered[i+1]:
            return seat+1


if __name__ == '__main__':
    little_helper.help(2020, __file__, answer)

import little_helper


def mask_it(mask, bin_value):
    for a,b in zip(mask, bin_value):
        if a == 'X':
            yield b
        else:
            yield a


def answer(input):
    """
    >>> answer('''mask = XXXXXXXXXXXXXXXXXXXXXXXXXXXXX1XXXX0X
    ... mem[8] = 11
    ... mem[7] = 101
    ... mem[8] = 0''')
    165
    """
    lines = input.split('\n')

    memory = {}

    for line in lines:
        if line.startswith('mask = '):
            mask = line[7:]
        else:
            address, value = line.replace('mem[', '').replace('] = ', '|').split('|',1)
            address = int(address)
            value = int(value)

            binary_value = bin(value).replace('0b','').rjust(36,'0')
            new_bin_value = ''.join(mask_it(mask, binary_value))

            new_value = int(new_bin_value, 2)

            memory[address] = new_value
    return sum(memory.values())


if __name__ == '__main__':
    little_helper.help(2020, __file__, answer)

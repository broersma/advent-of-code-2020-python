import little_helper


def paths(list):
    """
    >>> list(paths([[0],[1]]))
    [[0, 1]]
    >>> list(paths([[1, 2]]))
    [[1], [2]]
    >>> list(paths([[0],[1,2]]))
    [[0, 1], [0, 2]]
    """
    if len(list) > 0:
        lists = []
        for option in list[0]:
            for path in paths(list[1:]):
                lists.append([option] + path)
        return lists
    else:
        return [[]]

def mask_it(mask, bin_value):
    for a,b in zip(mask, bin_value):
        if a == '1':
            yield ['1']
        elif a == 'X':
            yield ['0', '1']
        else:
            yield [b]


def answer(input):
    """
    >>> answer('''mask = 000000000000000000000000000000X1001X
    ... mem[42] = 100
    ... mask = 00000000000000000000000000000000X0XX
    ... mem[26] = 1''')
    208
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

            binary_address = bin(address).replace('0b','').rjust(36,'0')
            new_bin_address_masked = mask_it(mask, binary_address)
            for path in paths(list(new_bin_address_masked)):
                new_bin_address = ''.join(path)
                new_address = int(new_bin_address, 2)
                memory[new_address] = value
    return sum(memory.values())


if __name__ == '__main__':
    little_helper.help(2020, __file__, answer)

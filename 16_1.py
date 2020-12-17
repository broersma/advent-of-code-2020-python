import little_helper
from collections import defaultdict

def range_matches(value, range):
    return range[0] <= value <= range[1]


def rule_matches(value, rule):
    return any(range_matches(value, range) for range in rule)

def answer(input):
    """
    >>> answer('''class: 1-3 or 5-7
    ... row: 6-11 or 33-44
    ... seat: 13-40 or 45-50
    ...
    ... your ticket:
    ... 7,1,14
    ...
    ... nearby tickets:
    ... 7,3,47
    ... 40,4,50
    ... 55,2,20
    ... 38,6,12''')
    71
    """
    sections = input.split('\n\n')

    rules = defaultdict(list)
    lines = sections[0].split('\n')
    for line in lines:
        name, ranges = line.split(': ', 1)
        ranges = ranges.split(' or ')
        for range in ranges:
            low, high = list(map(int, range.split('-', 1)))
            rules[name].append((low, high))

    other_tickets = []
    lines = sections[2].split('\n')[1:]
    for line in lines:
        other_ticket = list(map(int, line.split(',')))
        other_tickets.append(other_ticket)

    invalid_values = []
    for ticket in other_tickets:
        for value in ticket:
            if not any(rule_matches(value, rule) for rule in (rules[rule_name] for rule_name in rules)):
                invalid_values.append(value)
    return sum(invalid_values)


if __name__ == '__main__':
    little_helper.help(2020, __file__, answer)

import little_helper
from collections import defaultdict
from functools import reduce

def range_matches(value, range):
    return range[0] <= value <= range[1]


def rule_matches(value, rule):
    return any(range_matches(value, range) for range in rule)

def answer(input):
    """
    >>> answer('''class: 0-1 or 4-19
    ... row: 0-5 or 8-19
    ... departure2: 140-150 or 160-170
    ... seat: 0-13 or 16-19
    ... departure: 100-110 or 120-130
    ...
    ... your ticket:
    ... 3,11,5,12,13
    ...
    ... nearby tickets:
    ... 100,3,140,9,18
    ... 110,15,150,1,5
    ... 120,5,170,14,9''')
    15
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
    my_ticket = list(map(int, sections[1].split('\n', 1)[1].split(',')))

    other_tickets = []
    lines = sections[2].split('\n')[1:]
    for line in lines:
        other_ticket = list(map(int, line.split(',')))
        other_tickets.append(other_ticket)

    valid_tickets = []
    for ticket in other_tickets:
        for value in ticket:
            if not any(rule_matches(value, rule) for rule in (rules[rule_name] for rule_name in rules)):
                break
        else:
            valid_tickets.append(ticket)

    matching_rules = defaultdict(lambda: set(rules.keys()))
    for ticket in valid_tickets:
        for field_id, value in enumerate(ticket):
            matching_rules[field_id] &= set(rule_name for rule_name in rules if rule_matches(value, rules[rule_name]))

    matched_rules = {}
    for field_id in sorted(matching_rules, key=lambda k: len(matching_rules[k])):
        matching_rule = next(iter(matching_rules[field_id] - set(matched_rules)))
        matched_rules[matching_rule] = field_id

    return reduce(lambda a,b: a*b, (my_ticket[i] for i in (matched_rules[rule_name] for rule_name in matched_rules if rule_name.startswith('departure'))), 1)


if __name__ == '__main__':
    little_helper.help(2020, __file__, answer)

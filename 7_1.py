import little_helper
import re

def can_contain(rules, bag, target):
    return any(type == target or can_contain(rules, type, target) for (num, type) in rules[bag])


def answer(input):
    """
    >>> answer('''light red bags contain 1 bright white bag, 2 muted yellow bags.
    ... dark orange bags contain 3 bright white bags, 4 muted yellow bags.
    ... bright white bags contain 1 shiny gold bag.
    ... muted yellow bags contain 2 shiny gold bags, 9 faded blue bags.
    ... shiny gold bags contain 1 dark olive bag, 2 vibrant plum bags.
    ... dark olive bags contain 3 faded blue bags, 4 dotted black bags.
    ... vibrant plum bags contain 5 faded blue bags, 6 dotted black bags.
    ... faded blue bags contain no other bags.
    ... dotted black bags contain no other bags.''')
    4
    """
    lines = input.split('\n')

    rules = {}
    for line in lines:
        rule = line.replace(" contain ", "|").split("|", 1)
        bag = rule[0][:-5]
        contents = [(int(n), t) for (n, t) in re.findall(r'(\d+) (.*?) bags?', rule[1])]
        rules[bag] = contents
    return len([bag for bag in rules if can_contain(rules, bag, 'shiny gold')])


if __name__ == '__main__':
    little_helper.help(2020, __file__, answer)

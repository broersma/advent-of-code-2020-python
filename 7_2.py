import little_helper
import re

def num_contains(rules, bag):
    return 1 + sum(num * num_contains(rules, type) for (num, type) in rules[bag])


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
    32
    >>> answer('''shiny gold bags contain 2 dark red bags.
    ... dark red bags contain 2 dark orange bags.
    ... dark orange bags contain 2 dark yellow bags.
    ... dark yellow bags contain 2 dark green bags.
    ... dark green bags contain 2 dark blue bags.
    ... dark blue bags contain 2 dark violet bags.
    ... dark violet bags contain no other bags.''')
    126
    """
    lines = input.split('\n')

    rules = {}
    for line in lines:
        rule = line.replace(" contain ", "|").split("|", 1)
        bag = rule[0][:-5]
        contents = [(int(n), t) for (n, t) in re.findall(r'(\d+) (.*?) bags?', rule[1])]
        rules[bag] = contents
    return num_contains(rules, 'shiny gold') - 1


if __name__ == '__main__':
    little_helper.help(2020, __file__, answer)

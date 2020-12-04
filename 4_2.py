import little_helper

import re


def answer(input):
    """
    >>> answer('''eyr:1972 cid:100
    ... hcl:#18171d ecl:amb hgt:170 pid:186cm iyr:2018 byr:1926
    ...
    ... iyr:2019
    ... hcl:#602927 eyr:1967 hgt:170cm
    ... ecl:grn pid:012533040 byr:1946
    ...
    ... hcl:dab227 iyr:2012
    ... ecl:brn hgt:182cm pid:021572410 eyr:2020 byr:1992 cid:277
    ...
    ... hgt:59cm ecl:zzz
    ... eyr:2038 hcl:74454a iyr:2023
    ... pid:3556412378 byr:2007''')
    0
    >>> answer('''pid:087499704 hgt:74in ecl:grn iyr:2012 eyr:2030 byr:1980
    ... hcl:#623a2f
    ...
    ... eyr:2029 ecl:blu cid:129 byr:1989
    ... iyr:2014 pid:896056539 hcl:#a97842 hgt:165cm
    ...
    ... hcl:#888785
    ... hgt:164cm byr:2001 iyr:2015 cid:88
    ... pid:545766238 ecl:hzl
    ... eyr:2022
    ...
    ... iyr:2010 hgt:158cm hcl:#b6652a ecl:blu byr:1944 eyr:2021 pid:093154719''')
    4
    >>> answer('''pid:087499704 hgt:74in ecl:grn iyr:2012 eyr:2030 byr:2003
    ... hcl:#623a2f
    ...
    ... eyr:2029 ecl:blu cid:129 byr:1989
    ... iyr:2014 pid:896056539 hcl:#a97842 hgt:190
    ...
    ... hcl:#888785
    ... hgt:190in byr:2001 iyr:2015 cid:88
    ... pid:545766238 ecl:hzl
    ... eyr:2022
    ...
    ... iyr:2010 hgt:158cm hcl:#b6652z ecl:blu byr:1944 eyr:2021 pid:093154719
    ...
    ... eyr:2029 ecl:blu cid:129 byr:1989
    ... iyr:2014 pid:896056539 hcl:a97842 hgt:165cm
    ...
    ... pid:087499704 hgt:74in ecl:wat iyr:2012 eyr:2030 byr:1980
    ... hcl:#623a2f
    ...
    ... iyr:2010 hgt:158cm hcl:#b6652a ecl:blu byr:1944 eyr:2021 pid:0123456789''')
    0
    """
    passports = input.split('\n\n')

    valid = 0
    required_fields = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']
    for passport in passports:
        passport = passport.replace("\n", " ")
        fields = passport.split(" ")
        passport = dict(tuple(field.split(":")) for field in fields)
        if all(field in passport for field in required_fields):
            if 1920 <= int(passport['byr']) <= 2002 \
            and 2010 <= int(passport['iyr']) <= 2020 \
            and 2020 <= int(passport['eyr']) <= 2030 \
            and (passport['hgt'].endswith('cm') and 150 <= int(passport['hgt'][:-2]) <= 193 \
                 or passport['hgt'].endswith('in') and 59 <= int(passport['hgt'][:-2]) <= 76) \
            and re.match('^#[0-9a-f]{6}$', passport['hcl']) \
            and passport['ecl'] in 'amb blu brn gry grn hzl oth'.split() \
            and re.match('^\d{9}$', passport['pid']):
                valid += 1
    return valid


if __name__ == '__main__':
    little_helper.help(2020, __file__, answer)

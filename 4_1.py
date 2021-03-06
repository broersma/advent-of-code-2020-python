import little_helper


def answer(input):
    """
    >>> answer('''ecl:gry pid:860033327 eyr:2020 hcl:#fffffd
    ... byr:1937 iyr:2017 cid:147 hgt:183cm
    ...
    ... iyr:2013 ecl:amb cid:350 eyr:2023 pid:028048884
    ... hcl:#cfa07d byr:1929
    ...
    ... hcl:#ae17e1 iyr:2013
    ... eyr:2024
    ... ecl:brn pid:760753108 byr:1931
    ... hgt:179cm
    ...
    ... hcl:#cfa07d eyr:2025 pid:166559648
    ... iyr:2011 ecl:brn hgt:59in''')
    2
    """
    passports = input.split('\n\n')

    valid = 0
    required_fields = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']
    for passport in passports:
        passport = passport.replace("\n", " ")
        fields = passport.split(" ")
        passport = dict(tuple(field.split(":")) for field in fields)
        if all(field in passport for field in required_fields):
            valid += 1

    return valid


if __name__ == '__main__':
    little_helper.help(2020, __file__, answer)

'''
    byr (Birth Year)
    iyr (Issue Year)
    eyr (Expiration Year)
    hgt (Height)
    hcl (Hair Color)
    ecl (Eye Color)
    pid (Passport ID)
    cid (Country ID)
'''

def validate_passport(l):
    fields = {
        "byr",
        "iyr",
        "eyr",
        "hgt",
        "hcl",
        "ecl",
        "pid",
        "cid"
    }

    passport = dict()

    for pair in l.split(" "):
        kv = pair.split(":")
        if len(kv) == 2:
            passport[kv[0]] = kv[1]
        else:
            return False

    print("   $ " + repr(passport.items()))
    for (k,v) in passport.items():
        if k not in fields:
            print("Invalid passport: {} not among valid fields!".format(k))
            return False
        '''
        if not v:
            print("Invalid passport: value {} empty!".format(v))
            return False
        '''
        print("  Removing '{}'...".format(k))
        fields.remove(k)

    if "cid" in fields:
        fields.remove("cid")
    if not fields:
        print("Valid passport. Remaining fields {}.".format(repr(fields)))
        return True
    print("Invalid passport: remaining fields {}!".format(repr(fields)))
    return False

valid = 0
passports = []
passport = []
with open("input") as f:
    for l in f:
        if l == "\n" or not l:
            passports.append(" ".join(passport))
            passport = []
        else:
            passport.append(l)
    passports.append(" ".join(passport))

for l in passports:
    print(l)
    if validate_passport(l) == True:
        valid += 1

print(str(valid))

import re

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

    for (k,v) in passport.items():
        if k not in fields:
            return False

        if k == "byr":
            try:
                if len(str(v)) == 4 and int(v) >= 1920 and int(v) <= 2002:
                    fields.remove(k)
                else:
                    return False
            except Exception as e:
                return False

        if k == "iyr":
            try:
                if len(str(v)) == 4 and int(v) >= 2010 and int(v) <= 2020:
                    fields.remove(k)
                else:
                    return False
            except Exception as e:
                return False
            
        if k == "eyr":
            try:
                if len(str(v)) == 4 and int(v) >= 2020 and int(v) <= 2030:
                    fields.remove(k)
                else:
                    return False
            except Exception as e:
                return False
            
        if k == "hgt":
            try:
                num = int(v[0:-2])
                suffix = v[-2:]
                if suffix == "cm":
                    if num >= 150 and num <= 193:
                        fields.remove(k)
                    else:
                        return False
                if suffix == "in":
                    if num >= 59 and num <= 76:
                        fields.remove(k)
                    else:
                        return False
            except Exception as e:
                return False

        if k == "hcl":
            try:
                if re.fullmatch(r'#[a-f0-9]{6}', v):
                    fields.remove(k)
                else:
                    return False
            except Exception as e:
                return False

        if k == "ecl":
            try:
                if re.fullmatch(r"amb|blu|brn|gry|grn|hzl|oth", v):
                    fields.remove(k)
                else:
                    return False
            except Exception as e:
                return False

        if k == "pid":
            try:
                if re.fullmatch(r"[0-9]{9}", v) and re.fullmatch(r"0*[0-9]*", v):
                    fields.remove(k)
                else:
                    return False
            except Exception as e:
                return False

        if k == "cid":
            continue

    if "cid" in fields:
        fields.remove("cid")
    if not fields:
        return True
    return False

valid = 0
passports = []
passport = []
with open("input") as f:
    for l in f:
        if l == "\n" or not l:
            passports.append(" ".join(passport).replace("\n", ""))
            passport = []
        else:
            passport.append(l)
    passports.append(" ".join(passport).replace("\n", ""))

for l in passports:
    if validate_passport(l) == True:
        valid += 1

print(str(valid))

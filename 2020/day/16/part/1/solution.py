import re

class Mode:
    FIELDS = 1
    YOURS  = 2
    THEIRS = 3

def parseValidField(l, d):
    m = re.match(
        r"([a-zA-Z]*): ([0-9]*-[0-9]*) or ([0-9]*-[0-9]*)",
        l)
    if m:
        field  = m.group(1)
        range1 = m.group(2)
        range2 = m.group(3)

        m1 = re.match(r"([0-9]*)-([0-9]*)", range1)
        first1 = m1.group(1)
        last1 = m1.group(2)

        m2 = re.match(r"([0-9]*)-([0-9]*)", range2)
        first2 = m2.group(1)
        last2 = m2.group(2)

        d[field] = (first1, last1, first2, last2)

def validateCsvs(l, d, c):
    t = l[:-1].split(",")
    for k in t:
        valid = False
        k = int(k)
        for (s1, e1, s2, e2) in d.values():
            s1, e1, s2, e2 = int(s1), int(e1), int(s2), int(e2)
            if k in range(s1, e1 + 1) or k in range(s2, e2 + 1):
                valid = True
                break
        if not valid:
            c[0] += k

d = dict()
mode = Mode.FIELDS
c = [0]
with open('input') as file:
    for l in file:
        if l == "\n":
            if mode == Mode.FIELDS:
                mode = Mode.YOURS
            elif mode == Mode.YOURS:
                mode = Mode.THEIRS
            continue

        if mode == Mode.FIELDS:
            parseValidField(l, d)

        if mode == Mode.YOURS:
            if l == "your ticket:\n":
                continue
            validateCsvs(l, d, c)

        if mode == Mode.THEIRS:
            if l == "nearby tickets:\n":
                continue
            validateCsvs(l, d, c)

print(c[0])

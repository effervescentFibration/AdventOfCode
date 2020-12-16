import copy
import re

class Mode:
    FIELDS = 1
    YOURS  = 2
    THEIRS = 3

def parseValidField(l, d):
    m = re.match(
        r"([a-zA-Z ]*): ([0-9]*-[0-9]*) or ([0-9]*-[0-9]*)",
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
    validTicket = True
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
            validTicket = False
    return validTicket

def determineValidFields(l, d, h):
    l = l.split(",")
    i = 0
    for k in l:
        k = int(k)
        s = copy.deepcopy(h[i])
        for j in s:
            (s1, e1, s2, e2) =  d[j]
            s1, e1, s2, e2 = int(s1), int(e1), int(s2), int(e2)
            if k not in range(s1, e1 + 1) and k not in range(s2, e2 + 1):
                h[i].remove(j)
                break
        i += 1

def removeRedundanciesStep(h):
    for k,v in h.items():
        if len(v) == 1:
            for v in v:
                for k2 in h.keys():
                    if k2 != k and v in h[k2]:
                        h[k2].remove(v)

def removeRedundancies(h):
    # compute the least fixed point of removeRedundanciesStep
    # to remove all redundancies
    h2 = copy.deepcopy(h)
    removeRedundanciesStep(h2)
    while h != h2:
        h = h2
        h2 = copy.deepcopy(h)
        removeRedundanciesStep(h2)
    return h

d = dict()
mode = Mode.FIELDS
c = [0]
myTicket = None
validTickets = []
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
            myTicket = l[:-1]

        if mode == Mode.THEIRS:
            if l == "nearby tickets:\n":
                continue
            if validateCsvs(l, d, c):
                validTickets.append(l[:-1])

h = dict()
for t in range(len(validTickets[0].split(","))):
    t = int(t)
    h[t] = set(v for v in d.keys())
for l in validTickets:
    determineValidFields(l, d, h)

h = removeRedundancies(h)

p = 1
myTicket = myTicket.split(",")
for i,field in h.items():
    for field in field:
        if field.split()[0] == "departure":
            p *= int(myTicket[i])

print(p)

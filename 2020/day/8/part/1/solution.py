import copy
import re

def accumulate(sign, mag, acc):
    mag = int(mag)
    if sign == "-":
        mag *= -1
    pair[0] += mag

def jump(sign, mag, acc):
    mag = int(mag)
    if sign == "-":
        mag *= -1
    pair[1] += mag


def match(l, pair):
        match = re.match(r"acc ([\+-])(\d*)\n", l)
        if match:
            sign = match.groups()[0]
            mag = match.groups()[1]
            accumulate(sign, mag, pair)
        match = re.match(r"jmp ([\+-])(\d*)\n", l)
        if match:
            sign = match.groups()[0]
            mag = match.groups()[1]
            jump(sign, mag, pair)
            # skip incrementing ip since we jumped
            return
        pair[1] += 1

with open("input") as f:
    a = []
    for l in f:
        a.append(l)
    # (reg, ip)
pair = [0, 0]
visited = set()
while pair[1] >= 0 and pair[1] < len(a) and pair[1] not in visited:
    visited.add(pair[1])
    match(a[pair[1]], pair)
print(str(pair[0]))

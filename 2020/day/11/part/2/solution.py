import copy
from collections import defaultdict

def toStr(dd, imax, jmax):
    s = []
    for i in range(imax):
        for j in range(jmax):
            s.append(dd[(i, j)])
        s.append("\n")
    return "".join(s)

def evolve_cell(dd, i, j):
    t = [
        (-1, -1), # top-left
        (-1, 0), # top-center
        (-1, +1), # top-right
        (0, -1), # middle-left
        (0, +1), # middle-right
        (1, -1), # top-left
        (1, 0), # top-center
        (1, +1) # top-right
    ]
    count = 0
    
    for k in t:
        i_, j_ = i, j
        while True:
            (id, jd) = k
            i_ += id
            j_ += jd
            if (i_, j_) not in dd.keys():
                break
            if dd[(i_, j_)] == "L":
                break
            if dd[(i_, j_)] == "#":
                count += 1
                break

    if dd[(i, j)] == "L" and count == 0:
        return "#"
    if dd[(i, j)] == "#" and count >= 5:
        return "L"
    return dd[(i, j)]

dd = defaultdict()
dd.setdefault(".")

def evolve(dd, i_max, j_max):
    new_dd = copy.deepcopy(dd)
    for i in range(i_max):
        for j in range(j_max):
            new_dd[(i, j)] = evolve_cell(dd, i, j)
    return new_dd

i = 0
j = 0
with open("input") as file:
    i = 0
    for l in file:
        j = 0
        for c in l:
            if c == "\n":
                continue
            dd[(i, j)] = c
            j += 1
        i += 1

j_max = j
i_max = i

new_dd = evolve(dd, i_max, j_max)
while new_dd != dd:
    dd = new_dd
    new_dd = evolve(dd, i_max, j_max)

occupied = 0
for i in range(i_max):
    for j in range(j_max):
        if dd[(i, j)] == "#":
            occupied += 1

print(repr(occupied))

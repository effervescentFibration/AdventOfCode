import copy
from collections import defaultdict

def expand(x):
    i_max, j_max, k_max, w_max = x
    return (
        (j_max[0] - 1, j_max[1] + 1),
        (i_max[0] - 1, i_max[1] + 1),
        (k_max[0] - 1, k_max[1] + 1),
        (w_max[0] - 1, w_max[1] + 1)
    )

def find_dimensions(dd):
    i_sup = float("-inf")
    j_sup = float("-inf")
    k_sup = float("-inf")
    w_sup = float("-inf")

    i_inf = float("+inf")
    j_inf = float("+inf")
    k_inf = float("+inf")
    w_inf = float("+inf")

    for v in dd.keys():
        (i_, j_, k_, w_) = v

        if i_ > i_sup:
            i_sup = i_
        if i_ < i_inf:
            i_inf = i_

        if j_ > j_sup:
            j_sup = j_
        if j_ < j_inf:
            j_inf = j_

        if k_ > k_sup:
            k_sup = k_
        if k_ < k_inf:
            k_inf = k_

        if w_ > w_sup:
            w_sup = w_
        if w_ < w_inf:
            w_inf = w_

    return (
        (i_inf, i_sup),
        (j_inf, j_sup),
        (k_inf, k_sup),
        (w_inf, w_sup)
    )

def prnt_map(dd):
    (i_max, j_max, k_max, w_max) = find_dimensions(dd)
    s = []
    for w in range(w_max[0], w_max[1] + 1):
        for k in range(k_max[0], k_max[1] + 1):
            s.append("z = {}, w = {}".format(k, w))
            for i in range(i_max[0], i_max[1] + 1):
                s1 = []
                for j in range(j_max[0], j_max[1] + 1):
                    if (i, j, k, w) in dd.keys():
                        s1.append(dd[(i, j, k, w)])
                    else:
                        s1.append(".")
                s.append("".join(s1))
            s.append("")
    return "\n".join(s)

def evolve_cell(dd, i, j, k, w):
    t = set()
    for i_ in range(i - 1, i + 2):
        for j_ in range(j - 1, j + 2):
            for k_ in range(k - 1, k + 2):
                for w_ in range(w - 1, w + 2):
                    t.add((i_, j_, k_, w_))
    t.remove((i, j, k, w))
    assert(len(t) == 80)

    count = 0
    for u in t:
        if u not in dd.keys():
            continue
        if dd[u] == "#":
            count += 1
    if (i, j, k, w) not in dd.keys() or dd[(i, j, k, w)] == ".":
        if count == 3:
            return "#"
        else:
            return "."
    elif dd[(i, j, k, w)] == "#":
        if count == 2 or count == 3:
            return "#"
        else:
            return "."

def evolve(dd):
    (i_max, j_max, k_max, w_max) = expand(find_dimensions(dd))
    new_dd = dict()
    for i in range(i_max[0], i_max[1] + 1):
        for j in range(j_max[0], j_max[1] + 1):
            for k in range(k_max[0], k_max[1] + 1):
                for w in range(w_max[0], w_max[1] + 1):
                    new_dd[(i, j, k, w)] = evolve_cell(dd, i, j, k, w)
    return new_dd

dd = dict()

i = 0
j = 0
jm = 0
with open("input") as file:
    i = 0
    k = 0
    w = 0
    for l in file:
        j = 0
        for c in l:
            if c == "\n":
                continue
            dd[(i, j, k, w)] = c
            j += 1
            if j > jm:
                jm = j
        i += 1

cycles = 6

(i_max, j_max, k_max, w_max) = find_dimensions(dd)
print("{}, {}, {}, {}".format(i_max, j_max, k_max, w_max))
print("Before any cycles:")
print(prnt_map(dd))
for a in range(0, cycles):
    new_dd = evolve(dd)
    print("Round " + repr(a + 1) + ":")
    (i_max, j_max, k_max, w_max) = find_dimensions(dd)
    print("{}, {}, {}, {}".format(i_max, j_max, k_max, w_max))
    print(prnt_map(new_dd))
    dd = new_dd
    occupied = 0
    for v in new_dd.values():
        if v == "#":
            occupied += 1

    print(str(a + 1) + ": " + repr(occupied))

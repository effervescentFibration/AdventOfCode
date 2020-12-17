import copy
from collections import defaultdict

def expand(i_max, j_max, k_max):
    return (
        (j_max[0] - 1, j_max[1] + 1),
        (i_max[0] - 1, i_max[1] + 1),
        (k_max[0] - 1, k_max[1] + 1)
    )

def prnt_map(dd, i_max, j_max, k_max):
    s = []
    for k in range(k_max[0], k_max[1] + 1):
        s.append("z = " + repr(k))
        for i in range(i_max[0], i_max[1] + 1):
            s1 = []
            for j in range(j_max[0], j_max[1] + 1):
                if (i, j, k) in dd.keys():
                    s1.append(dd[(i, j, k)])
                else:
                    s1.append(".")
            s.append("".join(s1))
        #s.append("\n")
    return "\n".join(s)

def evolve_cell(dd, i, j, k):
    t = [
        (i - 1, j - 1, k - 1), # top-left
        (i - 1, j, k - 1), # top-center
        (i - 1, j + 1, k - 1), # top-right
        (i, j - 1, k - 1), # middle-left
        (i, j, k - 1), # middle-middle
        (i, j + 1, k - 1), # middle-right
        (i + 1, j - 1, k - 1), # top-left
        (i + 1, j, k - 1), # top-center
        (i + 1, j + 1, k - 1), # top-right
        
        (i - 1, j - 1, k), # top-left
        (i - 1, j, k), # top-center
        (i - 1, j + 1, k), # top-right
        (i, j - 1, k), # middle-left
        # (i, j, k), # middle-middle
        (i, j + 1, k), # middle-right
        (i + 1, j - 1, k), # top-left
        (i + 1, j, k), # top-center
        (i + 1, j + 1, k), # top-right

        (i - 1, j - 1, k + 1), # top-left
        (i - 1, j, k + 1), # top-center
        (i - 1, j + 1, k + 1), # top-right
        (i, j - 1, k + 1), # middle-left
        (i, j, k + 1), # middle-middle
        (i, j + 1, k + 1), # middle-right
        (i + 1, j - 1, k + 1), # top-left
        (i + 1, j, k + 1), # top-center
        (i + 1, j + 1, k + 1) # top-right
    ]
    count = 0
    for u in t:
        if u not in dd.keys():
            continue
        if dd[u] == "#":
            count += 1
    if (i, j, k) not in dd.keys() or dd[(i, j, k)] == ".":
        if count == 3:
            return "#"
        else:
            return "."
    elif dd[(i, j, k)] == "#":
        if count == 2 or count == 3:
            return "#"
        else:
            return "."

    # return dd[(i, j, k)]


# Function to return a default 
# values for keys that is not 
# present 
def inactive_cube(): 
    return "."

dd = defaultdict()
dd.setdefault(inactive_cube)

def evolve(dd, i_max, j_max, k_max):
    new_dd = copy.deepcopy(dd)
    for i in range(i_max[0], i_max[1] + 1):
        for j in range(j_max[0], j_max[1] + 1):
            for k in range(k_max[0], k_max[1] + 1):
                new_dd[(i, j, k)] = evolve_cell(dd, i, j, k)
    return new_dd

i = 0
j = 0
jm = 0
with open("input") as file:
    i = 0
    k = 0
    for l in file:
        j = 0
        for c in l:
            if c == "\n":
                continue
            dd[(i, j, k)] = c
            j += 1
            if j > jm:
                jm = j
        i += 1

cycles = 6

j_max = (0, jm)
i_max = (0, i - 1)
k_max = (0, 0)

j_max = (j_max[0] - 1, j_max[1] + 1)
i_max = (i_max[0] - 1, i_max[1] + 1)
k_max = (k_max[0] - 1, k_max[1] + 1)
#print("{}, {}, {}".format(i_max, j_max, k_max))
#print(repr(dd))
print("Round " + "1" + ":")
print(prnt_map(dd, i_max, j_max, k_max))
new_dd = evolve(dd, i_max, j_max, k_max)
# while new_dd != dd:
for a in range(1, cycles):
    print("Round " + repr(a + 1) + ":")
    # print(repr(dd))
    print("{}, {}, {}".format(i_max, j_max, k_max))
    print(prnt_map(dd, i_max, j_max, k_max))
    print("End Round " + repr(a + 1) + ".")
    # print(repr(dd))
    dd = new_dd
    j_max = (j_max[0] - 1, j_max[1] + 1)
    i_max = (i_max[0] - 1, i_max[1] + 1)
    k_max = (k_max[0] - 1, k_max[1] + 1)
    new_dd = evolve(dd, i_max, j_max, k_max)

    occupied = 0
    for v in new_dd.values():
        if v == "#":
            occupied += 1

    print(str(a + 1) + ": " + repr(occupied))

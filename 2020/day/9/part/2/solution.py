import copy
import re
from collections import deque

def contigSum(i, l):
    for first_i in range(len(l)):
        s = l[first_i]
        last_i = first_i + 1
        while last_i < len(l):
            s += l[last_i]
            if s == i:
                return [first_i, last_i]
            if s > i:
                break
            last_i += 1

import copy
import re
from collections import deque

def check(i, d):
    for k in range(len(d)):
        for l in range(k + 1, len(d)):
            if d[k] + d[l] == i:
                return True
    return False

d = deque()
a = []
badValue = None

with open("input") as f:
    for l in f:
        i = int(str(l[0:-1])) # Exclude the last char, which is a linebreak

        if len(d) == 25:
            if not check(i, d):
                badValue = i
                break # we have found the solution to part 1
            d.popleft()
        d.append(i)
        a.append(i)

# find the contiguous slice for part 1
g = contigSum(badValue, a)
# produce the slice indicated by the contiguous sum
contigSlice = a[g[0]:(g[1]+1)]

sliceMin = min(contigSlice)
sliceMax = max(contigSlice)

print(sum([sliceMin, sliceMax]))

import copy
import re
from collections import deque

a = list()
with open("input") as f:
    for l in f:
        i = int(str(l[0:-1])) # Exclude the last char, which is a linebreak
        a.append(i)
a.sort()

diffs1 = 1
diffs3 = 1

for i in range(len(a)):
    if i > 0:
        diff = a[i] - a[i - 1]
        if diff == 1:
            diffs1 += 1
        if diff == 3:
            diffs3 += 1

print(diffs1)
print(diffs3)
print(diffs1 * diffs3)

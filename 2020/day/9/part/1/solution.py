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

print(badValue)

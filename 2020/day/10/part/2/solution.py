import copy
import re
from collections import deque

# include the socket itself, in order to model
# cases that may not include the first outlet
a = list([0]) 
with open("input") as f:
    for l in f:
        i = int(str(l[0:(len(l) - 1)])) # Exclude the last char, which is a linebreak
        a.append(i)
a.sort()
print(repr(a))

# represent the number of ways of standing up the joltage
ways = [0 for i in range(len(a))]
ways[0] = 1 # base case
# inductive case
for i in range(1, len(a)):
    j = i - 1
    while j >= 0 and (a[i] - a[j] <= 3):
        ways[i] += ways[j]
        j -= 1

print(ways[-1])

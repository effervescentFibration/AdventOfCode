import copy
import re
from collections import deque

def contigSum(i, l):
    for first_i in range(len(l)):
        s = l[first_i]
        last_i = first_i + 1
        while last_i < len(l):# and l[last_i] == l[last_i - 1] + 1:
            #print(str(first_i) + "," + str(last_i))
            s += l[last_i]
            if s == i:
                return [first_i, last_i]
            if s > i:
                break
            last_i += 1

def gauss(t):
    return t * (t + 1) / 2

def check(i, d, s):
    for k in range(len(d)):
        for l in range(k + 1, len(d)):
            #print("k {} l {}".format(k, l))
            if d[k] + d[l] == i:
                #print(d[k] + " + " + d[l] + " = " + i)
                return True
    return False

d = deque()
s = set()
a = []

with open("input") as f:
    for l in f:
        try:
            i = int(str(l[0:-1]))
            a.append(i)
        except Exception as e:
            print(e)
            while True:
                continue
            continue

input = 556543474 # part 1

g = contigSum(input, a)
a0 = a[g[0]:(g[1]+1)]
print("??? " + str(sum(a0) - input))

amin = min(a0)
print(amin)
amax = max(a0)
print(amax)

print(sum([amin, amax]))

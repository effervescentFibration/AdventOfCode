import copy
import re
from collections import deque

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

with open("input") as f:
    for l in f:
        try:
            i = int(str(l[0:-1]))
            if i in d:
                raise Exception("Boof")
                
            if len(d) == 25:
                #print(repr(d))
                if not check(i, d, s):
                    print("# " + str(i))
                    raise Exception("Blah")
                s.remove(d.popleft())
            d.append(i)
            s.add(i)
        except Exception as e:
            print(e)
            while True:
                continue
            continue

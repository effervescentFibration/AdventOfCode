from collections import deque

def update_d(d, n, i):
    if n not in d.keys():
        d[n] = deque()
    d[n].append(i)
    while len(d[n]) > 2:
        d[n].popleft()

def gen_spoken_nums_up_to_k(t, k):
    d = dict() # num to its last two appearances
    for i in range(len(t) - 1):
        update_d(d, t[i], i)
    last_i = len(t) - 1
    last = t[last_i]
    while last_i < k - 1:
        update_d(d, last, last_i)
        if len(d[last]) < 2:
            last = 0
        else:
            last = (d[last][1] - d[last][0])
        last_i += 1
    return last

t = []
k = 2020
with open('input') as f:
    for l in f:
        t = l[:-1].split(",")
        t = [int(x) for x in t]
        print(gen_spoken_nums_up_to_k(t, k))

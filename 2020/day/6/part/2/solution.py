s = dict()
count = 0
m = 0

with open("input") as f:
    for l in f:
        if l == "\n":
            for k,v in s.items():
                if v == m:
                    count += 1
            s = dict()
            m = 0
            continue
        m += 1
        for c in l:
            if c == "\n":
                continue
            if c not in s.keys():
                s[c] = 0
            s[c] += 1

for k,v in s.items():
    if v == m:
        count += 1
print(count)

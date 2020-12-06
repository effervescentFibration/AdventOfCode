s = set()
count = 0
with open("input") as f:
    for l in f:
        if l == "\n":
            count += len(s)
            s = set()
            continue
        for c in l:
            if c == "\n":
                continue
            s.add(c)

count += len(s)
print(count)

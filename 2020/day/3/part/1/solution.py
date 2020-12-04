def trees(landscape, right, down):
    r = right
    d = down
    tree_count = 0
    while d < len(landscape):
        t = landscape[d][r % len(landscape[d])]
        
        if t == '.':
            t = t
        elif t == '#':
            tree_count += 1
        else:
            print("No good! Saw char {}".format(t))
        print ("{}, {}, {}, {}".format(d, r % (len(landscape[d])), t, tree_count ))
        d += down
        r += right
    return tree_count

landscape = []

with open("input") as f:
    for l in f:
        landscape.append([])
        for c in l:
            if c != "\n" and c != "\r":
                landscape[-1].append(c)

print(trees(landscape, 3, 1))

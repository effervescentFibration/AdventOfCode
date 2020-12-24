def get_tile_coords(l):
    x = 0
    y = 0
    z = 0

    i = 0
    print(l)
    while i < len(l):
        print("x={}, y={}, z={}, sum={}".format(x,y,z,str(sum([x,y,z]))))
        print("i = {}".format(i))
        if l[i] == "e":
            print("E")
            x += 1
            y -= 1
            i += 1
            continue
        elif l[i] == "n" and i < len(l) - 1:
            if l[i:i+2] == 'ne':
                print("NE")
                x += 1
                z -= 1
                i += 2
                continue
            if l[i:i+2] == 'nw':
                print("NW")
                y += 1
                z -= 1
                i += 2
                continue
        elif l[i] == "w":
            print("W")
            x -= 1
            y += 1
            i += 1
            continue
        elif l[i] == "s" and i < len(l) - 1:
            if l[i:i+2] == 'se':
                print("SE")
                z += 1
                y -= 1
                i += 2
                continue
            if l[i:i+2] == 'sw':
                print("SW")
                x -= 1
                z += 1
                i += 2
                continue
    print("x={}, y={}, z={}, sum={}".format(x,y,z,str(sum([x,y,z]))))
    return (x, y, z)

d = dict()

with open('input') as file:
    for l in file:
        coords = get_tile_coords(l[:-1])
        x,y,z = coords
        if coords not in d.keys():
            d[coords] = False
        else:
            d[coords] = not d[coords]

blacks = 0
for v in d.values():
    print(repr(v))
    if not v:
        blacks += 1
print("{}".format(blacks))

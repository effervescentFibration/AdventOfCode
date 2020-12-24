neighbors = {
    (+1, -1, 0),
    (+1, 0, -1),
    (0, +1, -1),
    (-1, +1, 0),
    (-1, 0, +1),
    (0, -1, +1)
}

def evolve(tiles):
    new_tiles = dict()
    empty_neighbors = set()
    for coords, color in tiles.items():
        x, y, z = coords
        active_neighbors = 0
        for neighbor in neighbors:
            dx, dy, dz = neighbor
            x_, y_, z_ = x + dx, y + dy, z + dz
            coord_ = x_, y_, z_
            if coord_ in tiles.keys():
                if tiles[coord_]:
                    active_neighbors += 1
            else:
                empty_neighbors.add(coord_)
        if color and ((not active_neighbors) or (active_neighbors > 2)):
            new_tiles[coords] = False
        elif not color and (active_neighbors == 2):
            new_tiles[coords] = True
        else:
            new_tiles[coords] = color
    for coords in empty_neighbors:
        color = False
        x, y, z = coords
        active_neighbors = 0
        for neighbor in neighbors:
            dx, dy, dz = neighbor
            x_, y_, z_ = x + dx, y + dy, z + dz
            coord_ = x_, y_, z_
            if coord_ in tiles.keys():
                if tiles[coord_]:
                    active_neighbors += 1
        if (active_neighbors == 2):
            new_tiles[coords] = True
    return new_tiles

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
            d[coords] = True
        else:
            d[coords] = not d[coords]

blacks = 0
for color in d.values():
    if color:
        blacks += 1
print("{}".format(blacks))

for i in range(100):
    d = evolve(d)

    blacks = 0
    for color in d.values():
        if color:
            blacks += 1
    print("{}".format(blacks))

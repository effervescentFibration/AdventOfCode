import copy
import math
from collections import defaultdict

def change_position(l, position, orientation):
    if l == "\n":
        return (position, orientation)
    x, y = position
    t = int(l[1:-1])
    if l[0] == "N":
        y += t
    if l[0] == "S":
        y -= t
    if l[0] == "E":
        x += t
    if l[0] == "W":
        x -= t

    if l[0] == "L" or l[0] == "R":
        if l[0] == "L":
            orientation += t
        else:
            orientation -= t
        orientation = orientation % 360

    if l[0] == "F":
        x += (
            round(float(t) * math.cos(float(orientation) * math.pi / 180.))
        )
        y += (
            round(float(t) * math.sin(float(orientation) * math.pi / 180.))
        )
    return ((x, y), orientation)

position = (0, 0)
orientation = 0
print("{}, {}".format(position, orientation))
with open("input") as file:
    for l in file:
        position, orientation = change_position(l, position, orientation)
        print("{}, {}".format(position, orientation))
x, y = position
print(sum([abs(x), abs(y)]))

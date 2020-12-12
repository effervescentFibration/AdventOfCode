import copy
import math
from collections import defaultdict

def change_position(l, position, waypoint):
    if l == "\n":
        return (position, waypoint)
    x, y = waypoint
    x_, y_ = position
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
            orientation = +t
        else:
            orientation = -t
        orientation = orientation % 360

        x, y = (
            round(float(x) * math.cos(float(orientation) * math.pi / 180.)) -
            round(float(y) * math.sin(float(orientation) * math.pi / 180.))
        ), (
            round(float(x) * math.sin(float(orientation) * math.pi / 180.)) +
            round(float(y) * math.cos(float(orientation) * math.pi / 180.))
        )
    if l[0] == "F":
        x_ += x * t
        y_ += y * t
    return ((x_, y_), (x, y))

position = (0, 0)
waypoint = (10, 1)

with open("input") as file:
    for l in file:
        position, waypoint = change_position(l, position, waypoint)

x, y = position
print(sum([abs(x), abs(y)]))

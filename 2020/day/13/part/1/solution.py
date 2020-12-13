import copy
import math
from collections import defaultdict

buses = set()
earliest = -1
with open("input") as file:
    i = 0
    for l in file:
        if not i:
            earliest = int(l[0:-1])
        else:
            bus_list = str(l[0:-1]).split(",")
            for bus in bus_list:
                if bus == "x":
                    continue
                else:
                    buses.add(int(bus))
        i += 1

soonest = float("inf")
soonest_bus = -1

for bus in buses:
    excess_time = (earliest % bus)
    cand = bus - excess_time
    excess_time = (bus - earliest) % bus
    if cand < soonest:
        soonest = cand
        soonest_bus = bus

print(soonest * soonest_bus)

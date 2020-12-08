import copy
import re

def match(l, prog, bag_contents):
    match = prog.search(l)
    d = dict()
    if match:
        groups = match.groups()
        t = 0
        v = None
        bag_name = groups[0]
        for group in re.finditer(r"(([0-9]*) ([a-z ]*) bags?, )", groups[2]):
            d[group.groups()[-1]] = group.groups()[-2]
        d[groups[-1]] = groups[-2]
    if not match:
        match = re.match(r"^([a-z ]*) bags contain no other bags\.\n$", l)
        bag_name = match[1]
    bag_contents[bag_name] = d

pattern = r"^([a-z ]*)( bags contain )((([0-9]*) ([a-z ]*) bags?, )*)(([0-9]*) ([a-z ]*) bags?)\.\n$"

prog = re.compile(pattern)

bag_contents = dict()
with open("input") as f:
    for l in f:
        match(l, prog, bag_contents)
        
bag_containers = dict()

for bag_name, bag_dict in bag_contents.items():
    if bag_name not in bag_containers.keys():
        bag_containers[bag_name] = set()
    for contained_name in bag_dict.keys():
        if contained_name not in bag_containers.keys():
            bag_containers[contained_name] = set()
        bag_containers[contained_name].add(bag_name)

bag_name = "shiny gold"

trans_closure_container = set()
trans_closure_container_new = copy.deepcopy(bag_containers[bag_name])
while trans_closure_container != trans_closure_container_new:
    trans_closure_container = copy.deepcopy(trans_closure_container_new)
    for container in trans_closure_container:
        for container_container in bag_containers[container]:
            trans_closure_container_new.add(container_container)

print(len(trans_closure_container))


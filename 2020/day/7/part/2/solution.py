import copy
import re

def total_bags_contained(bag_name, bag_contents):
    bags_contained = 0
    for sub_bag_name, bag_count in bag_contents[bag_name].items():
        bag_count = int(bag_count)
        # include the bags directly in the bag in bag in question
        bags_contained += bag_count
        # recursively include transitively contained bags
        bags_contained += (
            bag_count * total_bags_contained(sub_bag_name, bag_contents)
        )
    return bags_contained

def match(l, prog, bag_contents):
    match = prog.search(l)
    d = dict()
    if match:
        groups = match.groups()
        bag_name = groups[0]
        # add all but the last listed bag to the bag_dict
        for group in re.finditer(r"(([0-9]*) ([a-z ]*) bags?, )", groups[2]):
            d[group.groups()[-1]] = group.groups()[-2]
        # add the last listed bag to the bag dict
        d[groups[-1]] = groups[-2]
    if not match:
        # get the bag name for a bag containing no other bags
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

print(total_bags_contained(bag_name, bag_contents))

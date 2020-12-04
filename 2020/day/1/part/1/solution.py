
def product_of_sum_to_2020(l):
    d = set()
    for i in l:
        if (2020 - i) in d:
            return (2020 - i) * (i)
        d.add(i)

l = []
with open('input') as f:
    for line in f:
       l.append(int(line))

print(product_of_sum_to_2020(l))

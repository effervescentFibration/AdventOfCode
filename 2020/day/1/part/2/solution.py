def product_of_sum_to_2020(l):
    # O(n log n)
    l.sort()

    # O(n)
    # radixSort(l)

    # Initialize d: map of values to frequencies
    d = {}
    for e in l:
        if e in d.keys():
            d[e] += 1
        else:
            d[e] = 1

    start_i = 0
    end_i = len(l) - 1
    while (start_i != end_i):
        start = l[start_i]
        end = l[end_i]
        partial_sum = start + end
        desideratum = 2020 - partial_sum
        # Start by excluding start and end from d
        
        d[start] -= 1
        d[end] -= 1

        if (desideratum in d.keys()) and (d[desideratum] > 0):
            return start * end * desideratum

        start_diff = l[start_i + 1] - start
        end_diff = end - l[end_i - 1]

        if start_diff <= end_diff:
            start_i += 1
        else:
            end_i -= 1

        # Reintroduce start and end from d
        # to restore invariant for next iteration
        d[start] += 1
        d[end] += 1

l = []
with open('input') as f:
    for line in f:
       l.append(int(line))

print(product_of_sum_to_2020(l))

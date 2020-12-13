import copy
import math
from collections import defaultdict

def chinese_remainder(n, a):
    prod = 1
    for t in n:
        prod *= t
    sum = 0
        
    for n_i, a_i in zip(n, a):
        # factor prod into p, n_i
        # Since all n_i in n are pairwise coprime,
        # ∏_{j != i} n_j and n_i are as well.
        p = int(prod / n_i)
        # Now we have two moduli of coprimes.
        # Use Bézout's identity,
        # invoking the extended Euclidian algorithm
        # to find the multiplicative inverse.
        sum += a_i * mul_inv(p, n_i) * p
    # Finally, all solutions are equivalent modulo ∏_i n_i,
    # so take that modulus to find the smallest solution.
    return sum % prod
 
 
def mul_inv(a, b):
    # remainders of a, b
    old_r, r = (a, b)
    # Bézout coefficients for a
    old_s, s = (1, 0)
    # Bézout coefficients for b
    old_t, t = (0, 1)
    while r != 0:
        quotient = int(old_r / r)
        old_r, r = (r, old_r - (quotient * r))
        old_s, s = (s, old_s - (quotient * s))
        old_t, t = (t, old_t - (quotient * t))
    # Returning old_s gives us the Bézout for a
    return old_s

n = []
a = []

with open("input") as file:
    # i counts the line being read
    i = 0
    for l in file:
        if i != 0:
            bus_list = str(l[0:-1]).split(",")
            # j counts the position of the bus in the table
            j = 0
            for bus in bus_list:
                if bus != "x":
                    # This is the bus ID.
                    n.append(int(bus))
                    # This is the time that elapses between
                    # the bus that comes BEFORE the target time
                    # and that target time; if k seconds elapse
                    # between the target time and next bus arrival,
                    # and the bus comes every t seconds, then
                    # t - k seconds elapses after the previous bus
                    # arrival, which is the remainder we need
                    # to use the Chinese remainder theorem.
                    a.append(int(bus) - int(j))
                j += 1
        i += 1

c = chinese_remainder(n, a)

print(repr(c))

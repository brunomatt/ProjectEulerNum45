# Triangle, pentagonal, and hexagonal numbers are generated by the following formulae:
#
# Triangle	 	Tn=n(n+1)/2	 	1, 3, 6, 10, 15, ...
# Pentagonal	 	Pn=n(3n−1)/2	 	1, 5, 12, 22, 35, ...
# Hexagonal	 	Hn=n(2n−1)	 	1, 6, 15, 28, 45, ...
# It can be verified that T285 = P165 = H143 = 40755.
#
# Find the next triangle number that is also pentagonal and hexagonal.
from math import sqrt
import time
start = time.time()

triangles = []
tri_pent_hex = []

def is_pent(x):
	f = (.5 + sqrt(.25+6*x))/3
	if f == int(f):
		return True
	else:
		return False

def is_hex(y):
    f = (1 + sqrt(1+8*y))/4
    if f == int(f):
        return True
    else:
        return False

for n in range(1, 100000):
    triangles.append(int((n * n + n) / 2))

for j in triangles:
    if is_hex(j):
        if is_pent(j):
            tri_pent_hex.append(j)

answer = tri_pent_hex[tri_pent_hex.index(40755) + 1]
print(answer)

stop = time.time()
print("Time: ", stop - start)
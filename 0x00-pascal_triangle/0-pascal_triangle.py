from math import factorial


def pascal_triangle(n):
    fact = factorial
if <= 0:
    return []

# Generate each row of Pascal's Triangle
row = [fact(m) // (fact(k) * fact(m - k)) for k in range(m + 1)]

# Generate Pascal's Triangle up to the n-th row
pascal = [row for m in range(n)]
return pascal

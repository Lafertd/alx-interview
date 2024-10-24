from math import factorial
def pascal_triangle(n):
    fact = factorial
    pascal = [[fact(m)//(fact(k)*fact(m-k)) for k in range(m+1)] for m in range(n)]
    return pascal

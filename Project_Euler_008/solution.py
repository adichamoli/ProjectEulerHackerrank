import sys
from functools import reduce
from operator import mul

t = int(input().strip())
for a0 in range(t):
    N, k = map(int, input().split())
    digits = list(map(int, input()))

    max_product = product = reduce(mul, digits[:k])

    for index in range(1, N - k):
        try:
            product //= digits[index - 1]
            product  *= digits[index + k - 1]

        except ZeroDivisionError:
            product = reduce(mul, digits[index : index + k])

        if product > max_product:
            max_product = product

    print(max_product) 
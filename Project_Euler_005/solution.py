import sys

def gcd(a, b):
    if b:
        return gcd(b, a % b)
    else:
        return a

t = int(input().strip())
for a0 in range(t):
    product = 1
    n = int(input().strip())
    for number in range(2, n + 1):
        product *= number // gcd(product, number)
    print(product)
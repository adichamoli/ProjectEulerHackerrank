#!/bin/python3
import math
import sys

def largest_prime(n):
    maxPrime = -1

    while n % 2 == 0: 
        maxPrime = 2
        n >>= 1 # equivalent to n //= 2

    for i in range(3, int(math.sqrt(n)) + 1, 2): 
        while n % i == 0: 
            maxPrime = i 
            n //= i 

    return n if n > 2 else maxPrime


t = int(input().strip())
for a0 in range(t):
    n = int(input().strip())
    print(largest_prime(n))
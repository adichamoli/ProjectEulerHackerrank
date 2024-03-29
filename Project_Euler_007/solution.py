import sys
from math import ceil, log

N_upper_bound = 10 ** 4 + 1
limit = ceil(N_upper_bound * (log(N_upper_bound) + log(log(N_upper_bound))))

limit += 1
numbers = [True] * limit
primes = []

t = int(input().strip())
for a0 in range(t):
    N = int(input().strip())
    if len(primes) >= N:
        print(primes[N - 1])
        continue
    for number in range(next(reversed(primes), 1) + 1, limit):
        if numbers[number]:
            primes.append(number)
            for multiple in range(number * number, limit, number):
                numbers[multiple] = False
            if len(primes) == N:
                print(number)
                break
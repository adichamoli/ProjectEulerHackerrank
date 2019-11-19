import sys

t = int(input().strip())
for a0 in range(t):
    N = int(input().strip())
    square_of_sum = (N * (N + 1) // 2) ** 2
    sum_of_squares = N * (N + 1) * (2 * N + 1) // 6
    print(square_of_sum - sum_of_squares)
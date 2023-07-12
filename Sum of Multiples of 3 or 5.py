#!/bin/python3

import sys

def sum_of_multiples(range_limit):
    range_limit -= 1
    return (sum_divisible_by(range_limit, 3) + sum_divisible_by(range_limit, 5) - sum_divisible_by(range_limit, 15))

def sum_divisible_by(range_limit, divisor):
    n = range_limit // divisor
    return divisor * (n * (n + 1)) // 2




t = int(input().strip())
for a0 in range(t):
    n = int(input().strip())
    result = sum_of_multiples(n)
    print(result)

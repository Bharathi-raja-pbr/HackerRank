#!/bin/python3

import math
from math import *
import os
import random
import re
import sys

#
# Complete the 'counterGame' function below.
#
# The function is expected to return a STRING.
# The function accepts LONG_INTEGER n as parameter.
#

def nearestpow(x):
    n=floor(log(x,2))
    r=int(pow(2,n))
    return r

def counterGame(n):
    # Write your code here
    turns = 0
    while(n > 1):
        np = nearestpow(n)
        print(np)
        if np == n:
            n = int(n/2)
            print(n)
        else:
            n -= np
            print(n)
        turns += 1
    
    if turns%2!=0:
        return "Louise"
    else:
        return "Richard"

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input().strip())

    for t_itr in range(t):
        n = int(input().strip())

        result = counterGame(n)

        fptr.write(result + '\n')

    fptr.close()

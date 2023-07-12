#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'superDigit' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. STRING n
#  2. INTEGER k
#
def sumofdigits(s):
    
    #to find sum of digits
    sum1=0
    for x in s:
        sum1+=int(x)
    
    #to checkwhether the sum is one digit else recursive call
    val= str(sum1)
    if len(val)!=1:
        print(val)
        val=sumofdigits(val)
    return val
    

def superDigit(n, k):
    # Write your code here
    val=(sumofdigits(n)*k)
    return sumofdigits(val)

    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = first_multiple_input[0]

    k = int(first_multiple_input[1])
    

    result = superDigit(n, k)

    fptr.write(str(result) + '\n')

    fptr.close()

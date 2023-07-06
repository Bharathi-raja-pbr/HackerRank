#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'sockMerchant' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER_ARRAY ar
#

def sockMerchant(n, ar):
    # Write your code here
    count=[0]*101
    for x in ar:
        count[x]+=1
    print(count)
    ctr=val=0
    for x in range(0,101,1):
        if count[x]==2:
            ctr+=1
        elif count[x]>2:
            ctr+=int(count[x]/2)
    return ctr
    '''    if count[x]==2:
            ctr+=1
        elif count[x]>2:
            val=int(ctr/2)
            print(val)
            ctr+=val
        else:
            continue
        print(ctr)
    return ctr'''

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    ar = list(map(int, input().rstrip().split()))

    result = sockMerchant(n, ar)

    fptr.write(str(result) + '\n')

    fptr.close()

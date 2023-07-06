#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'pickingNumbers' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY a as parameter.
#

def pickingNumbers(a):
    # Write your code here
    arr=[0]*101
    for x in a:
        arr[x]+=1
    print(arr)
    ctr=max(arr)
    index=arr.index(max(arr))
    print(index)
    val=arr[index-1]
    val1=arr[index+1]
    ctr=ctr+max(val,val1)
    
    arr.pop(index)
    print(arr)
    ctr1=max(arr)
    index1=arr.index(max(arr))
    print(index1)
    val11=arr[index1-1]
    val12=arr[index1+1]
    ctr1=ctr1+max(val11,val12)    
    
    return max(ctr,ctr1)
    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    a = list(map(int, input().rstrip().split()))

    result = pickingNumbers(a)

    fptr.write(str(result) + '\n')

    fptr.close()

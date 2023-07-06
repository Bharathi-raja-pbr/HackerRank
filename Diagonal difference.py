#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'diagonalDifference' function below.
#
# The function is expected to return an INTEGER.
# The function accepts 2D_INTEGER_ARRAY arr as parameter.
#

def diagonalDifference(arr,n):
    # Write your code here
    sum2=0;
    for i in range(0,n):
        sum2+=arr[i][i];
        ##print(sum2);
    
    sum1=0;
    k=n-1;
    j=0;
    for i in range(0,n):
        sum1+=arr[j][k];
       ## print(sum1);
        j+=1;
        k-=1;
            
    return abs(sum1-sum2);
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    arr = []

    for _ in range(n):
        arr.append(list(map(int, input().rstrip().split())))

    result = diagonalDifference(arr,n)

    fptr.write(str(result) + '\n')

    fptr.close()

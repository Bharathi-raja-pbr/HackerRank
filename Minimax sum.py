#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'miniMaxSum' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#

def miniMaxSum(arr):
    # Write your code here
    minsum=0
    maxsum=0
    arr.sort()
    for i in range(0,4):
        minsum+=arr[i];
    for i in range(len(arr)-1,len(arr)-5,-1):
        maxsum+=arr[i];
    
    print(minsum,maxsum)

if __name__ == '__main__':

    arr = list(map(int, input().rstrip().split()))

    miniMaxSum(arr)

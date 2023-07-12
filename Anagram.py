#!/bin/python3

import math
import os
import random
import re
import sys


from collections import Counter
#
# Complete the 'anagram' function below.
#
# The function is expected to return an INTEGER.
# The function accepts STRING s as parameter.
#

def anagram(s):
    # Write your code here
    count=0
    val={}
    if len(s)%2!=0:
        return -1
    else:
        mid=int(len(s)/2)
        a=s[:mid]
        b=s[mid:]
        val=Counter(a)-Counter(b)
        return sum(val.values())
            
        

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input().strip())

    for q_itr in range(q):
        s = input()

        result = anagram(s)

        fptr.write(str(result) + '\n')

    fptr.close()

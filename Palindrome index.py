#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'palindromeIndex' function below.
#
# The function is expected to return an INTEGER.
# The function accepts STRING s as parameter.
#
def ispalindrome(s):
    if s==s[::-1]:
        return 1
    else: return 0

def palindromeIndex(s):
    # Write your code here
    mid=int((len(s)+1)/2)
    for i in range(mid):
        if s[i]!=s[len(s)-i-1]:
            if(ispalindrome(s[:i]+s[i+1:])==1):
              return i
            else:
              return len(s)-i-1
    return -1
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input().strip())

    for q_itr in range(q):
        s = input()

        result = palindromeIndex(s)

        fptr.write(str(result) + '\n')

    fptr.close()

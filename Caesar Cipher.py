#!/bin/python3

import math
import os
import random
import re
import sys
import string

#
# Complete the 'caesarCipher' function below.
#
# The function is expected to return a STRING.
# The function accepts following parameters:
#  1. STRING s
#  2. INTEGER k
#

def caesarCipher(s, k):
    # Write your code here
    alpha=string.ascii_lowercase
    alpha1=string.ascii_uppercase
    print(alpha)
    print(alpha1)
    a=''
    k=k%26
    for x in s:
        val=ord(x)
        value=val+k
        if x in alpha:
            if(value>122):
               #val1=(((val%97+k)%25)-1)+97 method i did 
               value = value - ord("z") + ord("a") - 1 #method copied from net 
               a+=chr(value)
            else:
                a+=chr(value)
        elif x in alpha1:
            if(value>90):
                #val2=(((val%65+k)%25)-1)+65
                value= value - ord("Z") + ord("A") - 1
                a+=chr(value)
            else:
                a+=chr(value)
        else:
            a+=x
    return a

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    s = input()

    k = int(input().strip())

    result = caesarCipher(s, k)

    fptr.write(result + '\n')

    fptr.close()

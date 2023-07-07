#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the jumpingOnClouds function below.
def jumpingOnClouds(c, k):
    flag=1
    n=len(c)
    i=0
    energy=100
    while(flag!=0):
        val=c[(i+k)%n]
        energy-=1
        if ((i+k)%n)==0:
            if val==1:
                energy-=2
            flag=0
        else:
            if val==1:
               energy-=2
        i+=k
        #print(i)
        #print(energy)
    return energy
        

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nk = input().split()

    n = int(nk[0])

    k = int(nk[1])

    c = list(map(int, input().rstrip().split()))

    result = jumpingOnClouds(c, k)

    fptr.write(str(result) + '\n')

    fptr.close()

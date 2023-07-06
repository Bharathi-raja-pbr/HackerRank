#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'breakingRecords' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY scores as parameter.
#

def breakingRecords(scores):
    # Write your code here
    miny=maxy=0
    minx=maxx=scores[0]
    for x in range(1,len(scores)):
        if minx > scores[x]:
            miny+=1
            minx=scores[x]
        elif maxx < scores[x]:
            maxy+=1
            maxx=scores[x]
    print(miny,maxy)
    arr=[maxy,miny]
    return arr
        
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    scores = list(map(int, input().rstrip().split()))

    result = breakingRecords(scores)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()

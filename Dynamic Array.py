#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'dynamicArray' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
#  1. INTEGER n
#  2. 2D_INTEGER_ARRAY queries
#

def dynamicArray(n, queries):
    # Write your code here
    arr=[[] for _ in range(n)]
    ans=[]
    lastAnswer=0
    print(queries)
    for x in queries:
        if x[0]==1:
            #idx=((x[1]^lastAnswer)%n)
            arr[((x[1]^lastAnswer)%n)].append(x[2]) 

        elif x[0]==2:
            idx=((x[1]^lastAnswer)%n)
            v=len((arr[idx]))
            lastAnswer=arr[idx][x[2]%v]
            #lastAnswer=arr[idx][x[2]]
            ans.append(lastAnswer)
    print(ans)
    return ans
    '''last_answer = 0  #this is a solution from another person  which i referred from github
    ans=[]
    seq = [[] for _ in range(n)]

    for q in queries:
        op, x, y = q

        if op == 1:
            seq[(x ^ last_answer) % n].append(y)
        elif op == 2:
            s = seq[(x ^ last_answer) % n]
            last_answer = s[y % len(s)]
            ans.append(last_answer)
    return ans'''

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    q = int(first_multiple_input[1])

    queries = []

    for _ in range(q):
        queries.append(list(map(int, input().rstrip().split())))

    result = dynamicArray(n, queries)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()

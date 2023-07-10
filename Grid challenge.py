#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'gridChallenge' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING_ARRAY grid as parameter.
#

def gridChallenge(grid):
    # Write your code here
    new=[list(row) for row in grid]
    for x in new:
        x.sort()
    r=len(new)
    c=len(new[0])
    for j in range(c):
        for i in range(1,r):
            print(new[i-1][j],new[i][j])
            if not new[i-1][j]<=new[i][j]:
                return 'NO'
    return 'YES'



if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input().strip())

    for t_itr in range(t):
        n = int(input().strip())

        grid = []

        for _ in range(n):
            grid_item = input()
            grid.append(grid_item)

        result = gridChallenge(grid)

        fptr.write(result + '\n')

    fptr.close()

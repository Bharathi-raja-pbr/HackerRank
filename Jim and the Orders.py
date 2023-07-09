#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'jimOrders' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts 2D_INTEGER_ARRAY orders as parameter.
#

def jimOrders(orders):
    # Write your code here
    order=[]
    prep=[]
    for x in orders: 
        order.append(x[0])
        prep.append(x[1])  #can also be done with list comprehension
    t=[]
    for i in range(0,n):
        t.append(order[i]+prep[i])
    lis=[]
    for i in range(len(t)):
       ans=t.index(min(t))
       lis.append(ans+1)
       t[ans]=100000000000000000000000000000000000000000000
    print(lis)
    return lis

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    orders = []

    for _ in range(n):
        orders.append(list(map(int, input().rstrip().split())))

    result = jimOrders(orders)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()

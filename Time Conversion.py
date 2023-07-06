#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'timeConversion' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#

def timeConversion(s):
    # Write your code here
    ##print(s[8:10])
    if(s[8:10]=="PM" and s[0:2]!="12"):
        hr=int(s[0:2])+12
        result =str(hr)+s[2:8]
    elif(s[0:2]=="12" and s[8:10]=="AM"):
        hr=int(s[0:2])-12
        result="00"+s[2:8]
    elif(s[0:2]=="12" and s[8:10]=="PM"):
        result=s[0:8]
    else:
        result=s[0:8]
        
    return result;
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = timeConversion(s)

    fptr.write(result + '\n')

    fptr.close()

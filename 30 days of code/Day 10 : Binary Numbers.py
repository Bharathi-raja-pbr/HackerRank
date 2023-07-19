'''
Given a base-10 integer,n , convert it to binary (base-2).
Then find and print the base-10 integer denoting the maximum number of consecutive 1's in n's binary representation.
When working with different bases, it is common to show the base as a subscript.

Example
The binary representation of 11 is 1011 . In base 2 , there are 3 and 1 consecutive ones in two groups. Print the maximum,3 .

Input Format
A single integer,n .

Constraints
1<n<=10^6

Output Format
Print a single base-10 integer that denotes the maximum number of consecutive 1's in the binary representation of n.

Sample Input 1
5
Sample Output 1
1
Sample Input 2
13
Sample Output 2
2
'''
#!/bin/python3

import math
import os
import random
import re
import sys



if __name__ == '__main__':
    n = int(input().strip())
    v=bin(n)
    ans=v[2:]
    
    max_count=0
    curr_count=0
    
    for ch in ans:
        if ch=='1':
            curr_count+=1
            max_count=max(max_count,curr_count)
        else:
            curr_count=0
    print(max_count)

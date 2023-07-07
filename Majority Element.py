#User function template for Python 3

class Solution:
    def majorityElement(self, A, N):
        count = {}
        for x in A:
            if x in count:
                count[x] += 1
            else:
                count[x] = 1
        
        for x in count:
            if count[x] > N // 2:
                return x
        
        return -1
            


#{ 
 # Driver Code Starts
#Initial Template for Python 3

import math

from sys import stdin


def main():
        T=int(input())
        while(T>0):
            
            N=int(input())

            A=[int(x) for x in input().strip().split()]
            
            
            obj = Solution()
            print(obj.majorityElement(A,N))
            
            T-=1


if __name__ == "__main__":
    main()

'''
Two friends like to pool their money and go to the ice cream parlor. They always choose two distinct flavors and they spend all of their money.

Given a list of prices for the flavors of ice cream, select the two that will cost all of the money they have.

Example.  m=6 arr=[1,6,3,4,5]

The two flavors that cost 1 and 5 meet the criteria. Using 1-based indexing, they are at indices 1 and 5 .

Function Description

Complete the icecreamParlor function in the editor below.

icecreamParlor has the following parameter(s):

int m: the amount of money they have to spend
int cost[n]: the cost of each flavor of ice cream
Returns

int[2]: the indices of the prices of the two flavors they buy, sorted ascending
Input Format

The first line contains an integer, t , the number of trips to the ice cream parlor. The next n sets of lines each describe a visit.

Each trip is described as follows:

The integer m, the amount of money they have pooled.
The integer n, the number of flavors offered at the time.
n space-separated integers denoting the cost of each flavor: .
Note: The index within the cost array represents the flavor of the ice cream purchased.

constraints:
There will always be a unique solution.

Sample Input

STDIN       Function
-----       --------
2           t = 2
4           k = 4
5           cost[] size n = 5
1 4 5 3 2   cost = [1, 4, 5, 3, 2]
4           k = 4
4           cost[] size n = 4
2 2 4 3     cost=[2, 2,4, 3]
Sample Output

1 4
1 2

'''

def icecreamParlor(m, arr):
    # Write your code here
    for x in combinations(arr,2):
        if sum(x)==m:
            values=x
            break
    lis=[] 
    for y in values:
        a=arr.index(y)
        arr[a]=-999
        lis.append(a+1)
    
    return lis

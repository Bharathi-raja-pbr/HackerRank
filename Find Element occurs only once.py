#User function Template for python3
class Solution:
    def search(self, A, N):
        # your code here
        count={}
        for x in A:
            if x in count:
                count[x]+=1
            else:
                count[x]=1
        #print(count) {0: 2, 17: 1, 24: 2}
        for x in count:
            if count[x]==1:
                return x


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == "__main__":
	t = int (input ())
	for tc in range (t):
		n = int (input ())
		arr = list(map(int, input().split()))
		ob = Solution()
		print(ob.search(arr, n)) 
# } Driver Code Ends

if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    arr=list(arr)
    arr.sort()
    maxi=max(arr)
    '''
    for i in range(n-1,0,-1):
        if arr[i]!=maxi:
            print(arr[i])
            break;'''
    res=[]
    res=[i for i in arr if i!=maxi]
   ## print(res)
    print(max(res))

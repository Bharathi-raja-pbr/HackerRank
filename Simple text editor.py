# Enter your code here. Read input from STDIN. Print output to STDOUT
q=int(input())
s=''
stack=[]
for _ in range(q):
    query=input().split(' ')
    if query[0]=='1':
        stack.append(s)
        s+=query[1]
    elif query[0]=='2':
        stack.append(s)
        v=len(s)-int(query[1])
        s= s[:v]
    elif query[0]=='3':
        k=int(query[1])-1
        print(s[k])
    elif query[0]=='4':
        s=stack.pop()
    

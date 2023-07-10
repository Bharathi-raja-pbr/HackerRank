# Enter your code here. Read input from STDIN. Print output to STDOUT
def func(s):
    a=b=''
    for i in range(0,len(s)):
        if i%2==0:
            a+=s[i]
        else:
            b+=s[i]
    return a+' '+b

n=int(input())
while(n>0):
    s=input()
    a=func(s)
    print(a)
    n-=1

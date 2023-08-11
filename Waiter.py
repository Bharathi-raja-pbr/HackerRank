def prime(q):
    primegen=[1]*10000
    primes=[]
    
    for i in range(2,10000):
        if primegen[i]==1:
            for j in range(i,10000,i):
                 primegen[j]=0
            primes.append(i)
    '''    if len(primes)==q+1:
    break
    print(len(primes))'''
    return primes[:q+1]
    
def waiter(number, q):
    # Write your code here
    ans=prime(q)
    print(q)
    ans=prime(q+1)
    answers=[]
    A=[]
    B=[]
    for i in range(0,q,1):
        print(i)
        while number:
            x=number.pop()
            if x%ans[i]==0:
                B.append(x)
            else :
                A.append(x)
        while len(B)!=0:
            val=B.pop()
            answers.append(val)
        number=A
        A=[]
        B=[]
    
    while number:
        answers.append(number.pop())
    
    print(answers)
    return answers

def isBalanced(s):
    # Write your code here
    valid= '{[('
    invalid='}])'
    stack=[0]
    
    
    for x in s:
        if x=="}" and stack[-1]=="{":
            stack.pop()
        elif x=="]" and  stack[-1]=="[":
            stack.pop()
        elif x==")" and stack[-1]=="(":
            stack.pop()
        else:
            stack.append(x)
            
    if len(stack)==1:
        return "YES"
    else :
        return "NO"

def solve(temp):
    n=len(temp)
    ans=[0]*n
    stack=[]

    for i in range(n):
        while stack and temp[i]>temp[stack[-1]]:
            top=stack.pop()
            ans[top]=i-top

        stack.append(i)

    return ans  

temp=list(map(int,input().split()))

print(solve(temp))                                                              

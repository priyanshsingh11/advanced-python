def reversestring(s):
    left=0
    right=len(s)-1
    while(left<right):
        s[left],s[right]=s[right],s[left]
        left+=1
        right-=1

    return s

s=input("Enter a string: ").split()

ans=reversestring(s)
print(ans)
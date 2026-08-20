def palindrom(s):
    left=0
    right=len(s)-1


    while(left<right):

        if not s[left].isalnum():
            left+=1

        if not s[right].isalnum():
            right-=1
        
        if s[left]!=s[right]:
            return False

        left+=1
        right-=1

    return True        

s=input("Enter string:")

ans = palindrom(s)
print(ans)

def solve(s):
    n=len(s)
    ans=s[0]

    for i in range(n):
        if n%2 !=0:
            left=i
            right=i
            while(left>=0 and right<n and s[left]==s[right]):
                length=s[left:right+1]
                if (len(length)>len(ans)):
                    ans=length

                left-=1
                right+=1

        else:
            left=i-1
            right=i
            while(left>=0 and right<n and s[left]==s[right]):
                length=s[left:right+1]
                if (len(length)>len(ans)):
                    ans=length

                left-=1
                right+=1
        
    return ans

    
s=input("Enter string: ")
print(solve(s))

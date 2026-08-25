def solve(s):
    ans=0

    for i in range(len(s)):
        for j in range(i,len(s)):
            sub=s[i:j+1]
            if sub==sub[::-1]:ans+=1

    return ans

s=input("Enter string - ")

print(solve(s))

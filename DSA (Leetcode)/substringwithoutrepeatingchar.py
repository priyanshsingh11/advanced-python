def solve(s):
    mapping={}
    left=0
    right=0

    ans=0

    while (right<len(s)):
        char=s[right]

        if char in mapping and mapping[char]>=left:
            left=mapping[char]+1

        mapping[char]=right

        ans=max(right-left+1, ans)

        right+=1

    return ans    
        

s=input("Enter a string - ")

print(solve(s))

from collections import Counter

def solve(s1,s2):
    length=len(s2)
    ans=[]

    m1=Counter(s2)

    for i in range(len(s1)):
        m2=Counter(s1[i:i+length])
        if m1==m2:
            ans.append(i)

    return ans


s1=input()
s2=input()

print(solve(s1,s2))

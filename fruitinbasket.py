from collections import Counter

def solve(fruits):
    n=len(fruits)
    left=0
    right=0
    ans=0
    # count=2

    while right<n:
        m1=Counter(fruits[left:right+1])

        while len(m1)>2:
            m1[fruits[left]]-=1
            if m1[fruits[left]]==0:
               del m1[fruits[left]]
            left+=1

        else:
            ans=max(ans,right-left+1)

        right+=1

    return ans

fruits=list(map(int,input().split()))

print(solve(fruits))

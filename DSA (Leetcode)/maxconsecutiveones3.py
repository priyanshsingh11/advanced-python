def solve(nums,k):
    left=0
    right=0
    ans=0
    n=len(nums)
    zeros=0

    while right<n:
        if nums[right]==0:
            zeros+=1

        if zeros<=k:
            ans=max(ans,right-left+1)

        else:
            if nums[left]==0:
                zeros-=1
            left+=1

        right+=1

    return ans           

nums=list(map(int,input().split()))
k=int(input())

print(solve(nums,k))

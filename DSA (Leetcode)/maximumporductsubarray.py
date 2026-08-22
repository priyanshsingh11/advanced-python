def solve(nums):
    start=nums[0]
    ans=nums[0]
    maxi=nums[0]
    mini=nums[0]

    for i in range(1,len(nums)):
        curr=nums[i]

        if curr<0:
            mini,maxi=maxi,mini

        maxi=max(curr,maxi*curr)
        mini=min(curr,mini*curr)
        ans=max(ans,maxi)

    return ans

nums=list(map(int,input("Enter array:").split()))

print(solve(nums))

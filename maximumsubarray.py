def maximumsubarray(nums):
    left=0
    right=1
    ans=nums[left]
    max_sum=nums[left]

    for i in range(1,len(nums)):
        max_sum=max(nums[i],max_sum+nums[i])
        ans=max(ans,max_sum)
        # right+=1

    return ans


nums=list(map(int,input("Enter the array: ").split()))

ans=maximumsubarray(nums)
print(ans)

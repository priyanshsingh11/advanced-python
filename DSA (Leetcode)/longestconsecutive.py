def solve(nums):
    # nums.sort()
    # ans=1
    # curr=1
    # length=0

    # for i in range(1,len(nums)):
    #     if nums[i]==nums[i-1]+1:
    #         curr+=1

    #     elif nums[i]==nums[i-1]:
    #         continue

    #     else:
    #         curr=1

    #     ans=max(ans,curr)

    # return ans
    setter=set(nums)
    ans=1

    for num in setter:
        if num-1 not in setter:
            length=1
            curr=num

            while (curr+1) in setter:
                length+=1
                curr+=1

        ans=max(ans,length)

    return ans


nums=list(map(int,input("Enter array:").split()))

print(solve(nums))

def subarraysumequalK(nums, k):
    n=len(nums)
    curr_sum=0
    ans=0
    freq={0:1}

    for num in nums:
        curr_sum+=num

        if curr_sum-k in freq:
            ans+=freq[curr_sum-k]

        freq[curr_sum] = freq.get(curr_sum, 0) + 1

    return ans

nums=list(map(int,input("Enter a array-").split()))
k=int(input("Enter a number-"))

print(subarraysumequalK(nums,k))

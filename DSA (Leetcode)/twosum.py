def twoSum(nums, x):
    dict={}

    for i in range(len(nums)):
        current=nums[i]
        diff=x-current

        if diff in dict:
            return [dict[diff],i]

        else:
            dict[current]=i


nums=list(map(int,input("enter array:").split()))
x=int(input("enter number:"))

ans=twoSum(nums,x)
print(ans)


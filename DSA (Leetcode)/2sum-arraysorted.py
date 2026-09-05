def solve(nums,target):
    n=len(nums)
    left=0
    right=n-1

    while left<right:
        if nums[left]+nums[right]==target: return left,right

        elif nums[left]+nums[right]<target: left+=1
        else:
            right-=1


nums=list(map(int,input("Enter the array - ")))
target=int(input("Enter the number - "))

print(solve(nums, target))

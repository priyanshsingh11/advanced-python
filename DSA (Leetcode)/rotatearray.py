def solve(nums,k):
    n=len(nums)

    k=k%n

    nums.reverse()
    nums[:k]=reversed(nums[:k])
    nums[k:]=reversed(nums[k:])

    return nums

nums=list(map(int,input("Enter array:").split()))
k=int(input("Enter the number:"))

print(solve(nums,k))

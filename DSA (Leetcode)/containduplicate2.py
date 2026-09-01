def solve(nums,k):
    n=len(nums)
    store={}

    for i in range(n):
        if nums[i] in store:
            if abs(i-store[nums[i]])<=k: return True

        else:
            store[nums[i]]=i

    return False


nums=list(map(int,input("enter nums:").split()))
k=int(input("Enter a number:"))

print(solve(nums,k))

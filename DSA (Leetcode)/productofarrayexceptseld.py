def product(nums):
    n=len(nums)
    ans=[0]*n
    left=[0]*n
    right=[0]*n

    left[0]=1
    right[n-1]=1

    for i in range(1,len(nums)):
        left[i]=left[i-1]*nums[i-1]

    for i in range(n-2,-1,-1):
        right[i]=right[i+1]*nums[i+1]

    for i in range(n):
        ans[i]=left[i]*right[i]

    return ans        

nums=list(map(int,input("Enter Array: ").split()))

print(product(nums))

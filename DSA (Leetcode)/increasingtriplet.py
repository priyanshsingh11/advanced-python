def increasingTriplet(nums):
    n=len(nums)
    first=float('inf')
    second=float('inf')

    for num in nums:
        if num<=first:
            first=num

        elif num<=second:
            second=num

        else:
            return True

    return False

nums=list(map(int,input("Enter a array - ").split()))

print(increasingTriplet(nums))

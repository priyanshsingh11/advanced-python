def solve(nums):
    ans=[]
    freq={}

    for num in nums:
        freq[num]=freq.get(num,0)+1

    for color in [0,1,2]:
        if color in freq:
            ans.extend([color]*freq[color])

    return ans


nums=list(map(int,input("Enter the array - ").split()))
print(solve(nums))

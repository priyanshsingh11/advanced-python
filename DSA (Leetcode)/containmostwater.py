def solve(height):
    n=len(height)
    left=0
    right=n-1
    ans=0

    while(left<right):
        width=right-left
        water=min(height[left],height[right])*width
        ans=max(water,ans)
    
        if height[left]<height[right]: left+=1
        else: 
            right-=1
            
    return ans


height=list(map(int,input("Enter the array - ").split()))

print(solve(height))

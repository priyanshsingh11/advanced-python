def buyandsell(array):
    left=0
    right=1
    ans=0

    while right<len(array):
        profit=array[right]-array[left]
        if array[left]<array[right]:
            ans=max(ans,profit)

        else:
            left=right

        right+=1

    return ans



array=list(map(int,input("Enter the array:").split()))

ans = buyandsell(array)
print(ans)

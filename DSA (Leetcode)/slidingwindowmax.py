import heapq

def solve(nums,k):
    n=len(nums)

    heap=[]
    ans=[]

    for i in range(n):
        heapq.heappush(heap, (-nums[i],i))

        if i>=k-1:
            while heap[0][1]<i-k+1:
              heapq.heappop(heap)

            ans.append(-heap[0][0])

    return ans

nums=list(map(int,input("Enter an array - ").split()))
k=int(input("Enter a number - "))

print(solve(nums,k))

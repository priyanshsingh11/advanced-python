import heapq
from collections import Counter

def solve(nums,k):
    n=len(nums)
    freq=Counter(nums)

    max_heap=[]
    ans=[]

    for num,count in freq.items():
        heapq.heappush(max_heap,(-count,num))

    for _ in range(k):
        ans.append(heapq.heappop(max_heap)[1])

    return ans


nums=list(map(int,input("Enter Array: ").split()))
k=int(input("Enter number: "))

print(solve(nums,k))

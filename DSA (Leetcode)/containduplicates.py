def duplicates(array):
    dict={}

    for i in range(len(array)):
        curr=array[i]

        if curr in dict:
            return True

        else:
            dict[curr]=1

    return False


array=list(map(int,input("enter nums:").split()))

ans=duplicates(array)
print(ans)

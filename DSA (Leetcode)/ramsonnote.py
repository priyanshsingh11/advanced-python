def solve(a,b):
    store={}

    for i in b:
        if i in store:
            store[i]+=1
        else:
            store[i]=1

    for j in a:
        if j in store:
            store[j]-=1
        else:
            return False

        if store[j]==0: del store[j]

    return True

a=input("Enter string 1 - ")
b=input("Enter string 2 - ")

print(solve(a,b))

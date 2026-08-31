def solve(s,t):
    if len(s)!=len(t): return False

    first={}
    second={}

    for a,b in zip(s,t):
        if a in first and first[a]!=b: return False
        if b in second and second[b]!=a: return False

        first[a]=b
        second[b]=a

    return True

s=input("Enter string1 -")
t=input("Enter string2 -")

print(solve(s,t))

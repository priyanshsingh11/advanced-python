def solve(pattern,s):
    if len(pattern) != len(s): return False

    first={}
    second={}

    for a,b in zip(pattern,s):
            if a in first and first[a]!=b: return False
            if b in second and second[b]!=a: return False
    
            first[a]=b
            second[b]=a
    
    return True

pattern=input("Enter a string-")
s=input("Enter a word- ").split()

print(solve(pattern,s))

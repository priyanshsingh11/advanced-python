def solve(strs):
    ans={}

    for words in strs:
        key=''.join(sorted(words))

        if key not in ans:
            ans[key]=[]

        ans[key].append(words)

    return list(ans.values())

strs=input("Enter all: ").split()

print(solve(strs))

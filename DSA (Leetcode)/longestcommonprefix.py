def solve(strs):
    first=strs[0]

    for s in strs[1:]:
        while not s.startswith(first):
            first=first[:-1]

        if first=="":
            return ""

    return first

strs = input("Enter strings: ").split()

print(solve(strs))

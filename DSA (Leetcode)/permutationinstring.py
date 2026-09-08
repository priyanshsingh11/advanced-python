def solve(s1,s2):
    m1={}

    for ch in s1:
        m1[ch]=m1.get(ch,0)+1

    packet=len(s1)

    for ch in range(len(s2)):
        m2={}
        for char in s2[ch:ch+packet]:
            m2[char]=m2.get(char,0)+1

        if m1==m2: return True


    return False

s1=input()
s2=input()

print(solve(s1,s2))

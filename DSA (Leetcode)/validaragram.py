def anagram(one,two):
    dict={}
    for char in one:
        if char in dict:
            dict[char]+=1

        else:
            dict[char]=1

    for char in two:
        if char in dict:
            dict[char]-=1

        else: return False

        if dict[char]<0: return False


    return True
    


one=input("enter string 1")
two=input("enter string 2")

ans=anagram(one,two)
print(ans)

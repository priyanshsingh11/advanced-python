def solve(s):
    stack=[]

    for ch in s:
        if ch == "(" or ch == "{" or ch == "[":
            stack.append(ch)

        else:
            if not stack: return False 
            top=stack.pop()

            if ((ch==')' and top!='(') or
                    (ch=='}' and top!='{') or
                    (ch==']' and top!='[')):
                    return False   
             
    if stack: return False
    return True

s=input()

print(solve(s))

def isValid(s:str)-> bool:
    stack = []
    bracket_types = {"(": ")", "{":"}", "[":"]"}

    for c in s:
        if (len(stack) == 0):
            stack.append(c)
            continue
        if(bracket_types.get(stack[-1]) and bracket_types[stack[-1]] == c):
            stack.pop()
        else:
            stack.append(c)
    
    return len(stack) == 0

s = "([)]"
output = isValid(s)
print(output)
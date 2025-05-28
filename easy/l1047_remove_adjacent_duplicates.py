def removeDuplicates(s: str) -> str:
    stack = []
    for i in s:
        if(len(stack) >= 1 and stack[-1]==i):
            stack.pop()
            continue
        stack.append(i)
    return "".join(stack)

a = "abbaca"
print(removeDuplicates(a))
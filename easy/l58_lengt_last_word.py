def len_last_word(s:str) -> int:
    count = 0
    start = 1
    j = len(s)-1
    while(s[j] == " "):
        start+= 1
        j -= 1
    
    for i in range(len(s)-start, -1,  -1):
        if s[i]==" ":
            break
        count += 1
    return count

s = "Hello World   "
a = len_last_word(s)
print(a)
def longest_palindrome(s:str)->int:
    ans: int = 0
    count = {}
    for c in s:
        count[c] = count.get(c, 0) + 1

    is_there_odd:bool = False
    for k, v in count.items():
        if(v%2 == 0):
            ans += v
        else:
            ans += v-1
            is_there_odd = True
    if(is_there_odd):
        ans += 1
    return ans

def longest_palindrome_set(s:str)->int:
    temp_set = set()
    ans = 0
    for c in s:
        if c in temp_set:
            ans += 2
            temp_set.remove(c)
        else:
            temp_set.add(c)
    if(temp_set):
        ans += 1
    return ans

a = "aAbBABbabbfffffg" 
so  = longest_palindrome_set(a)
print(so)
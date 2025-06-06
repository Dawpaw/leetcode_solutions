def str_str(haystack:str, needle: str)->int:
    right = 0
    result = -1

    haystack_len = len(haystack)
    needle_len = len(needle)

    if(haystack_len<needle_len):
        return result
    
    for left in range(haystack_len-needle_len+1):
        if (haystack[left] == needle[0]):
            right = 1
            while(right < needle_len):
                if(haystack[left + right] != needle[right]):
                    break
                right += 1
            if right == needle_len:
                return left
    return result

haystack = "mississippi"
needle = "issipi"



str_str("a", "a")
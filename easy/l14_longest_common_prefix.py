def longestCommonPrefix(strs: list[str]) -> str:
    if(len(strs)==0):
        return ""
    
    shortest_word = min(strs)

    for i, ch in enumerate(shortest_word) :
        for word in strs:
            if word[i] != ch:
                return shortest_word[:i]
    
    return shortest_word


strs = ["cat","flow","flight"]
print(longestCommonPrefix(strs))

def longest_common_subsequence(text1:str, text2:str) -> int: 
    table = [[0 for _ in range(len(text2)+1)] for _ in range(len(text1) + 1)]
    for i in range(len(text1) - 1, -1, -1):
        for j in range(len(text2) - 1, -1, -1):
            if (text1[i] == text2[j]):
                table[i][j] = 1 + table[i+1][j+1]
            else:
                table[i][j] = max(table[i][j+1], table[i+1][j])
    return table[0][0]
    

if __name__ == "__main__":
    text1 = "abcde"
    text2 = "jpg"
    res = longest_common_subsequence(text1, text2)
    print(res)
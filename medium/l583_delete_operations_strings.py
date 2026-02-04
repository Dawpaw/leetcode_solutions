def minDistance(word1: str, word2: str) -> int:
    table = [[0 for _ in range(len(word2)+1)] for _ in range(len(word1) + 1)]
    for i in range(len(word1) - 1, -1, -1):
        for j in range(len(word2) - 1, -1, -1):
            if (word1[i] == word2[j]):
                table[i][j] = 1 + table[i+1][j+1]
            else:
                table[i][j] = max(table[i][j+1], table[i+1][j])
    common_len = table[0][0] 
    return len(word1) + len(word2) - 2*common_len


if(__name__ == "__main__"):
    word1 = "ab"
    word2 = "bc"
    res = minDistance(word1, word2)
    print(res)
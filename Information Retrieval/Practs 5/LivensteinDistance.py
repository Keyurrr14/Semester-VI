# With Matrix
def levenshtein(str1, str2):
    m = len(str1)
    n = len(str2)
    grid = [[0 for _ in range(n + 1)] for _ in range(m + 1)]

    for i in range(m + 1):
        grid[i][0] = i
    for j in range(n + 1):
        grid[0][j] = j

    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if str1[i - 1] == str2[j - 1]:
                grid[i][j] = grid[i - 1][j - 1]
            else:
                grid[i][j] = 1 + min(grid[i - 1][j], grid[i][j - 1], grid[i - 1][j - 1])

    for row in grid:
        print(row)
    return grid[m][n]

print(f"Distance between cat and cut: {levenshtein('cat', 'cut')}")


# With Recursion
def levenshtein_distance(str1, str2):
    if len(str1) == 0:
        return len(str2)
    if len(str2) == 0:
        return len(str1)
    
    if str1[0] == str2[0]:
        return levenshtein_distance(str1[1:], str2[1:])
    
    return 1 + min(
        levenshtein_distance(str1[1:], str2[1:]),
        levenshtein_distance(str1[1:], str2),
        levenshtein_distance(str1, str2[1:])
    )

word1 = "cat"
word2 = "cut"
print(f"Distance between {word1} and {word2}: {levenshtein_distance(word1, word2)}")

word1 = "book"
word2 = "back"
print(f"Distance between {word1} and {word2}: {levenshtein_distance(word1, word2)}")



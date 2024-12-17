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

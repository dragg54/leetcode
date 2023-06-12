def wordPattern(pattern: str, s: str) -> bool:
    word = s.split(" ")
    if (len(word) != len(pattern)):
        return False
    mapSt = {}
    mapTs = {}
    for i,j in zip(pattern, word):
        if i in mapSt and mapSt[i] != j or j in mapTs and mapTs[j] != i:
            return False
        mapSt[i] = j
        mapTs[j] = i
    return True

print(wordPattern("abba", "dog cat cat dog"))
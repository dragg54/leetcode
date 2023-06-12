def isSubsequence(s: str, t: str) -> bool:
    count = 0
    res = False
    for i in range(len(s)):
        for j in range(count, len(t)):
            res = False
            if t[j] == s[i]:
                count = j + 1
                res = True
                break
            res = False
    return True

print(isSubsequence("acb", "ahbgdc"))
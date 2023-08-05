import math


def binarySubs(s):
    prevCnt = 0
    ans = 0
    i = 0
    while i < len(s):
        currCnt = 1
        while i < len(s) - 1 and s[i] == s[i + 1]:
            currCnt += 1
            i += 1
        if prevCnt > 0:
            ans += min(prevCnt, currCnt)
        prevCnt = currCnt
        i += 1
    return ans


print(math.inf)

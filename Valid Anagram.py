def isAnagram(a, b):
    if len(a) != len(b):
        return False
    countA, countB = {}, {}
    for i in range(len(a)):
        countA[a[i]] = 1 + countA.get(a[i], 0)
        countB[b[i]] = 1 + countB.get(b[i], 0)
    for c in a:
        if countA[c] != countB.get(c, 0):
            return False
    return True

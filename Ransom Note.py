def ransomNote(ransom, magazine):
    mapRans = {}
    mapMagz = {}
    for i, j in zip(ransom, magazine):
        if i not in magazine:
            return False
        mapRans[i] = 1 + mapRans.get(i, 0)
        mapMagz[j] = 1 + mapMagz.get(j, 0)
    for c in ransom:
        if mapRans[c] > mapRans[c]:
            return False
    return True

print(ransomNote("acdi", "aabcd"))
def isIsomorphic(s, t):
    mapST, mapTS = {}, {}
    for i in range(len(s)):
        c1, c2 = mapST[i], mapTS[i]
        if((c1 in mapST and mapST[c1] != c2) or
            (c2 in mapTS and mapTS[c2] != c1)):
            return False
        mapST[c1] = c2
        mapTS[c2] = c1
    return True
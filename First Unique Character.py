def firstUniqChar(s):
    """
    :type s: str
    :rtype: int
    """
    map = {}
    for i in s:
        map[i] = 1 + map.get(i, 0)
    for i in map:
        if map[i] < 2:
            return s.index(i)
    return -1

print(firstUniqChar("leetcode"))
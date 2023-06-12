def firstBadVersion(n):
    left = 0
    right = n
    while left <= right:
        midpoint = (left + right)//2
        if isBadVersion(midpoint):
            if not isBadVersion(midpoint - 1):
                return midpoint
            else:
                left = midpoint - 1
        else:
            right = midpoint + 1
    return -1